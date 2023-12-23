from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint
app = QApplication([]) # збереження додатка

window = QWidget()
window.resize(250,250) # розміри
window.move(250,250) # розміщення в коодинатах

button = QPushButton('кнопка') # віджет кнопка

text1 = QLabel('натисни') #текстовий віджет

text2 = QLabel('?')

v = QVBoxLayout() # Вертикальний лайаут
v.addWidget(text1, alignment=Qt.AlignCenter)
v.addWidget(text2, alignment=Qt.AlignCenter)
v.addWidget(button, alignment=Qt.AlignCenter)

def random_number():
    n = randint(1,101)
    text2.setText(str(n))

button.clicked.connect(random_number)

button.setStyleSheet ("""
    background-color: violet;
    border-radius: 10px;
    font-size: 10px;
    border-color: black;
    padding: 10px 20px;
""")
window.setStyleSheet ("""
    background-color: yellow;
    border-radius: 10px;
    font-size: 10px;
    border-color: black;
    padding: 10px 20px;
""")

window.setLayout(v)

window.show()

app.exec_()
