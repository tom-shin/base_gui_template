#!/usr/bin/env python3
import os.path

from PyQt5.QtCore import QThread

from source.head import *
from source.source_files.testSetCreation import TestSetCreation

if getattr(sys, 'frozen', False):  # PyInstaller로 패키징된 경우
    BASE_DIR = os.path.dirname(sys.executable)  # 실행 파일이 있는 폴더
    RESOURCE_DIR = sys._MEIPASS  # 임시 폴더(내부 리소스 저장됨)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = BASE_DIR  # 개발 환경에서는 현재 폴더 사용


class LoadFiles(QThread, FileManager):
    LoadFiles_finished_file_list_signal = pyqtSignal(list)

    def __init__(self, dirpath, file_filter=None):
        super().__init__()
        self.dirpath = dirpath

        if file_filter is None:
            self.filter = []
        else:
            self.filter = file_filter

    def run(self):
        print("File Loading ...")
        file_list = self.search_files(directory=self.dirpath, file_filter=self.filter)

        self.LoadFiles_finished_file_list_signal.emit(file_list)

    def stop(self):
        self.quit()
        self.wait(3000)


class ProjectMainWindow(QtWidgets.QMainWindow, FileManager):
    def __init__(self):
        super().__init__()

        self.file_list = None
        self.mainFrame_ui = None
        self.widget_ui = None
        self.progress_dialog = None
        self.threadList = []
        self.finished_flag = False

        control_parameter_path = os.path.join(BASE_DIR, "control_parameter.json")

        # 만약 실행 폴더에 control_parameter.json이 없으면, 임시 폴더에서 복사
        if not os.path.exists(control_parameter_path):
            original_path = os.path.join(RESOURCE_DIR, "source", "control_parameter.json")
            shutil.copyfile(original_path, control_parameter_path)

        _, self.CONFIG_PARAMS = self.load_json(control_parameter_path, use_encoding=False)

        # 기존 UI 로드
        rt = load_module_func(module_name="source.ui_designer.main_frame")
        self.mainFrame_ui = rt.Ui_MainWindow()
        self.mainFrame_ui.setupUi(self)

        self.mainFrameInitialize()
        os.environ["OPENAI_API_KEY"] = "".join(self.CONFIG_PARAMS["openai"]["key"])

    def mainFrameInitialize(self):
        self.mainFrame_ui.n_lineEdit.setText(str(self.CONFIG_PARAMS["test_set_creation"]["test_size"]))

    def closeEvent(self, event):
        answer = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:
            for s_thread in self.threadList:
                s_thread.stop()

            event.accept()
        else:
            event.ignore()

    def normalOutputWritten(self, text):
        cursor = self.mainFrame_ui.logtextbrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)

        # 기본 글자 색상 설정
        color_format = cursor.charFormat()
        if "><" in text:
            color_format.setForeground(QtCore.Qt.red)
        else:
            color_format.setForeground(QtCore.Qt.black)

        cursor.setCharFormat(color_format)
        cursor.insertText(text)

        # 커서를 최신 위치로 업데이트
        self.mainFrame_ui.logtextbrowser.setTextCursor(cursor)
        self.mainFrame_ui.logtextbrowser.ensureCursorVisible()

    def cleanLogBrowser(self):
        self.mainFrame_ui.logtextbrowser.clear()

    def connectSlotSignal(self):
        """ sys.stdout redirection """
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        self.mainFrame_ui.log_clear_pushButton.clicked.connect(self.cleanLogBrowser)
        self.mainFrame_ui.gengenpushButton.clicked.connect(self.testSetCreation_job)
        self.mainFrame_ui.dirpushButton.clicked.connect(self.testSetCreation_doc_selection)
        self.mainFrame_ui.clear_pushButton.clicked.connect(self.testSetCreation_erase_file_list)

    def testSetCreation_erase_file_list(self):
        self.mainFrame_ui.filelistlistWidget.clear()

    def finished_TestSetCreation(self):
        print("finished_TestSetCreation")
        self.mainFrame_ui.filelistlistWidget.clear()

        if self.progress_dialog is not None:
            self.progress_dialog.close()
            self.progress_dialog = None

        for thread in self.threadList:
            thread.stop()

    def testSetCreation_gui_set(self, file_list):
        print("File Loading Done.")
        self.file_list = file_list
        self.mainFrame_ui.filelistlistWidget.addItems(file_list)
        self.mainFrame_ui.filenumlineEdit.setText(str(len(file_list)))

    def testSetCreation_doc_selection(self):
        m_dir = QFileDialog.getExistingDirectory(self, "Select Directory")

        if not m_dir:
            return

        load_file_instance = LoadFiles(dirpath=m_dir, file_filter=self.CONFIG_PARAMS["filter"]["include"])
        load_file_instance.LoadFiles_finished_file_list_signal.connect(self.testSetCreation_gui_set)
        load_file_instance.start()

        self.threadList.append(load_file_instance)

        self.mainFrame_ui.dirlineEdit.setText(os.path.normpath(m_dir))

    def testSetCreation_job(self):
        self.progress_dialog = ProgressDialog(message="TestSet Creation")
        self.progress_dialog.progress_stop_signal.connect(self.finished_TestSetCreation)

        test_size = self.CONFIG_PARAMS["test_set_creation"]["test_size"]

        ctrl_parm = {"file_list": self.file_list, "gpt_model": "gpt-4o-mini", "test_size": test_size,
                     "user": "tom.shin", "file_extension": self.CONFIG_PARAMS["filter"]["include"]}

        thread = TestSetCreation(ctrl_parm=ctrl_parm)
        thread.TestSetCreation_finished_thread_signal.connect(self.finished_TestSetCreation)
        thread.TestSetCreation_progress_signal.connect(self.progress_dialog.update_progress)
        thread.TestSetCreation_text_update_signal.connect(self.progress_dialog.update_text)
        thread.TestSetCreation_total_files_cnt_signal.connect(self.progress_dialog.set_progress_max)

        thread.start()

        self.threadList.append(thread)

        self.progress_dialog.show_progress()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # QApplication 생성 (필수)

    app.setStyle("Fusion")
    ui = ProjectMainWindow()
    ui.showMaximized()
    ui.connectSlotSignal()

    sys.exit(app.exec_())
