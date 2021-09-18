from qt_core import *

class ButtonController(QWidget):
    def __init__(self):
        super().__init__()
        self.app = QWidget()
        self.button_1 = QPushButton(self.app)
        self.button_2 = QPushButton(self.app)
        self.button_3 = QPushButton(self.app)
        self.button_4 = QPushButton(self.app)
        self.button_5 = QPushButton(self.app)
        self.button_6 = QPushButton(self.app)
        self.button_7 = QPushButton(self.app)

        self.serial = QtSerialPort.QSerialPort(
            '/dev/ttyUSB0',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receiveButton)
#         try:
#     ser = serial.Serial('/dev/ttyUSB0',9600)
# except:
#     try:
#         ser = serial.Serial('/dev/ttyUSB1',9600)
#     except:
#         pass

        if not self.serial.isOpen():
            self.serial.open(QIODevice.ReadWrite)  

    def receiveButton(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            try:
                print(text)
                number = int(text)
                if number == 1:
                    self.button_1.clicked.emit()
                elif number == 2:
                    self.button_2.clicked.emit()
                elif number == 3:
                    self.button_3.clicked.emit()
                elif number == 4:
                    self.button_4.clicked.emit()
                elif number == 5:
                    self.button_5.clicked.emit()
                elif number == 6:
                    self.button_6.clicked.emit()
                elif number == 7:
                    self.button_7.clicked.emit()
            except:
                pass

    

    

# class KeyPress(QWidget):
#     def __init__():
#         super().__init__()

    

