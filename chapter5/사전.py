# key값이 key-value 형식
cabinet = {3: "유재석", 100: "김태호"}

# 사전에 접근하는 방법
print(cabinet[3])
print(cabinet.get(3))

# [] 로 접근할 때는 key가 없는 경우 Error를 뱉고 프로그램이 종료됨
# print(cabinet[5])

# get으로 접근할 때는 key 가 없는 경우 None이 출력된다.
print(cabinet.get(5))

# None이 아니고 다른 값을 출력하고 싶은 경우 두 번째 인자로 출력값을 넘겨주면 된다.
print(cabinet.get(5, "사용 가능"))

# 사전 자료형에 key가 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

# 새로운 key를 할당하는 방법
cabinet["B-30"] = "조세호"
print(cabinet)

# 만약 기존에 있던 key와 같은 key를 할당하면 덮어쓰기가 된다.
cabinet[3] = "하하"
print(cabinet)

# del로 값을 지울 수 있다.
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모든 값을 지우기
cabinet.clear()
print(cabinet)