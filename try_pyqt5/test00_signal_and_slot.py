import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt

class Example(qtw.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        lcd = qtw.QLCDNumber(self)
        sld = qtw.QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(lcd.display)
        

        vbox = qtw.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        wid = qtw.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(vbox)
        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()
        



if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())