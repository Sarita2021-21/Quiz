from quiz_1 import Question
from data_2 import question_data
from quiz_brain import Quiz_brain

question_bank=[]
for questions in question_data:
    question_text=questions["question"]
    question_answer=questions["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
    
quiz=Quiz_brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    
print("Congratulations you completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")