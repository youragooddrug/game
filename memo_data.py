
class Form():
    ''' хранит информацию про одну анкетку'''
    def __init__(self, question, answer, 
                       wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question # вопрос
        self.answer = answer # правильный ответ
        self.wrong_answer1 = wrong_answer1 # считаем, что всегда пишется три неверных варианта
        self.wrong_answer2 = wrong_answer2 # 
        self.wrong_answer3 = wrong_answer3 #
        self.is_active = True # продолжать ли задавать этот вопрос?
        self.attempts = 0 # сколько раз этот вопрос задавался
        self.correct = 0 # количество верных ответов
    def got_right(self):
        ''' меняет статистику, получив правильный ответ'''
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        ''' меняет статистику, получив неверный ответ'''
        self.attempts += 1


