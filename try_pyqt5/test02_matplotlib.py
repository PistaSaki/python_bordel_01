import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import pyqtSignal


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
 
import random


class Example(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        
        
        self.label = qtw.QLabel("Nothing yet.", self)
        main_layout.addWidget(self.label)
        
        self.canvas = PlotCanvas(parent = self)
        main_layout.addWidget(self.canvas)
        self.canvas.mouse_moved_signal.connect(self.update_label)
        
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
    def update_label(self, x, y):
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)
    
        
class PlotCanvas(FigureCanvas):
    mouse_moved_signal = pyqtSignal([int, int])
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        self.setSizePolicy(
                qtw.QSizePolicy.Expanding,
                qtw.QSizePolicy.Expanding)
        self.updateGeometry()
        self.plot()
        
        self.setMouseTracking(True)
        
 
 
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
        
    def mouseMoveEvent(self, e):
        
        x = e.x()
        y = e.y()
        
        self.mouse_moved_signal.emit(x, y)
        #text = "x: {0},  y: {1}".format(x, y)
        #self.label.setText(text)
        #print(text)
 

        
if __name__ == '__main__':
    
    app = qtw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
