import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked multiple-choice questions.")
        print("Let's see how many you can answer correctly.\n")

    def display_question(self, question):
        print(question['question'])
        for i, choice in enumerate(question['choices']):
            print(f"{i + 1}. {choice}")
        print()

    def evaluate_answer(self, question, answer):
        if answer.lower() == question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {question['answer']}\n")

    def play_game(self):
        self.display_welcome_message()
        random.shuffle(self.questions)
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Your answer: ")
            self.evaluate_answer(question, user_answer)
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        while True:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == 'yes':
                return True
            elif play_again.lower() == 'no':
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    questions = [
        {
            'question': "What is the capital of France?",
            'choices': ["Paris", "London", "Berlin", "Madrid"],
            'answer': "Paris"
        },
        {
            'question': "Who wrote 'To Kill a Mockingbird'?",
            'choices': ["Stephen King", "Harper Lee", "J.K. Rowling", "George Orwell"],
            'answer': "Harper Lee"
        },
        {
            'question': "What is the chemical symbol for water?",
            'choices': ["H2O", "CO2", "NaCl", "O2"],
            'answer': "H2O"
        }
    ]

    while True:
        quiz = Quiz(questions)
        quiz.play_game()
        if not quiz.play_again():
            break
