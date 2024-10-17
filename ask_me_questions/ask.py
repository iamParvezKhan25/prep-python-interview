import random


def store_question(questions):
    question = input("Enter a question: ")
    questions.append(question)
    print("Question stored successfully.")


def ask_questions(questions):
    random.shuffle(questions)
    for i in range(len(questions)):
        print(questions[i])
        input()
        if i < len(questions) - 1:
            print(questions[i + 1])
            input()


def main():
    questions = []
    while True:
        print("Menu:")
        print("1. Store Question")
        print("2. Ask Interview Questions")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            store_question(questions)
        elif choice == 2:
            ask_questions(questions)
        elif choice == 3:
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
