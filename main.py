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

#เขียนฟังชั่นที่ retuen yes หรือ no เพื่อให้ผู้ใช้เลือกว่าจะกรอกเองหรือ ให้โปรแกรงสุ่มให้
def mode_select():
    

#เขียนฟังชั่นที่ retuen จำนวนตัวเลขที่จะกรอก เช่น 5 เท่ากับต้องกรอก 5 ตัวเลข
def round_select():
    while True:
        try:
            _round = int(_input("How many numbers would you like to input? ").strip())
            if _round > 0:
                return _round
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")
    

#ขียนฟังชั่นที่จะสุ่มตัวเลขตามจะนวนที่ผู้เล่นเลือ(_round)
def auto_Input(_round):
    

def promp_for_list(_round):
    for _ in range(_round):
        while True:
            try:
                num_Input = int(_input("Enter a number: ").strip())
                numbers.append(num_Input)
                clear_console()
                break
            except ValueError:
                print("Please enter a valid number.")

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
