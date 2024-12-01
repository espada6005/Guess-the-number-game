import random

while True:
    min_num = int(input("最小数を入力してください："))
    max_num = int(input("最大数を入力してください："))
    if min_num < max_num:
        break
    else:
        print("\n最小数 < 最大数になるように入力してください\n")

answer = random.randint(min_num, max_num)
print(answer)

guess_num = int(input("数字を入力してください："))

while guess_num != answer:
    if guess_num < answer:
        print(f"答えは{guess_num}より大きいです")
    else:
        print(f"答えは{guess_num}より小さいです")
    guess_num = int(input("数字を入力してください："))

print("正解です")
