from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    tmp = Question(question["text"], question["answer"])
    question_bank.append(tmp)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
    quiz.next_question()

print("That's the end of the quiz.")
print(f"Your final score is {quiz.score} / {len(quiz.question_list)}")