#!/usr/bin/env python3

from source.head import *
from source.source_files.test_example import ExampleThread

if getattr(sys, 'frozen', False):  # PyInstaller로 패키징된 경우
    BASE_DIR = os.path.dirname(sys.executable)  # 실행 파일이 있는 폴더
    RESOURCE_DIR = sys._MEIPASS  # 임시 폴더(내부 리소스 저장됨)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = BASE_DIR  # 개발 환경에서는 현재 폴더 사용


class ProjectMainWindow(QtWidgets.QMainWindow, FileManager):
    def __init__(self):
        super().__init__()

        # 실행 파일이 있는 폴더에 저장할 실제 JSON 파일 경로
        control_parameter_path = os.path.join(BASE_DIR, "control_parameter.json")

        # 만약 실행 폴더에 control_parameter.json이 없으면, 임시 폴더에서 복사
        if not os.path.exists(control_parameter_path):
            original_path = os.path.join(RESOURCE_DIR, "source", "control_parameter.json")
            shutil.copyfile(original_path, control_parameter_path)

        _, self.CONFIG_PARAMS = self.load_json(control_parameter_path, use_encoding=False)

        """ for main frame & widget """
        self.mainFrame_ui = None
        self.widget_ui = None
        self.progress_dialog = None
        self.threadList = []

        # 기존 UI 로드
        rt = load_module_func(module_name="source.ui_designer.main_frame")
        self.mainFrame_ui = rt.Ui_MainWindow()
        self.mainFrame_ui.setupUi(self)

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
        self.mainFrame_ui.clearlog_pushButton.clicked.connect(self.cleanLogBrowser)
        self.mainFrame_ui.execute_pushButton.clicked.connect(self.sub_job)

    def finished_ExampleThread(self):
        self.progress_dialog.close_dialog()
        for thread in self.threadList:
            thread.stop()

    def sub_job(self):
        self.progress_dialog = ProgressDialog(message="Test Program")
        # self.progress_dialog.set_progress_max(max_value=10)

        thread = ExampleThread()
        thread.ExampleThread_finished_thread_signal.connect(self.finished_ExampleThread)

        thread.ExampleThread_progress_signal.connect(self.progress_dialog.update_progress)
        thread.ExampleThread_text_update_signal.connect(self.progress_dialog.update_text)

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
