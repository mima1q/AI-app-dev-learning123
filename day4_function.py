def say_hello():
    print("大家好！")
    print("欢迎学习Python函数！")
say_hello()
say_hello()
def greet(name):
    print(f"你好，{name}!")
    print(f"欢迎{name}来到AI之旅!")
greet("小明")
greet("小红")
def add(a,b):
    return a+b
sum1=add(10,20)
print(sum1)
sum2=add(3,5)
print(sum2)
print(add(100,200))
def circle_area(radius):
    pi=3.14159
    area=pi*radius*radius
    return area
area1=circle_area(5)
print(f"半径是5的圆面积是：{area1}")
area2=circle_area(10)
print(f"半径是10的圆面积是：{area2}")
def get_user_info():
    name="小明"
    age=20
    city="杭州"
    return name,age,city
name,age,city=get_user_info()
print(f"姓名：{name},年龄:{age},城市：{city}")


