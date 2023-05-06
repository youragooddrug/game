from memo_card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Result,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_result, show_question, btn_Menu, btn_correct
)
from PyQt5.QtWidgets import QWidget
from random import shuffle, randint # будем перемешивать ответы в карточке вопроса
from random import shuffle, randint
from memo_data import Form

card_width, card_height = 600, 500 # начальные размеры окна "карточка"
text_wrong = 'Неверно'
text_correct = 'Верно'

# в этой версии напишем в коде один вопрос и ответы к нему 
# соответствующие переменные как бы поля будущего объекта "form" (т.е. анкета) 
# frm_question = 'Яблоко'
# frm_right = 'apple'
# frm_wrong1 = 'application'
# frm_wrong2 = 'building'
# frm_wrong3 = 'caterpillar'


# Теперь нам нужно показать эти данные,
# причем ответы распределить случайно между радиокнопками, и помнить кнопку с правильным ответом.
# Для этого создадим набор ссылок на радиокнопки и перемешаем его 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]






questions = []

frm = Form('Яблоко', 'apple', 'application', 'pinapple', 'apply')
questions.append(frm)
frm = Form('Дом', 'house', 'horse', 'hurry', 'hour')
questions.append(frm)
frm = Form('Мышь', 'mouse', 'mouth', 'muse', 'museum')
questions.append(frm)
frm = Form('Число', 'number', 'digit', 'amount', 'summary')
questions.append(frm)




def show_data(frm: Form):
    ''' показывает на экране нужную информацию '''
    # объединим в функцию похожие действия
    lb_Question.setText(frm.question)
    lb_Correct.setText(frm.answer)
    radio_list[0].setText(frm.answer)
    radio_list[1].setText(frm.wrong_answer1)
    radio_list[2].setText(frm.wrong_answer2)
    radio_list[3].setText(frm.wrong_answer3)
    show_question()



        

def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    correct = radio_list[0].isChecked() # в этом радиобаттоне лежит наш ответик!
    if correct:
        # ответ верный, запишем 
        lb_Result.setText(text_correct) # надпись "верно" или "неверно"
        frm.got_right()
        show_result()
    else:
        incorrect = radio_list[1].isChecked() or radio_list[2].isChecked() or radio_list[3].isChecked()
        if incorrect:
            # ответ неверный, запишем и отразим в статистике
            lb_Result.setText(text_wrong) # надпись "верно" или "неверно"
            frm.got_wrong()
            show_result()
    print("Всего задано вопросов:", frm.attempts, "Всего правильных ответов:", frm.correct)
    btn_correct.setText(str(frm.correct))


def next_question():
    global cur_question
    cur_question += 1
    if cur_question >= len(questions):
        cur_question = 0
    frm = questions[cur_question]
    show_data(frm)






def click_OK(self):
    # пока что проверяем вопрос, если мы в режиме вопроса, иначе ничего
    if btn_OK.text() == 'Ответить':
        check_result()
    else:
        next_question()
    
    
    

cur_question = -1
     

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)

show_data(frm)
show_question()
btn_OK.clicked.connect(click_OK)
win_card.show()
app.exec_()