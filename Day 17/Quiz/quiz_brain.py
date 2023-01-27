class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        curren_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curren_question.text} (True/False) ").lower()
        self.check_answer(user_answer, curren_question.answer)

    def still_has_question(self):
        return True if self.question_number < len(self.question_list) else False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"You got it wrong, the correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
