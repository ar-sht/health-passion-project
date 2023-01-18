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
    cprint(r'''
 /'\_/`\               /\ \__        /\_ \     /\ \/\ \                /\_ \ /\ \__/\ \        
/\      \     __    ___\ \ ,_\    __ \//\ \    \ \ \_\ \     __     __ \//\ \\ \ ,_\ \ \___    
\ \ \__\ \  /'__`\/' _ `\ \ \/  /'__`\ \ \ \    \ \  _  \  /'__`\ /'__`\ \ \ \\ \ \/\ \  _ `\  
 \ \ \_/\ \/\  __//\ \/\ \ \ \_/\ \L\.\_\_\ \_   \ \ \ \ \/\  __//\ \L\.\_\_\ \\ \ \_\ \ \ \ \ 
  \ \_\\ \_\ \____\ \_\ \_\ \__\ \__/.\_/\____\   \ \_\ \_\ \____\ \__/.\_/\____\ \__\\ \_\ \_\
   \/_/ \/_/\/____/\/_/\/_/\/__/\/__/\/_\/____/    \/_/\/_/\/____/\/__/\/_\/____/\/__/ \/_/\/_/
    ''', "cyan")


def print_option():
    cprint('''
 __   ____  _     ____  __   _____      ___   _      ____ 
( (` | |_  | |   | |_  / /`   | |      / / \ | |\ | | |_  
_)_) |_|__ |_|__ |_|__ \_\_,  |_|      \_\_/ |_| \| |_|__ 
 ''', "light_grey")
    cprint("[1] Learn about depression", "red")
    cprint("[2] Learn about anxiety", "light_yellow")
    cprint("[3] Find resources to help", "green")
    cprint("[4] Look at my wonderful sources", "blue")
