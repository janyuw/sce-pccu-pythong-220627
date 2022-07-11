ans = 0
tip = "如果存在，請輸入(Y)，輸入其他表示無"
q1 = "(1, 3, 5, 7), 是不是您心中默想的數字\n "
a1 =input(q1 + tip)

if a1 == "y" or a1 == "Y":
    ans += 1


q2 = "(2, 3, 6, 7), 是不是您心中默想的數字\n "
a2 =input(q2 + tip)

if a2 == "y" or a1 =="Y":
    ans += 2

q3 = "(4, 5, 6, 7), 是不是您心中默想的數字\n "
a3 =input(q3 + tip)

if a1 == "y" or a1 =="Y":
    ans += 4

print("您心中默想的數字為：" , ans)