# ฟังก์ชันสำหรับการบวก
def add(x, y):
    return x + y

# ฟังก์ชันสำหรับการลบ
def subtract(x, y):
    return x - y

# ฟังก์ชันสำหรับการคูณ
def multiply(x, y):
    return x * y

# ฟังก์ชันสำหรับการหาร
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! การหารด้วย 0 ไม่สามารถทำได้."

# แสดงเมนูให้เลือก
def calculator():
    print("เลือกการคำนวณ:")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")
    
    while True:
        try:
            # รับตัวเลือกจากผู้ใช้
            choice = input("กรุณาเลือก (1/2/3/4): ")

            # ตรวจสอบว่าผู้ใช้เลือกอะไร
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("กรุณาใส่ตัวเลขตัวแรก: "))
                num2 = float(input("กรุณาใส่ตัวเลขตัวที่สอง: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("เลือกไม่ถูกต้อง! กรุณาเลือกใหม่.")
            
            next_calculation = input("ต้องการคำนวณอีกครั้งหรือไม่? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("ขอบคุณที่ใช้โปรแกรมเครื่องคิดเลข!")
                break
        except ValueError:
            print("กรุณาใส่ตัวเลขที่ถูกต้อง.")

# เรียกใช้งานฟังก์ชัน calculator
calculator()
