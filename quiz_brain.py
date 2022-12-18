class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        currentItem = self.question_list[self.question_number]
        input(f"Q. {self.question_number}: {currentItem.text} (True/False): ")