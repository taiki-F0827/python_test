#1
print("hello world")

#2greet関数の定義
def greet():
    print("こんにちは")

greet()

#3print_name関数
def print_name(name:str):
    print("私の名前は"+name+"です")

print_name("タイキ")

#4get_greet関数
def get_greet():
    return "おはようございます"

greet=get_greet()
print(greet)

#5add関数
def add(a:int,b:int):
    return a+b

add=add(1,2)
print(add)
