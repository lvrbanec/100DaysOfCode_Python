from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Reformat the data: create a list of objects containing .question and .answer
# from a list of dictionaries with "question" and "answer"
question_bank = []
for dictionary in question_data:
    question = dictionary["text"]
    answer = dictionary["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

# create an object quiz, on which the program is ran
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")