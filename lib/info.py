from termcolor import cprint
import time


def print_general_info(topic):
    with open(f"resources/{topic}.txt") as text:
        lines = text.readlines()

    for line in lines:
        if line.startswith("-1"):
            cprint("\n"+line[2:], "white", attrs=["underline"], end="")
            time.sleep(0.5)
        elif line.startswith("-2"):
            cprint("\n"+line[2:], "white", attrs=["bold"], end="")
            time.sleep(0.75)
        elif line.startswith("+"):
            cprint("\t- " + line[1:], "light_grey")
            time.sleep(1.5)
        else:
            cprint(line, "light_grey", end="")
            time.sleep(1)

    cprint("\n\nPress enter to return home.", "light_red", attrs=["bold"])
