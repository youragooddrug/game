''' Окно для карточки вопроса '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from PyQt5.QtWidgets import QApplication 



app = QApplication([]) 

# виджеты, которые надо будет разместить:
btn_Menu = QLabel('Правильные ответы:') 
btn_correct = QLabel('') # выводит на экран полсчет правильных ответов
btn_Sleep = QPushButton('Отдохнуть') # кнопка убирает окно и возвращает его после окончания таймера
box_Minutes = QSpinBox() # ввод количества минут
box_Minutes.setValue(30)
btn_OK = QPushButton('Oтветить') # кнопка ответа
btn_OK.setStyleSheet("background-color: #D5D268; color:red; font-family:'Consolas'; font-size:15px;") 
lb_Question = QLabel('') # текст вопроса

# Панель с вариантами:
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
RadioGroup = QButtonGroup() # а это для группировки переключателей, чтобы управлять их поведением

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Панель с результатом:
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('') # здесь будет написан текст правильного ответа

#  Теперь занимаемся размещением:

# Размещаем варианты ответов в два столбца внутри группы:
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов    
# размещаем результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# размещаем все виджеты в окне, они расположены в четыре строки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(btn_correct)
layout_line1.addStretch(1) # разрыв между кнопками делаем по возможности длиннее
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('минут')) # нам не нужна переменная для этой надписи

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line4.addStretch(1)

# Теперь созданные 4 строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

# Результат работы этого модуля: виджеты помещены внутрь layout_card, который можно назначить окну.

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    # сбросить выбранную радио-кнопку
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
    
    
    
    
    
    
 