import random

def roll_dice():
    return random.randint(1, 6)

# คะแนนสะสม
player1_score = 0
player2_score = 0

print("🎲 เกมทอยลูกเต๋า: ผู้เล่น 2 คน แข่งกันคนละ 3 ครั้ง")

# ทอยลูกเต๋า 3 ครั้ง
for turn in range(1, 6):
    input(f"\n[เทิร์น {turn}] กด Enter เพื่อให้ผู้เล่น 1 ทอยลูกเต๋า...")
    roll1 = roll_dice()
    print("ผู้เล่น 1 ได้:", roll1)
    player1_score += roll1

    input("กด Enter เพื่อให้ผู้เล่น 2 ทอยลูกเต๋า...")
    roll2 = roll_dice()
    print("ผู้เล่น 2 ได้:", roll2)
    player2_score += roll2

# แสดงผลรวม
print("\n--- ผลลัพธ์ ---")
print("ผู้เล่น 1 ได้คะแนนรวม:", player1_score)
print("ผู้เล่น 2 ได้คะแนนรวม:", player2_score)

# ประกาศผลผู้ชนะ
if player1_score > player2_score:
    print("🎉 ผู้เล่น 1 ชนะ!")
elif player2_score > player1_score:
    print("🎉 ผู้เล่น 2 ชนะ!")
else:
    print("🤝 เสมอกัน!")
