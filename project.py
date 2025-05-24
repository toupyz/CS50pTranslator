import random
import os

HIGHSCORE_FILE = "times_table_highscore.txt"

def load_highscore(): # Load high score from a file, or return 0 if no file exists.
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0


def save_highscore(score): # Save high score to a file.
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))


def ask_question(): # Generate a random multiplication question from 1 to 12 and return if the answer was correct.
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    correct_answer = a * b
    while True:
        try:
            user_answer = int(input(f"What is {a} x {b}? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    return user_answer == correct_answer


def main():
    print("Welcome to the Times Table Quiz Game!")
    print("Answer the multiplication questions correctly. Type Ctrl+C to quit anytime.\n")
    highscore = load_highscore()
    print(f"Current high score: {highscore}\n")

    score = 0

    try:
        while True:
            if ask_question():
                score += 1
                print(f"Correct! Your score is now {score}.\n")
            else:
                print("Oops, wrong answer!")
                print(f"Your final score: {score}")

                if score > highscore:
                    print("Congrats! New high score!")
                    save_highscore(score)
                else:
                    print(f"High score remains: {highscore}")

                break

    except KeyboardInterrupt:
        print("\nThanks for playing! See you next time.")
        if score > highscore:
            save_highscore(score)


if __name__ == "__main__":
    main()

