import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from menu import Ui_Menu
from gui import Ui_Solver
import test

class main(QDialog,Ui_Menu):
    def __init__(self,parent=None):
        super(main,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("Sudoku-Solver-android-thumb"))
        self.setWindowTitle("Soduko Solver")
        self.solve=solver(self)
        self.solve_btn.clicked.connect(self.opensolver)
    def opensolver(self):
        self.close()
        self.solve.show()
global Yes
Yes=QMessageBox.Yes


class solver(QDialog,Ui_Solver):
    def __init__(self,parent=None):
        super(solver,self).__init__(parent)
        self.setupUi(self)
        self.new_btn.clicked.connect(self.load)
        self.solve_btn.clicked.connect(self.solveclick)
        self.reset_btn.clicked.connect(self.tableWidget.clear)
        self.cancel_btn.clicked.connect(self.closew)
    def closew(self):
        msg = QMessageBox()
        msg.setWindowTitle("Status Window")
        msg.setIcon(QMessageBox.Information)
        msg.setText('Are you sure you wanna exit?')
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        a=msg.exec_()
        if a==Yes:
            sys.exit()
        else:
            pass

    def load(self):
        grid=test.load1()
        print(grid)
        for i in range(9):
            for j in range(9):
                item = QTableWidgetItem(str(grid[i][j]))
                self.tableWidget.setItem(i, j, item)

    def solveclick(self):
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                item = self.tableWidget.item(i, j)
                if item == None:
                    item = '0'
                else:
                    item = item.text()
                if item not in list('123456789'):
                    item = '0'
                row.append(int(item))
            puzzle.append(row[:])
        soln = test.solve(puzzle)
        print(soln)
        if -1 in soln:
            print(1)
            msg=QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Sudoku can`t be solved")
            msg.setStandardButtons(QMessageBox.Ok)
            a=msg.exec_()
            if(a == QMessageBox.Ok):
                pass
        else:
            self.showSolution(soln)
        

    def showSolution(self, soln):
        for i in range(9):
            for j in range(9):
                item = QTableWidgetItem(str(soln[i][j]))
                self.tableWidget.setItem(i, j, item)
    


if __name__== '__main__':
    global app
    app=QApplication(sys.argv)
    form=main()
    form.show()
    sys.exit(app.exec_())
