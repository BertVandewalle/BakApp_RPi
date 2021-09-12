from qt_core import *
from button_controller import ButtonController

def keyPressEventHandler(btc:ButtonController,event):
    print(f"key pressed {event.key()}")
    if event.key() == Qt.Key_4: btc.button_1.clicked.emit()
    elif event.key() == Qt.Key_1: btc.button_2.clicked.emit()
    elif event.key() == Qt.Key_3: btc.button_3.clicked.emit()
    elif event.key() == Qt.Key_6: btc.button_4.clicked.emit()
    elif event.key() == Qt.Key_7: btc.button_5.clicked.emit()
    elif event.key() == Qt.Key_8: btc.button_6.clicked.emit()
    elif event.key() == Qt.Key_9: 
        btc.button_7.clicked.emit()
        print("button 7 clicked") 