import random
import json

try:
    with open("score.json", "r") as f:
        best_score = json.load(f)
except FileNotFoundError:
    best_score = None

while True:

    print("""
Choose difficulty:
1. Easy (1 - 50)
2. Medium (1 - 100)
3. Hard (1 - 500)
""")

    difficulty = input("Select (1/2/3): ")

    if difficulty == "1":
        max_number = 50
    elif difficulty == "2":
        max_number = 100
    elif difficulty == "3":
        max_number = 500
    else:
        print("Invalid choice, defaulting to Medium")
        max_number = 100

    attempt = 0
    random_number = random.randint(1, max_number)

    print(f"\nGuess a number between 1 - {max_number}")

    while True:
        user_input = input("Your guess: ")

        if not user_input.isdigit():
            print("Please enter a valid number")
            continue

        user_guess = int(user_input)

        if user_guess < 1 or user_guess > max_number:
            print(f"Please enter a number between 1 - {max_number}")
            continue

        attempt += 1

        if user_guess == random_number:
            print("You guessed the number!")
            print(f"You won in {attempt} attempts!")

            # ---------------- BEST SCORE LOGIC ----------------
            if best_score is None or attempt < best_score:
                best_score = attempt
                print("🎉 New best score!")

                # SAVE TO FILE
                with open("score.json", "w") as f:
                    json.dump(best_score, f)

            print(f"Best score so far: {best_score} attempts")
            break

        elif user_guess > random_number:
            print("You are too high")
        else:
            print("You are too low")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break