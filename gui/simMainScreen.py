import time

from PyQt5 import QtCore, QtGui, QtWidgets

from common.types import BitString
from engine.hardware.components import InstructionMemory, Memory, Registers
from engine.software.mipsAssembler import MIPSAssembler
from gui.codeEditor import CodeEditor
from gui.simMainScreen_Ui import Ui_simMainWindow
from simProcessor import Processor


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
            QtWidgets.QApplication.processEvents()
            self._updateMemoryCell(address)
        for idx in range(34):
            QtWidgets.QApplication.processEvents()
            self._updateRegister(idx)
