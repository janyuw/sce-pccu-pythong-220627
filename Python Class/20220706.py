a = 706
b = 22

if a < b:
    print("A > B")
    print("我還在if裡")
print("我已經離開if")

if a > b: print("一行式寫法")

if a < b:
    print("a < b")
else:
    print("a > b")

print("已出if else結構")


score = input("請輸入你的python成績")
score_int = int(score)
if score_int >=70:
    print("老王可以放1天假")
elif score_int >=60 and score_int < 70:
    print("老王可以放半天假")
else:
    print("老王不能放假")