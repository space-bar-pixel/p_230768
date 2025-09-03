import os
import random

numbers = []

def clear_console():
    return os.system('cls' if os.name == 'nt' else 'clear')

def _input(text):
    return input(text)

def sortList(_list):
    _list.sort()
    return _list

def mode_select():
    

def round_select():
   

def auto_Input(_round):
    

def promp_for_list(_round):
    

def main():
    while True:
        numbers.clear()
        _mode_ = mode_select()
        _round = round_select()

        if _mode_ in ["yes", "y"]:
            auto_Input(_round)
        elif _mode_ in ["no", "n"]:
            promp_for_list(_round)

        print("Sorted list:", sortList(numbers))
        print()
        
        play_again = _input("Play again? y/n: ").strip().lower()
        if play_again not in ["y", "yes"]:
            print("Thank you for using the program!")
            break
        
        clear_console()

if __name__ == "__main__":
    main()