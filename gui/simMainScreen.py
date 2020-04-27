import time

from PyQt5 import QtCore, QtGui, QtWidgets

from common.types import BitString
from engine.hardware.components import InstructionMemory, Memory, Registers
from engine.software.mipsAssembler import MIPSAssembler
from gui.codeEditor import CodeEditor
from simProcessor import Processor


class Ui_simMainWindow(object):
    def setupUi(self, simMainWindow):
        simMainWindow.setObjectName("simMainWindow")
        simMainWindow.resize(1401, 906)

        self.centralwidget = QtWidgets.QWidget(simMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.assemblyEditor = CodeEditor(self.centralwidget)
        self.assemblyEditor.setGeometry(QtCore.QRect(30, 40, 331, 541))
        self.assemblyEditor.setObjectName("assemblyEditor")

        self.machineCodeViewer = CodeEditor(self.centralwidget)
        self.machineCodeViewer.setGeometry(QtCore.QRect(380, 40, 271, 541))
        self.machineCodeViewer.setObjectName("machineCodeViewer")

        self.registersTableWidget_1 = QtWidgets.QTableWidget(
            self.centralwidget)
        self.registersTableWidget_1.setGeometry(
            QtCore.QRect(710, 40, 321, 540))
        self.registersTableWidget_1.setWordWrap(True)
        self.registersTableWidget_1.setObjectName("registersTableWidget_1")
        self.registersTableWidget_1.setColumnCount(3)
        self.registersTableWidget_1.setRowCount(17)

        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_1.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.registersTableWidget_1.horizontalHeader().setDefaultSectionSize(90)
        self.registersTableWidget_1.horizontalHeader().setMinimumSectionSize(90)
        self.registersTableWidget_1.horizontalHeader().setStretchLastSection(True)
        self.registersTableWidget_1.verticalHeader().setCascadingSectionResizes(False)
        self.registersTableWidget_1.verticalHeader().setDefaultSectionSize(30)
        self.registersTableWidget_1.verticalHeader().setMinimumSectionSize(25)
        self.registersTableWidget_1.verticalHeader().setStretchLastSection(True)
        self.registersTableWidget_1.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.registersTableWidget_2 = QtWidgets.QTableWidget(
            self.centralwidget)
        self.registersTableWidget_2.setGeometry(
            QtCore.QRect(1050, 40, 321, 540))
        self.registersTableWidget_2.setWordWrap(True)
        self.registersTableWidget_2.setObjectName("registersTableWidget_2")
        self.registersTableWidget_2.setColumnCount(3)
        self.registersTableWidget_2.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.registersTableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.registersTableWidget_2.setHorizontalHeaderItem(2, item)
        self.registersTableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.registersTableWidget_2.horizontalHeader().setMinimumSectionSize(90)
        self.registersTableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.registersTableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.registersTableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.registersTableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.registersTableWidget_2.verticalHeader().setStretchLastSection(True)
        self.registersTableWidget_2.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.runButton = QtWidgets.QToolButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(30, 10, 25, 25))
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./gui/icons/run_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setObjectName("runButton")

        self.editorButtonGroup = QtWidgets.QButtonGroup(simMainWindow)
        self.editorButtonGroup.setObjectName("editorButtonGroup")
        self.editorButtonGroup.addButton(self.runButton)

        self.memoryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.memoryTableWidget.setGeometry(QtCore.QRect(30, 610, 1341, 113))
        self.memoryTableWidget.setObjectName("memoryTableWidget")
        self.memoryTableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.memoryTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.memoryTableWidget.setVerticalHeaderItem(1, item)
        self.memoryTableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.memoryTableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.memoryTableWidget.verticalHeader().setDefaultSectionSize(31)
        self.memoryTableWidget.verticalHeader().setMinimumSectionSize(31)
        self.memoryTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.stackTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.stackTableWidget.setGeometry(QtCore.QRect(30, 750, 1341, 113))
        self.stackTableWidget.setObjectName("stackTableWidget")
        self.stackTableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.stackTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stackTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stackTableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.stackTableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.stackTableWidget.verticalHeader().setDefaultSectionSize(31)
        self.stackTableWidget.verticalHeader().setMinimumSectionSize(31)
        self.stackTableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.machineCodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.machineCodeLabel.setGeometry(QtCore.QRect(380, 10, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.machineCodeLabel.setFont(font)
        self.machineCodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.machineCodeLabel.setObjectName("machineCodeLabel")

        self.stopButton = QtWidgets.QToolButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(150, 10, 25, 25))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./gui/icons/stop_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.editorButtonGroup.addButton(self.stopButton)

        self.pauseButton = QtWidgets.QToolButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(110, 10, 25, 25))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./gui/icons/pause_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setIconSize(QtCore.QSize(30, 30))
        self.pauseButton.setObjectName("pauseButton")
        self.editorButtonGroup.addButton(self.pauseButton)

        self.previousButton = QtWidgets.QToolButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(190, 10, 25, 25))
        self.previousButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./gui/icons/prev_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon3)
        self.previousButton.setIconSize(QtCore.QSize(30, 30))
        self.previousButton.setObjectName("previousButton")
        self.editorButtonGroup.addButton(self.previousButton)

        self.nextButton = QtWidgets.QToolButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(230, 10, 25, 25))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./gui/icons/next_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setIconSize(QtCore.QSize(30, 30))
        self.nextButton.setObjectName("nextButton")
        self.editorButtonGroup.addButton(self.nextButton)

        self.debugButton = QtWidgets.QToolButton(self.centralwidget)
        self.debugButton.setGeometry(QtCore.QRect(70, 10, 25, 25))
        self.debugButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.debugButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./gui/icons/debug_icon.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.debugButton.setIcon(icon5)
        self.debugButton.setIconSize(QtCore.QSize(30, 30))
        self.debugButton.setObjectName("debugButton")

        self.delayLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.delayLineEdit.setGeometry(QtCore.QRect(320, 10, 41, 22))
        self.delayLineEdit.setObjectName("delayLineEdit")
        self.delayLineEdit.setPlaceholderText("1.0")
        self.delayLineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.delayLabel = QtWidgets.QLabel(self.centralwidget)
        self.delayLabel.setGeometry(QtCore.QRect(270, 10, 51, 20))
        self.delayLabel.setObjectName("delayLabel")

        self.memoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.memoryLabel.setGeometry(QtCore.QRect(30, 590, 61, 20))
        self.memoryLabel.setObjectName("memoryLabel")

        self.registersLabel = QtWidgets.QLabel(self.centralwidget)
        self.registersLabel.setGeometry(QtCore.QRect(714, 10, 651, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registersLabel.setFont(font)
        self.registersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registersLabel.setObjectName("registersLabel")

        self.stackLabel = QtWidgets.QLabel(self.centralwidget)
        self.stackLabel.setGeometry(QtCore.QRect(30, 730, 55, 16))
        self.stackLabel.setObjectName("stackLabel")
        simMainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(simMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1401, 26))
        self.menuBar.setObjectName("menuBar")

        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        simMainWindow.setMenuBar(self.menuBar)
        self.actionOpen_File = QtWidgets.QAction(simMainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menufile.addAction(self.actionOpen_File)
        self.menuBar.addAction(self.menufile.menuAction())

        self.retranslateUi(simMainWindow)
        QtCore.QMetaObject.connectSlotsByName(simMainWindow)

    def retranslateUi(self, simMainWindow):
        _translate = QtCore.QCoreApplication.translate
        simMainWindow.setWindowTitle(
            _translate("simMainWindow", "MIPS Simulator"))
        item = self.registersTableWidget_1.verticalHeaderItem(0)
        item.setText(_translate("simMainWindow", "zero"))
        item = self.registersTableWidget_1.verticalHeaderItem(1)
        item.setText(_translate("simMainWindow", "at"))
        item = self.registersTableWidget_1.verticalHeaderItem(2)
        item.setText(_translate("simMainWindow", "v0"))
        item = self.registersTableWidget_1.verticalHeaderItem(3)
        item.setText(_translate("simMainWindow", "v1"))
        item = self.registersTableWidget_1.verticalHeaderItem(4)
        item.setText(_translate("simMainWindow", "a0"))
        item = self.registersTableWidget_1.verticalHeaderItem(5)
        item.setText(_translate("simMainWindow", "a1"))
        item = self.registersTableWidget_1.verticalHeaderItem(6)
        item.setText(_translate("simMainWindow", "a2"))
        item = self.registersTableWidget_1.verticalHeaderItem(7)
        item.setText(_translate("simMainWindow", "a3"))
        item = self.registersTableWidget_1.verticalHeaderItem(8)
        item.setText(_translate("simMainWindow", "t0"))
        item = self.registersTableWidget_1.verticalHeaderItem(9)
        item.setText(_translate("simMainWindow", "t1"))
        item = self.registersTableWidget_1.verticalHeaderItem(10)
        item.setText(_translate("simMainWindow", "t2"))
        item = self.registersTableWidget_1.verticalHeaderItem(11)
        item.setText(_translate("simMainWindow", "t3"))
        item = self.registersTableWidget_1.verticalHeaderItem(12)
        item.setText(_translate("simMainWindow", "t4"))
        item = self.registersTableWidget_1.verticalHeaderItem(13)
        item.setText(_translate("simMainWindow", "t5"))
        item = self.registersTableWidget_1.verticalHeaderItem(14)
        item.setText(_translate("simMainWindow", "t6"))
        item = self.registersTableWidget_1.verticalHeaderItem(15)
        item.setText(_translate("simMainWindow", "t7"))
        item = self.registersTableWidget_1.verticalHeaderItem(16)
        item.setText(_translate("simMainWindow", "hi"))
        item = self.registersTableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("simMainWindow", "Hex"))
        item = self.registersTableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("simMainWindow", "Signed dec"))
        item = self.registersTableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("simMainWindow", "Unsigned dec"))
        __sortingEnabled = self.registersTableWidget_1.isSortingEnabled()
        self.registersTableWidget_1.setSortingEnabled(False)
        self.registersTableWidget_1.setSortingEnabled(__sortingEnabled)
        item = self.registersTableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("simMainWindow", "s0"))
        item = self.registersTableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("simMainWindow", "s1"))
        item = self.registersTableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("simMainWindow", "s2"))
        item = self.registersTableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("simMainWindow", "s3"))
        item = self.registersTableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("simMainWindow", "s4"))
        item = self.registersTableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("simMainWindow", "s5"))
        item = self.registersTableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("simMainWindow", "s6"))
        item = self.registersTableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("simMainWindow", "s7"))
        item = self.registersTableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("simMainWindow", "t8"))
        item = self.registersTableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("simMainWindow", "t9"))
        item = self.registersTableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("simMainWindow", "k1"))
        item = self.registersTableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("simMainWindow", "k2"))
        item = self.registersTableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("simMainWindow", "gp"))
        item = self.registersTableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("simMainWindow", "sp"))
        item = self.registersTableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("simMainWindow", "fp"))
        item = self.registersTableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("simMainWindow", "ra"))
        item = self.registersTableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("simMainWindow", "lo"))
        item = self.registersTableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("simMainWindow", "Hex"))
        item = self.registersTableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("simMainWindow", "Signed dec"))
        item = self.registersTableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("simMainWindow", "Unsigned dec"))
        self.runButton.setToolTip(_translate("simMainWindow", "Run"))
        item = self.memoryTableWidget.verticalHeaderItem(0)
        item.setText(_translate("simMainWindow", "Decimal"))
        item = self.memoryTableWidget.verticalHeaderItem(1)
        item.setText(_translate("simMainWindow", "Binary"))
        __sortingEnabled = self.memoryTableWidget.isSortingEnabled()
        self.memoryTableWidget.setSortingEnabled(False)
        self.memoryTableWidget.setSortingEnabled(__sortingEnabled)
        item = self.stackTableWidget.verticalHeaderItem(0)
        item.setText(_translate("simMainWindow", "Decimal"))
        item = self.stackTableWidget.verticalHeaderItem(1)
        item.setText(_translate("simMainWindow", "Binary"))
        item = self.stackTableWidget.horizontalHeaderItem(0)
        __sortingEnabled = self.stackTableWidget.isSortingEnabled()
        self.stackTableWidget.setSortingEnabled(False)
        self.stackTableWidget.setSortingEnabled(__sortingEnabled)
        self.machineCodeLabel.setText(
            _translate("simMainWindow", "Machine Code"))
        self.stopButton.setToolTip(_translate("simMainWindow", "Stop"))
        self.pauseButton.setToolTip(_translate("simMainWindow", "Pause"))
        self.previousButton.setToolTip(_translate("simMainWindow", "Previous"))
        self.nextButton.setToolTip(_translate("simMainWindow", "Next"))
        self.debugButton.setToolTip(_translate("simMainWindow", "Debug"))
        self.delayLabel.setText(_translate("simMainWindow", "Delay(s)"))
        self.memoryLabel.setText(_translate("simMainWindow", " Memory"))
        self.registersLabel.setText(_translate("simMainWindow", "Registers"))
        self.stackLabel.setText(_translate("simMainWindow", " Stack"))
        self.menufile.setTitle(_translate("simMainWindow", "File"))
        self.actionOpen_File.setText(_translate("simMainWindow", "Open File"))


class SimMainScreen(QtWidgets.QMainWindow):

    # STATIC VARIABLES #
    _running = False
    _next = False
    _prev = False
    _backStack = []

    # DUNDERS #
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        ui = Ui_simMainWindow()
        ui.setupUi(self)
        self.initializeObjects()
        self.connectCallbacks()

    # PROPERTIES #

    # PUBLIC METHODS #
    def initializeObjects(self):
        self.assemblyEditor: CodeEditor = self.findChild(
            CodeEditor, "assemblyEditor")
        self.machineCodeViewer: CodeEditor = self.findChild(
            CodeEditor, "machineCodeViewer")

        memory_length = len(Memory._memory)*4
        self.memoryTableWidget: QtWidgets.QTableWidget = self.findChild(
            QtWidgets.QTableView, "memoryTableWidget")
        self.memoryTableWidget.setColumnCount(memory_length)

        self.stackTableWidget: QtWidgets.QTableWidget = self.findChild(
            QtWidgets.QTableView, "stackTableWidget")
        self.stackTableWidget.setColumnCount(memory_length)

        font = QtGui.QFont()
        font.setUnderline(True)
        for address in range(memory_length):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            item.setText("0x" + hex(address)[2:].upper())
            self.memoryTableWidget.setHorizontalHeaderItem(address, item)
            self.stackTableWidget.setHorizontalHeaderItem(
                memory_length - address - 1, item)
            self._updateMemoryCell(address)

        self.registersTableWidget_1: QtWidgets.QTableWidget = self.findChild(
            QtWidgets.QTableWidget, "registersTableWidget_1")
        self.registersTableWidget_2: QtWidgets.QTableWidget = self.findChild(
            QtWidgets.QTableWidget, "registersTableWidget_2")

        for reg_idx in range(34):
            self._updateRegister(reg_idx)

        self.delayLineEdit: QtWidgets.QLineEdit = self.findChild(
            QtWidgets.QLineEdit, "delayLineEdit")

    def connectCallbacks(self):
        self.assemblyEditor.textChanged.connect(
            self._assemblyEditor_textChanged)

        self.runButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "runButton")
        self.runButton.clicked.connect(self._runButton_clicked)

        self.debugButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "debugButton")
        self.debugButton.clicked.connect(self._debugButton_clicked)

        self.pauseButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "pauseButton")
        self.pauseButton.clicked.connect(self._pauseButton_clicked)
        self.pauseButton.setDisabled(True)

        self.stopButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "stopButton")
        self.stopButton.clicked.connect(self._stopButton_clicked)
        self.stopButton.setDisabled(True)

        self.previousButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "previousButton")
        self.previousButton.clicked.connect(self._previousButton_clicked)
        self.previousButton.setDisabled(True)

        self.nextButton: QtWidgets.QToolButton = self.findChild(
            QtWidgets.QToolButton, "nextButton")
        self.nextButton.clicked.connect(self._nextButton_clicked)
        self.nextButton.setDisabled(True)

        self.actionOpen_File: QtWidgets.QAction = self.findChild(
            QtWidgets.QAction, "actionOpen_File")
        self.actionOpen_File.triggered.connect(self._actionOpen_File_triggered)

    # PRIVATE METHODS #
    def _actionOpen_File_triggered(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName", "",
            "All Files (*);;Assembly Files (*.s)")
        if fname:
            with open(fname, 'r') as f:
                self.assemblyEditor.setPlainText(f.read())

    def _runButton_clicked(self):
        self._resetDebugger()
        self.pauseButton.setDisabled(False)
        self.stopButton.setDisabled(False)

        assembl_text = self.assemblyEditor.toPlainText()
        try:
            delay = float(self.delayLineEdit.text())
        except:
            delay = 1.0

        try:
            InstructionMemory.load_instructions(
                MIPSAssembler.assembly(assembl_text))
        except Exception as e:
            QtWidgets.QErrorMessage(self).showMessage(str(e))

        self._running = True
        step = Processor.processNext()
        while step is not None and self._running:
            for _ in range(300):
                time.sleep(delay/300)
                QtWidgets.QApplication.processEvents()
            changed_regs, changed_mems = step
            for changed_reg in changed_regs:
                self._updateRegister(changed_reg)
            for changed_mem in changed_mems:
                self._updateMemoryCell(changed_mem)
            step = Processor.processNext()
        else:
            QtWidgets.QErrorMessage(self).showMessage("Done")

        self._running = False
        self.pauseButton.setDisabled(True)
        self.stopButton.setDisabled(True)

    def _debugButton_clicked(self):
        self._resetDebugger()
        self.stopButton.setDisabled(False)
        self.previousButton.setDisabled(False)
        self.nextButton.setDisabled(False)

        assembl_text = self.assemblyEditor.toPlainText()
        cursor: QtGui.QTextCursor = self.machineCodeViewer.textCursor()

        try:
            InstructionMemory.load_instructions(
                MIPSAssembler.assembly(assembl_text))
        except Exception as e:
            QtWidgets.QErrorMessage(self).showMessage(str(e))

        self._running = True
        old_pc = 0
        cursor.setPosition(0)
        self.machineCodeViewer.setTextCursor(cursor)
        step = Processor.processNext()
        while step is not None and self._running:
            time.sleep(0.001)
            QtWidgets.QApplication.processEvents()
            if self._next:
                self._next = False
                self._backStack.append((old_pc, InstructionMemory.PC, step))
                if InstructionMemory.PC-old_pc > 0:
                    cursor.movePosition(QtGui.QTextCursor.Down,
                                        n=(InstructionMemory.PC-old_pc)//4)
                elif InstructionMemory.PC-old_pc < 0:
                    cursor.movePosition(QtGui.QTextCursor.Up,
                                        n=abs(InstructionMemory.PC-old_pc)//4)
                self.machineCodeViewer.setTextCursor(cursor)
                changed_regs, changed_mems = step
                for changed_reg in changed_regs:
                    self._updateRegister(changed_reg[0])
                for changed_mem in changed_mems:
                    self._updateMemoryCell(changed_mem[0])
                old_pc = InstructionMemory.PC
                step = Processor.processNext()

            if self._prev:
                self._prev = False
                try:
                    prev_old_pc, prev_pc, prev_vals = self._backStack.pop()
                except IndexError as e:
                    continue
                if InstructionMemory.PC-prev_pc < 0:
                    cursor.movePosition(QtGui.QTextCursor.Down,
                                        n=abs(InstructionMemory.PC-prev_pc)//4)
                elif InstructionMemory.PC-prev_pc > 0:
                    cursor.movePosition(QtGui.QTextCursor.Up,
                                        n=(InstructionMemory.PC-prev_pc)//4)
                self.machineCodeViewer.setTextCursor(cursor)

                InstructionMemory.PC = prev_pc
                old_pc = prev_old_pc
                regs, mems = prev_vals
                for reg_idx, reg_val in regs:
                    self._reverseRegister(reg_idx, reg_val)
                for mem_adr, mem_val in mems:
                    self._reverseMemory(mem_adr, mem_val)

        else:
            QtWidgets.QErrorMessage(self).showMessage("Done")

        self._running = False
        self.stopButton.setDisabled(True)
        self.previousButton.setDisabled(True)
        self.nextButton.setDisabled(True)

    def _pauseButton_clicked(self):
        self._running = False

    def _stopButton_clicked(self):
        self._running = False

    def _previousButton_clicked(self):
        self._prev = True

    def _nextButton_clicked(self):
        self._next = True

    def _assemblyEditor_textChanged(self):
        assembly_lines = self.assemblyEditor.toPlainText()
        machineCodeViewer_text = ""
        try:
            for machine_code in MIPSAssembler.assembly(assembly_lines, True):
                machineCodeViewer_text += machine_code + "\n"
        except:
            return
        self.machineCodeViewer.setPlainText(machineCodeViewer_text)

    def _updateMemoryCell(self, adress: int):
        memory_length = len(Memory._memory)*4

        item = QtWidgets.QTableWidgetItem(str(Memory.loadByte(adress)))
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.memoryTableWidget.setItem(0, adress, item)
        item = QtWidgets.QTableWidgetItem(
            str(BitString(Memory.loadByte(adress), length=8)))
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.memoryTableWidget.setItem(1, adress, item)

        item = QtWidgets.QTableWidgetItem(str(Memory.loadByte(adress)))
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.stackTableWidget.setItem(0, memory_length - adress - 1, item)
        item = QtWidgets.QTableWidgetItem(
            str(BitString(Memory.loadByte(adress), length=8)))
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.stackTableWidget.setItem(
            1, memory_length - adress - 1, item)

    def _updateRegister(self, reg_idx: int):
        if reg_idx < 16:
            item = QtWidgets.QTableWidgetItem(str("0x" + hex(
                Registers.getRegister(f"r{reg_idx}").value)[2:].upper()))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 0, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister(f"r{reg_idx}").signedValue))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 1, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister(f"r{reg_idx}").value))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 2, item)

        elif reg_idx == 16:
            item = QtWidgets.QTableWidgetItem(
                str("0x" + hex(Registers.getRegister("hi").value)[2:].upper()))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 0, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister("hi").signedValue))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 1, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister("hi").value))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_1.setItem(reg_idx, 2, item)

        elif reg_idx == 33:
            item = QtWidgets.QTableWidgetItem(
                str("0x" + hex(Registers.getRegister("lo").value)[2:].upper()))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 0, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister("lo").signedValue))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 1, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister("lo").value))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 2, item)

        else:
            item = QtWidgets.QTableWidgetItem(str("0x" + hex(Registers.getRegister(
                f"r{reg_idx-1}").value)[2:].upper()))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 0, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister(f"r{reg_idx-1}").signedValue))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 1, item)
            item = QtWidgets.QTableWidgetItem(
                str(Registers.getRegister(f"r{reg_idx-1}").value))
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.registersTableWidget_2.setItem(reg_idx % 17, 2, item)

    def _reverseMemory(self, address, val):
        Memory.storeByte(address, offset=0, value=val)
        self._updateMemoryCell(address)

    def _reverseRegister(self, reg_idx, val):
        if reg_idx < 16:
            Registers.getRegister(f"r{reg_idx}").setRegisterValue(val)
        elif reg_idx == 16:
            Registers.getRegister("hi").setRegisterValue(val)
        elif reg_idx == 33:
            Registers.getRegister("lo").setRegisterValue(val)
        else:
            Registers.getRegister(f"r{reg_idx-1}").setRegisterValue(val)
        self._updateRegister(reg_idx)

    def _resetDebugger(self):
        self.previousButton.setDisabled(True)
        self.nextButton.setDisabled(True)
        self.stopButton.setDisabled(True)
        self.pauseButton.setDisabled(True)
        Registers.resetRegisters()
        Memory.resetMemory()

        for address in range(4*len(Memory._memory)):
            self._updateMemoryCell(address)
        for idx in range(34):
            self._updateRegister(idx)
