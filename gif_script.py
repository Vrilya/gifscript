from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class BaseWidget(QtWidgets.QWidget):
    def __init__(self, always_on_top):
        super().__init__()

        window_flags = QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTransparentForInput | QtCore.Qt.Tool
        if always_on_top:
            window_flags |= QtCore.Qt.WindowStaysOnTopHint

        self.setWindowFlags(window_flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_Disabled)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            self.showNormal()

        super().changeEvent(event)

class TransparentGif(BaseWidget):
    def __init__(self, always_on_top):
        super().__init__(always_on_top)

        self.movie = QtGui.QMovie("/home/animelover/gifscript/giphy1.gif")
        self.label = QtWidgets.QLabel(self)
        self.label.setMovie(self.movie)

        self.movie.start()

        self.desktop = QtWidgets.QApplication.desktop()
        self.resize(498, 280)
        self.move(self.desktop.width() - self.width(), self.desktop.height() - self.height())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkPosition)
        self.timer.start(1000)

    def checkPosition(self):
        desired_position = QtCore.QPoint(self.desktop.width() - self.width(), self.desktop.height() - self.height())
        current_position = self.pos()
        
        if current_position != desired_position:
            self.move(desired_position)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    always_on_top = 0  # \C4ndra detta v\E4rde till 0 f\F6r att ha widgeten alltid i bakgrunden, eller 1 f\F6r att ha den alltid ovanp\E5
    gif = TransparentGif(always_on_top)
    gif.show()
    sys.exit(app.exec_())

