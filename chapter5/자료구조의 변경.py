# 자료구조의 변경
# type으로 자료형 확인 가능
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# list로 바꾸기
menu = list(menu)
print(menu, type(menu));

# 튜플로 바꾸기
menu = tuple(menu)
print(menu, type(menu))

# 다시 사전형으로 바꾸기
menu = set(menu)
print(menu, type(menu))