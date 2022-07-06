print("abc")
print("abc", "測試", "abc123")
print("abc", "測試", "abc123", sep=" > ")
print("abc", "測試", "abc123", sep="", end="@")
print("abc", "測試", "abc456", end="")
print("abc", "測試", "abc789", end="\t")
print("abc", "測試", "abc999", end="\n")

x=123
y=456
print(x + y)
print(str(x) + str(y))
z = 7654321
print(int(z)- y)

#練習格式化輸出
score = 90.2
name = "Frank Wang"
count = 4
print("%s 你的python成績是 %d" %(name, score))

print("{} 你的第{}次python成績是{}".format(name, count, score))
print("{0} 你的第{1}次python成績是{2}".format(name, count, score))
print("{2} 你的第{0}次python成績是{1}".format(count, score, name))
print("{n} 你的第{c}次python成績是{s}".format(c=count, s=score, n=name))

x = 12345
y = -123
print("x = /%d/" % x)
print("x = /%6d/" % x)
print("x = /%4d/" % x)
print("x = /%+4d/" % x)

print("y = /%d/" % y)
print("y = /%2d/" % y)
print("y = /%5d/" % -65536)

a1 = 123.56
print("%4.2f" %(a1))

#對齊符號的練習
pi = 3.14159
r = 8
area = pi * r **2
print("/半徑{}, 圓面積是{}/".format(r, area))
print("/半徑{0:3d}, 圓面積是{1:10.2f}/".format(r, area))
print("/半徑{0:<3d}, 圓面積是{1:<10.2f}/".format(r, area))
print("/半徑{0:^3d}, 圓面積是{1:^10.2f}/".format(r, area))
print("/半徑{0:>3d}, 圓面積是{1:>10.2f}/".format(r, area))

fs1 = open("output1.txt", mode="w")
print("這是測試檔案寫入", file=fs1)
fs1.close

fs2 = open("output1.txt", mode="a")
print("這是測試檔案寫入-2", file=fs2)
fs2.close

name2 = input("請輸入姓名")
eng = input("請輸入英文成績")
print("name2 的資聊型態是", type(name2))
print("eng 的資聊型態是", type(name2))
print(int(eng) * 100)