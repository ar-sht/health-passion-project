from termcolor import cprint
import time


def print_intro():
    cprint('''
 _ _ _       _                         ___  ___ 
| | | | ___ | | ___  ___ ._ _ _  ___  |_ _|| . |
| | | |/ ._>| |/ | '/ . \| ' ' |/ ._>  | | | | |
|__/_/ \___.|_|\_|_.\___/|_|_|_|\___.  |_| `___'
''', "light_magenta")
    time.sleep(0.5)
    cprint('''
 /$$      /$$                       /$$               /$$       /$$   /$$                     /$$   /$$     /$$      
| $$$    /$$$                      | $$              | $$      | $$  | $$                    | $$  | $$    | $$      
| $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$ | $$      | $$  | $$  /$$$$$$   /$$$$$$ | $$ /$$$$$$  | $$$$$$$ 
| $$ $$/$$ $$ /$$__  $$| $$__  $$|_  $$_/   |____  $$| $$      | $$$$$$$$ /$$__  $$ |____  $$| $$|_  $$_/  | $$__  $$
| $$  $$$| $$| $$$$$$$$| $$  \ $$  | $$      /$$$$$$$| $$      | $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$    | $$  \ $$
| $$\  $ | $$| $$_____/| $$  | $$  | $$ /$$ /$$__  $$| $$      | $$  | $$| $$_____/ /$$__  $$| $$  | $$ /$$| $$  | $$
| $$ \/  | $$|  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$  |  $$$$/| $$  | $$
|__/     |__/ \_______/|__/  |__/   \___/   \_______/|__/      |__/  |__/ \_______/ \_______/|__/   \___/  |__/  |__/
    ''', "cyan")


def print_option():
    cprint('''
 __   ____  _     ____  __   _____      ___   _      ____ 
( (` | |_  | |   | |_  / /`   | |      / / \ | |\ | | |_  
_)_) |_|__ |_|__ |_|__ \_\_,  |_|      \_\_/ |_| \| |_|__ 
 ''', "light_grey")
    cprint("[1] Learn about depression", "light_red")
    cprint("[2] Learn about anxiety", "yellow")
    cprint("[3] Find resources to help", "green")
    cprint("[4] Look at my wonderful sources", "light_cyan")