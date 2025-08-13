# BIG TEAM
นี่เป็น master repo ของกลุ่ม big ใช้เพื่อส่งงานกลุ่ม

# วิธีทำงาน
1. สร้าง branch เป็นของตัวเอง
2. ทำงานแก้ไขใน branch ของตัวเอง
3. ห้ามแก้ไขจาก main branch

# วิธีส่งงาน ให้ทำการ pull request เพื่องส่งงานเท่านั้น

1. สร้างและสลับไปยัง branch ของตัวเอง:
ใช้คำสั่ง git checkout -b <branch ของตัวเอง> เพื่อสร้างและสลับไปยังสาขาใหม่สำหรับการเปลี่ยนแปลง. 
ตัวอย่าง: git checkout -b feature/new-feature

3. ทำการเปลี่ยนแปลง:
แก้ไขไฟล์และเพิ่มการเปลี่ยนแปลงใน branch ของตัวเอง.

5. เพิ่มและคอมมิตการเปลี่ยนแปลง:
ใช้ git add . เพื่อเพิ่มการเปลี่ยนแปลงทั้งหมดไปยัง staging area. 
ใช้ git commit -m "<ข้อความ_คอมมิต>" เพื่อบันทึกการเปลี่ยนแปลงพร้อมข้อความอธิบาย.

7. push branch ของตัวเองไปยัง githuh:
ใช้ git push origin <branch ของตัวเอง> เพื่ออัปโหลด branch ของตัวเอง และ คอมมิตไปยัง GitHub.

9. สร้าง Pull Request:
ไปที่หน้าหลักของที่เก็บข้อมูลบน GitHub (หรือแพลตฟอร์ม Git อื่นๆ). 
เลือก branch ของตัวเอง ที่เพิ่ง push ไป. 
คลิก "Compare & pull request" หรือ "New pull request". 
ตรวจสอบข้อมูลในหน้า Pull Request (branch base, branch head, ชื่อเรื่อง, คำอธิบาย). 
คลิก "Create pull request" เพื่อสร้าง Pull Request. 


