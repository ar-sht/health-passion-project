from lib import info, intro
import time
import re

CHOICE_TO_FILE = {
    "1": "depression",
    "2": "anxiety",
    "3": "help",
    "4": "sources"
}


if __name__ == "__main__":
    intro.print_intro()
    time.sleep(1)
    while True:
        intro.print_option()

        choice = input("Pick one (1, 2, 3, 4, or 'exit' to leave): ").strip().lower()
        if choice == "exit":
            exit(0)

        while not re.match("^[1-4]$", choice):
            choice = input("Invalid input, please try again: ").strip().lower()
            if choice == "exit":
                exit(0)
        print("\033[2J", end="")
        print("\033[H", end="")

        info.print_general_info(CHOICE_TO_FILE[choice])
        _ = input()
        print("\033[2J", end="")
        print("\033[H", end="")
