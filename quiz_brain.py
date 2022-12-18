class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        currentItem = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {currentItem.text} (True/False): ")
        self.check_answer(answer, currentItem.answer)
        
    def check_answer(self, answer, correct_answer):
        