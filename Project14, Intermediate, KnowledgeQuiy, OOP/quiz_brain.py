class QuizBrain:

    # load in the question list of objects, set the question number as 0
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # check if there are unused objects left in the list of objects
    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    # increase the question number and show the next question
    def next_question(self):
        current_question = self.question_list[self.question_number] # enters the
        # specific object in a list, no matter of its name
        # current_question.text fetches the object's attribute text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # checks if the answer was correct and tracks the number of right answers
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
