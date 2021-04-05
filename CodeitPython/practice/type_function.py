print(type(3))
print(type(3.0))
print(type("3"))
print(type("TRUE"))
print(type(True))

def hello():
    print("Hello world!")

print(type(hello))
print(type(print))
# type() 자료형을 출력해주는 함수

# 실행 결과
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'str'>
# <class 'bool'>
# <class 'function'>
# <class 'builtin_function_or_method'>
