class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # first attribute
        self.question_list = q_list  # Second attribute
        self.score = 0  # To track of the number players score

    # def still_has_question(self):
    #     if self.question_number < len(self.question_list):
    #         return True
    #     else:
    #         False

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print('You have got it right')
            self.score +=1
        else:
            print('That\'s wrong')
        print(f'The correct answer is {correct_answer}')
        print(f'your current score is: {self.score}/{self.question_number}')
        print('\n')


"""The simpler way to write the above method is as follows:
def still_has_question:
    return self.question_number < len(self.question_list)

"""
