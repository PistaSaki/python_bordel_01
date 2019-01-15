import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class Example(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        grid = qtw.QGridLayout()
        
        
        self.label = qtw.QLabel("Nothing yet.", self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        self.setMouseTracking(True)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
    def mouseMoveEvent(self, e):
        
        x = e.x()
        y = e.y()
        
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())