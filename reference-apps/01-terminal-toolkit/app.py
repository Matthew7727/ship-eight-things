"""Reference build for Project 1: a small, reusable terminal toolbox."""
import random


def number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def convert() -> None:
    celsius = number("Celsius: ")
    kilometres = number("Kilometres: ")
    print(f"{celsius}°C is {celsius * 9 / 5 + 32:.1f}°F")
    print(f"{kilometres} km is {kilometres * 0.621371:.1f} miles")


def roll_dice() -> None:
    dice, sides = int(number("How many dice? ")), int(number("How many sides? "))
    if dice < 1 or sides < 2:
        print("Use at least one die with two sides.")
        return
    rolls = [random.randint(1, sides) for _ in range(dice)]
    print(f"Rolled {rolls}; total: {sum(rolls)}")


def split_tip() -> None:
    bill, percent, people = number("Bill: £"), number("Tip percent: "), int(number("People: "))
    if people < 1:
        print("There must be at least one person.")
        return
    print(f"£{bill * (1 + percent / 100) / people:.2f} each")


def guess_game() -> None:
    secret, attempts = random.randint(1, 20), 0
    print("Guess a number between 1 and 20.")
    while True:
        guess, attempts = int(number("Guess: ")), attempts + 1
        if guess == secret:
            print(f"Correct in {attempts} guesses.")
            return
        print("Too low." if guess < secret else "Too high.")


def main() -> None:
    actions = {"1": convert, "2": roll_dice, "3": split_tip, "4": guess_game}
    while True:
        print("\n1 Convert  2 Dice  3 Split a tip  4 Guessing game  q Quit")
        choice = input("Choose: ").lower().strip()
        if choice == "q": return
        action = actions.get(choice)
        if action: action()
        else: print("Choose 1–4 or q.")


if __name__ == "__main__":
    main()
