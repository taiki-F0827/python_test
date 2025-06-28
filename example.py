#1 hello worldの出力
print("hello world")
#2 greet function
def greet():
    print("こんにちは")
greet()
#3 print_name function
def print_name(name:str):
    print("私の名前は"+name+"です")
print_name("タイキ")

#4 get_greet function
def get_greet():
    return "おはようございます"
greet=get_greet()
print(greet)

#5 add function
def add(a:int,b:int):
    return a+b
add=add(1,2)
print(add)

