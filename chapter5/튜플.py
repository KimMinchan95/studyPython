# 리스트와 다르게 내용을 변경하거나 추가할 수 없다
menu = ("돈까스", "치즈까스")

# 값을 출력하는 방법
print(menu[0])

# 튜플 활용법

# 튜플 활용 전
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# 튜플 활용 후 - 값을 한 번에 넣을 수 있다.
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

print(name)