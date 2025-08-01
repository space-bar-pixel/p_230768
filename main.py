import random

numbers = []

def _input(text):
    return input(text)

def sortList(_list):
    _list.sort()
    return _list

def mode_select():
    while True:
        try:
            _mode = _input("Use auto input? y/n or yes/no: ").strip().lower()
            if _mode not in ["y", "n", "yes", "no"]:
                raise ValueError("Please enter a valid response (y/n or yes/no)")
            return _mode
        except ValueError as e:
            print(e)

def round_select():
    while True:
        try:
            _round = int(_input("Enter the number of values: ").strip())
            if _round <= 0:
                raise ValueError
            return _round
        except ValueError:
            print("Please enter a positive whole number only.")

def auto_Input(_round):
    global numbers
    numbers = [random.randint(1, 100) for _ in range(_round)]

def promp_for_list(_round):
    for _ in range(_round):
        while True:
            try:
                num_Input = int(_input("Enter a number: ").strip())
                numbers.append(num_Input)
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

if __name__ == "__main__":
    main()
