# ฟังก์ชันแปลงเซลเซียสเป็นฟาเรนไฮต์
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# การใช้งานโปรแกรม
def main():
    # ขออุณหภูมิจากผู้ใช้
    celsius = float(input("กรุณาใส่อุณหภูมิในหน่วยเซลเซียส: "))
    
    # แปลงเป็นฟาเรนไฮต์
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # แสดงผลลัพธ์
    print(f"{celsius}°C เท่ากับ {fahrenheit}°F")

if __name__ == "__main__":
    main()
