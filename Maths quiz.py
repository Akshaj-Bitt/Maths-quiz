import random
from importlib.metadata import always_iterable

SCORES_FILE = "scores.txt"
OPERATORS = ["+", "-", "*"]


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    return a * b


def save_score(name, level1, level2):
    total = level1 + level2

    with open(SCORES_FILE, "a") as file:
        file.write(f"{name},{level1},{level2},{total}\n")



def show_scores():
    print("\n========== SCOREBOARD ==========")
    print("-" * 40)
    print(f"{'Name':10}{'L1':>6}{'L2':>6}{'Total':>8}")
    print("-" * 40)

    top_name = ""
    top_score = 0

    try:
        with open(SCORES_FILE, "r") as file:
            scores = file.readlines()

        if not scores:
            print("No scores yet!")
            return

        for line in scores:
            parts = line.strip().split(",")

            if len(parts) != 4:
                continue

            name, l1, l2, total = parts
            total = int(total)

            print(f"{name:10}{l1:>6}{l2:>6}{total:>8}")

            if total > top_score:
                top_score = total
                top_name = name

        print("-" * 40)
        print(f"TOP SCORER: {top_name} ({top_score} points)")
        print("-" * 40)

    except FileNotFoundError:
        print("No scores file found!")


def play_level(level, questions, minimum, maximum):
    print(f"\n========== LEVEL {level} ==========")

    score = 0
    lives = 3

    for question in range(1, questions + 1):

        if lives == 0:
            print("\nNo lives left!")
            break

        a = random.randint(minimum, maximum)
        b = random.randint(minimum, maximum)
        op = random.choice(OPERATORS)

        correct_answer = calculate(a, b, op)

        print(f"\nLives Left: {lives}")

        try:
            user_answer = int(input(f"Q{question}: {a} {op} {b} = "))

            if user_answer == correct_answer:
                print("Correct! +1")
                score += 1
            else:
                lives -= 1
                print(f"Wrong! Correct Answer: {correct_answer}")

        except ValueError:
            lives -= 1
            print("Invalid input! Life lost!")

    print(f"\nLevel {level} Score: {score}/{questions}")
    return score



def main():

    print("=" * 45)
    print("        WELCOME TO MATH QUIZ")
    print("=" * 45)

    while True:


        print("\n1. Play Quiz")
        print("2. View Scores")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("\nEnter your name: ")

            level1_score = play_level(1, 5, 1, 20)
            level2_score = 0

            if level1_score >= 3:
                print("\nLEVEL 2 UNLOCKED!")
                level2_score = play_level(2, 8, 10, 30)
            else:
                print("\nNeed 3 marks to unlock Level 2")

            save_score(name, level1_score, level2_score)

            print("\nScores Saved Successfully!")
            show_scores()

        elif choice == "2":
            show_scores()

        elif choice == "3":
            print("\nThanks for playing!")
            break

        else:
            print("Invalid choice!")


main()
