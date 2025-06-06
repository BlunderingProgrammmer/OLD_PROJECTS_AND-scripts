class Quiz_brain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} :(true/false)")
        self.check_answer(user_answer, current_question.answer)

    # def sill_has_questions(self):
    #     if self.answer == "true":
    #         self.next question()
    #     else:
    #         return False
    # def still_has_question(self):
    #     if self.question_number != len(self.question_list):
    #         return True
    #     else:
    #         return False

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("you got it wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
