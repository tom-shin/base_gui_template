# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1136, 2814)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scenario_checkBox = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.scenario_checkBox.setFont(font)
        self.scenario_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scenario_checkBox.setAutoFillBackground(False)
        self.scenario_checkBox.setObjectName("scenario_checkBox")
        self.horizontalLayout_6.addWidget(self.scenario_checkBox)
        self.logonoffcheckBox = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logonoffcheckBox.sizePolicy().hasHeightForWidth())
        self.logonoffcheckBox.setSizePolicy(sizePolicy)
        self.logonoffcheckBox.setObjectName("logonoffcheckBox")
        self.horizontalLayout_6.addWidget(self.logonoffcheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.src_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.src_label.sizePolicy().hasHeightForWidth())
        self.src_label.setSizePolicy(sizePolicy)
        self.src_label.setObjectName("src_label")
        self.horizontalLayout_3.addWidget(self.src_label)
        self.srclineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srclineEdit.sizePolicy().hasHeightForWidth())
        self.srclineEdit.setSizePolicy(sizePolicy)
        self.srclineEdit.setObjectName("srclineEdit")
        self.horizontalLayout_3.addWidget(self.srclineEdit)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.licenselineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.licenselineEdit.sizePolicy().hasHeightForWidth())
        self.licenselineEdit.setSizePolicy(sizePolicy)
        self.licenselineEdit.setObjectName("licenselineEdit")
        self.horizontalLayout_3.addWidget(self.licenselineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.questioin_groupBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.questioin_groupBox.setFont(font)
        self.questioin_groupBox.setObjectName("questioin_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.questioin_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathlineEdit = QtWidgets.QLineEdit(self.questioin_groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pathlineEdit.setFont(font)
        self.pathlineEdit.setReadOnly(True)
        self.pathlineEdit.setObjectName("pathlineEdit")
        self.horizontalLayout_2.addWidget(self.pathlineEdit)
        self.verticalLayout_5.addWidget(self.questioin_groupBox)
        self.contexts_groupBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.contexts_groupBox.setFont(font)
        self.contexts_groupBox.setObjectName("contexts_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contexts_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.parametersetting_textEdit = QtWidgets.QTextEdit(self.contexts_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametersetting_textEdit.sizePolicy().hasHeightForWidth())
        self.parametersetting_textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.parametersetting_textEdit.setFont(font)
        self.parametersetting_textEdit.setReadOnly(True)
        self.parametersetting_textEdit.setObjectName("parametersetting_textEdit")
        self.verticalLayout.addWidget(self.parametersetting_textEdit)
        self.verticalLayout_5.addWidget(self.contexts_groupBox)
        self.groupBox_10 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.memory_graph = QtWidgets.QVBoxLayout()
        self.memory_graph.setObjectName("memory_graph")
        self.verticalLayout_13.addLayout(self.memory_graph)
        self.verticalLayout_5.addWidget(self.groupBox_10)
        self.horizontalLayout.addWidget(self.frame)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.elapsedlineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elapsedlineEdit.sizePolicy().hasHeightForWidth())
        self.elapsedlineEdit.setSizePolicy(sizePolicy)
        self.elapsedlineEdit.setObjectName("elapsedlineEdit")
        self.gridLayout_7.addWidget(self.elapsedlineEdit, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_7)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 5, 0, 1, 1)
        self.directshape = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directshape.sizePolicy().hasHeightForWidth())
        self.directshape.setSizePolicy(sizePolicy)
        self.directshape.setObjectName("directshape")
        self.gridLayout_9.addWidget(self.directshape, 1, 1, 1, 1)
        self.onnxdomain = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onnxdomain.sizePolicy().hasHeightForWidth())
        self.onnxdomain.setSizePolicy(sizePolicy)
        self.onnxdomain.setObjectName("onnxdomain")
        self.gridLayout_9.addWidget(self.onnxdomain, 6, 1, 1, 1)
        self.modelvalidaty = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelvalidaty.sizePolicy().hasHeightForWidth())
        self.modelvalidaty.setSizePolicy(sizePolicy)
        self.modelvalidaty.setObjectName("modelvalidaty")
        self.gridLayout_9.addWidget(self.modelvalidaty, 0, 1, 1, 1)
        self.direct_shape_label = QtWidgets.QLabel(self.groupBox_9)
        self.direct_shape_label.setObjectName("direct_shape_label")
        self.gridLayout_9.addWidget(self.direct_shape_label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.onnxruntime_InferenceSession = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onnxruntime_InferenceSession.sizePolicy().hasHeightForWidth())
        self.onnxruntime_InferenceSession.setSizePolicy(sizePolicy)
        self.onnxruntime_InferenceSession.setObjectName("onnxruntime_InferenceSession")
        self.gridLayout_9.addWidget(self.onnxruntime_InferenceSession, 3, 1, 1, 1)
        self.onnxlineEdit = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onnxlineEdit.sizePolicy().hasHeightForWidth())
        self.onnxlineEdit.setSizePolicy(sizePolicy)
        self.onnxlineEdit.setObjectName("onnxlineEdit")
        self.gridLayout_9.addWidget(self.onnxlineEdit, 7, 1, 1, 1)
        self.onnxruntime_InferenceSessiontextEdit = QtWidgets.QTextEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onnxruntime_InferenceSessiontextEdit.sizePolicy().hasHeightForWidth())
        self.onnxruntime_InferenceSessiontextEdit.setSizePolicy(sizePolicy)
        self.onnxruntime_InferenceSessiontextEdit.setObjectName("onnxruntime_InferenceSessiontextEdit")
        self.gridLayout_9.addWidget(self.onnxruntime_InferenceSessiontextEdit, 4, 1, 1, 1)
        self.modeltype = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeltype.sizePolicy().hasHeightForWidth())
        self.modeltype.setSizePolicy(sizePolicy)
        self.modeltype.setObjectName("modeltype")
        self.gridLayout_9.addWidget(self.modeltype, 5, 1, 1, 1)
        self.onnxlabel = QtWidgets.QLabel(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onnxlabel.sizePolicy().hasHeightForWidth())
        self.onnxlabel.setSizePolicy(sizePolicy)
        self.onnxlabel.setObjectName("onnxlabel")
        self.gridLayout_9.addWidget(self.onnxlabel, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_9)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_9)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 6, 0, 1, 1)
        self.simplifier = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simplifier.sizePolicy().hasHeightForWidth())
        self.simplifier.setSizePolicy(sizePolicy)
        self.simplifier.setObjectName("simplifier")
        self.gridLayout_9.addWidget(self.simplifier, 2, 1, 1, 1)
        self.simplifier_label = QtWidgets.QLabel(self.groupBox_9)
        self.simplifier_label.setObjectName("simplifier_label")
        self.gridLayout_9.addWidget(self.simplifier_label, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_9)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.initlineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initlineEdit.sizePolicy().hasHeightForWidth())
        self.initlineEdit.setSizePolicy(sizePolicy)
        self.initlineEdit.setObjectName("initlineEdit")
        self.gridLayout.addWidget(self.initlineEdit, 0, 1, 1, 1)
        self.initlabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initlabel.sizePolicy().hasHeightForWidth())
        self.initlabel.setSizePolicy(sizePolicy)
        self.initlabel.setObjectName("initlabel")
        self.gridLayout.addWidget(self.initlabel, 0, 0, 1, 1)
        self.inittextEdit = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inittextEdit.sizePolicy().hasHeightForWidth())
        self.inittextEdit.setSizePolicy(sizePolicy)
        self.inittextEdit.setObjectName("inittextEdit")
        self.gridLayout.addWidget(self.inittextEdit, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.conversionlineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversionlineEdit.sizePolicy().hasHeightForWidth())
        self.conversionlineEdit.setSizePolicy(sizePolicy)
        self.conversionlineEdit.setObjectName("conversionlineEdit")
        self.gridLayout_2.addWidget(self.conversionlineEdit, 0, 1, 1, 1)
        self.conversionlabel = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversionlabel.sizePolicy().hasHeightForWidth())
        self.conversionlabel.setSizePolicy(sizePolicy)
        self.conversionlabel.setObjectName("conversionlabel")
        self.gridLayout_2.addWidget(self.conversionlabel, 0, 0, 1, 1)
        self.conversiontextEdit = QtWidgets.QTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversiontextEdit.sizePolicy().hasHeightForWidth())
        self.conversiontextEdit.setSizePolicy(sizePolicy)
        self.conversiontextEdit.setObjectName("conversiontextEdit")
        self.gridLayout_2.addWidget(self.conversiontextEdit, 1, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.compilelabel = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compilelabel.sizePolicy().hasHeightForWidth())
        self.compilelabel.setSizePolicy(sizePolicy)
        self.compilelabel.setObjectName("compilelabel")
        self.gridLayout_3.addWidget(self.compilelabel, 0, 0, 1, 1)
        self.compilertextEdit = QtWidgets.QTextEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compilertextEdit.sizePolicy().hasHeightForWidth())
        self.compilertextEdit.setSizePolicy(sizePolicy)
        self.compilertextEdit.setObjectName("compilertextEdit")
        self.gridLayout_3.addWidget(self.compilertextEdit, 1, 1, 1, 1)
        self.compilelineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compilelineEdit.sizePolicy().hasHeightForWidth())
        self.compilelineEdit.setSizePolicy(sizePolicy)
        self.compilelineEdit.setObjectName("compilelineEdit")
        self.gridLayout_3.addWidget(self.compilelineEdit, 0, 1, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_3)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.estimationlineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estimationlineEdit.sizePolicy().hasHeightForWidth())
        self.estimationlineEdit.setSizePolicy(sizePolicy)
        self.estimationlineEdit.setObjectName("estimationlineEdit")
        self.gridLayout_4.addWidget(self.estimationlineEdit, 0, 1, 1, 1)
        self.executelabel = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.executelabel.sizePolicy().hasHeightForWidth())
        self.executelabel.setSizePolicy(sizePolicy)
        self.executelabel.setObjectName("executelabel")
        self.gridLayout_4.addWidget(self.executelabel, 0, 0, 1, 1)
        self.estimationtextEdit = QtWidgets.QTextEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estimationtextEdit.sizePolicy().hasHeightForWidth())
        self.estimationtextEdit.setSizePolicy(sizePolicy)
        self.estimationtextEdit.setObjectName("estimationtextEdit")
        self.gridLayout_4.addWidget(self.estimationtextEdit, 1, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.analysistextEdit = QtWidgets.QTextEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysistextEdit.sizePolicy().hasHeightForWidth())
        self.analysistextEdit.setSizePolicy(sizePolicy)
        self.analysistextEdit.setObjectName("analysistextEdit")
        self.gridLayout_5.addWidget(self.analysistextEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.analysislineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysislineEdit.sizePolicy().hasHeightForWidth())
        self.analysislineEdit.setSizePolicy(sizePolicy)
        self.analysislineEdit.setObjectName("analysislineEdit")
        self.gridLayout_5.addWidget(self.analysislineEdit, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_5)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.profilinglabel = QtWidgets.QLabel(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profilinglabel.sizePolicy().hasHeightForWidth())
        self.profilinglabel.setSizePolicy(sizePolicy)
        self.profilinglabel.setObjectName("profilinglabel")
        self.gridLayout_6.addWidget(self.profilinglabel, 0, 0, 1, 1)
        self.profiletextEdit = QtWidgets.QTextEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profiletextEdit.sizePolicy().hasHeightForWidth())
        self.profiletextEdit.setSizePolicy(sizePolicy)
        self.profiletextEdit.setObjectName("profiletextEdit")
        self.gridLayout_6.addWidget(self.profiletextEdit, 1, 1, 1, 1)
        self.profilinglineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profilinglineEdit.sizePolicy().hasHeightForWidth())
        self.profilinglineEdit.setSizePolicy(sizePolicy)
        self.profilinglineEdit.setObjectName("profilinglineEdit")
        self.gridLayout_6.addWidget(self.profilinglineEdit, 0, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_6)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.exeperflineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exeperflineEdit.sizePolicy().hasHeightForWidth())
        self.exeperflineEdit.setSizePolicy(sizePolicy)
        self.exeperflineEdit.setObjectName("exeperflineEdit")
        self.gridLayout_8.addWidget(self.exeperflineEdit, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 6, 0, 1, 1)
        self.snrlineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snrlineEdit.sizePolicy().hasHeightForWidth())
        self.snrlineEdit.setSizePolicy(sizePolicy)
        self.snrlineEdit.setObjectName("snrlineEdit")
        self.gridLayout_8.addWidget(self.snrlineEdit, 5, 1, 1, 1)
        self.enntestlineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enntestlineEdit.sizePolicy().hasHeightForWidth())
        self.enntestlineEdit.setSizePolicy(sizePolicy)
        self.enntestlineEdit.setObjectName("enntestlineEdit")
        self.gridLayout_8.addWidget(self.enntestlineEdit, 1, 1, 1, 1)
        self.enntesttextEdit = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enntesttextEdit.sizePolicy().hasHeightForWidth())
        self.enntesttextEdit.setSizePolicy(sizePolicy)
        self.enntesttextEdit.setObjectName("enntesttextEdit")
        self.gridLayout_8.addWidget(self.enntesttextEdit, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 5, 0, 1, 1)
        self.memorytextEdit = QtWidgets.QTextEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memorytextEdit.sizePolicy().hasHeightForWidth())
        self.memorytextEdit.setSizePolicy(sizePolicy)
        self.memorytextEdit.setMaximumSize(QtCore.QSize(170, 60))
        self.memorytextEdit.setObjectName("memorytextEdit")
        self.gridLayout_8.addWidget(self.memorytextEdit, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 7, 0, 1, 1)
        self.exetimelineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exetimelineEdit.sizePolicy().hasHeightForWidth())
        self.exetimelineEdit.setSizePolicy(sizePolicy)
        self.exetimelineEdit.setObjectName("exetimelineEdit")
        self.gridLayout_8.addWidget(self.exetimelineEdit, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_8)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 2, 0, 1, 1)
        self.iterlineEdit = QtWidgets.QLineEdit(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iterlineEdit.sizePolicy().hasHeightForWidth())
        self.iterlineEdit.setSizePolicy(sizePolicy)
        self.iterlineEdit.setObjectName("iterlineEdit")
        self.gridLayout_8.addWidget(self.iterlineEdit, 2, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_8)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.scenario_checkBox.setText(_translate("Form", "CheckBox"))
        self.logonoffcheckBox.setText(_translate("Form", "Log On/ Off"))
        self.src_label.setText(_translate("Form", "Repo."))
        self.label_6.setText(_translate("Form", "License"))
        self.questioin_groupBox.setTitle(_translate("Form", "Target Model Path"))
        self.contexts_groupBox.setTitle(_translate("Form", "Set Parameter:"))
        self.groupBox_10.setTitle(_translate("Form", "Memory Profile"))
        self.groupBox_2.setTitle(_translate("Form", "Measurement Items"))
        self.label.setText(_translate("Form", "     Elapsed Time      "))
        self.groupBox_9.setTitle(_translate("Form", "ONNX Info."))
        self.label_3.setText(_translate("Form", "Model Precision"))
        self.direct_shape_label.setText(_translate("Form", "Direct Shape"))
        self.label_2.setText(_translate("Form", "Model Check"))
        self.onnxlabel.setText(_translate("Form", "Opset Version "))
        self.label_5.setText(_translate("Form", "Runtime Inference Check"))
        self.label_4.setText(_translate("Form", "Domain"))
        self.simplifier_label.setText(_translate("Form", "Execute Simplifier"))
        self.groupBox.setTitle(_translate("Form", "enntools init"))
        self.initlabel.setText(_translate("Form", "Result"))
        self.groupBox_3.setTitle(_translate("Form", "enntools conversion"))
        self.conversionlabel.setText(_translate("Form", "Result"))
        self.groupBox_4.setTitle(_translate("Form", "enntools compile"))
        self.compilelabel.setText(_translate("Form", "Result"))
        self.groupBox_5.setTitle(_translate("Form", "enntools estimation"))
        self.executelabel.setText(_translate("Form", "Result"))
        self.groupBox_6.setTitle(_translate("Form", "enntools analysis"))
        self.label_7.setText(_translate("Form", "Result"))
        self.groupBox_7.setTitle(_translate("Form", "enntools profile"))
        self.profilinglabel.setText(_translate("Form", "Result"))
        self.groupBox_8.setTitle(_translate("Form", "NNC profile(enntester)"))
        self.label_8.setText(_translate("Form", "Result"))
        self.label_11.setText(_translate("Form", "Execution Time[ms]"))
        self.label_10.setText(_translate("Form", "SNR"))
        self.label_12.setText(_translate("Form", "Execution Performance"))
        self.label_9.setText(_translate("Form", "Memory Usage[MB]"))
        self.label_13.setText(_translate("Form", "Iterations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
