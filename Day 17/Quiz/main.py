from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
qb = QuizBrain(question_bank)

while qb.still_has_question():
    qb.next_question()
    print()

print()
print("The quiz is over")
print(f"Your final score is: {qb.score}/{qb.question_number}")
