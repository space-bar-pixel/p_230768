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
            _mode = _input("ใช้ระบบ auto input หรือไม่ y/n or yes/no : ").strip().lower()
            if _mode not in ["y", "n", "yes", "no"]:
                raise ValueError("กรุณากรอกคำตอบให้ถูกต้อง (y/n or yes/no)")
            return _mode
        except ValueError as e:
            print(e)

def round_select():
    while True:
        try:
            _round = int(_input("เลือกจำนวนตัวเลข : ").strip())
            if _round <= 0:
                raise ValueError
            return _round
        except ValueError:
            print("กรุณากรอกตัวเลขจำนวนเต็มบวกเท่านั้น")

def auto_Input(_round):
    global numbers
    numbers = [random.randint(1, 100) for _ in range(_round)]

def promp_for_list(_round):
    for _ in range(_round):
        while True:
            try:
                num_Input = int(_input("กรอกตัวเลข : ").strip())
                numbers.append(num_Input)
                break
            except ValueError:
                print("กรุณากรอกตัวเลขที่ถูกต้อง")

def main():
    while True:
        numbers.clear()
        _mode_ = mode_select()
        _round = round_select()

        if _mode_ in ["yes", "y"]:
            auto_Input(_round)
        elif _mode_ in ["no", "n"]:
            promp_for_list(_round)

        print("ลำดับที่เรียงแล้ว:", sortList(numbers))
        print()
        
        play_again = _input("เล่นอีกรอบหรือไม่ y/n : ").strip().lower()
        if play_again not in ["y", "yes"]:
            print("ขอบคุณที่ใช้โปรแกรม!")
            break
        

if __name__ == "__main__":
    main()
