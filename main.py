from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    tmp = Question(question["text"], question["answer"])
    question_bank.append(tmp)
    
quiz = QuizBrain(question_bank)
quiz.next_question()