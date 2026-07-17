age=int(input("请输入你的年龄："))
if age>=18:
    print("你已经成年了，可以投票!")
else:
    print("你还未成年，再等等吧!")
score=int(input("请输入你的成绩："))
if score>=90:
    print("优秀！A等")
elif score>=80:
    print("良好！B等")
elif score>=60:
    print("及格！C等")
else:
    print("不及格，继续加油！")