# 기본 연산
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

# 제곱
print(2**3) # 2^3 = 8

# 나머지 구하기
print(5%3) # 2
print(10%3) # 1

# 몫 구하기
print(5//3) # 1
print(10//3) # 3

# 비교연산
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 7) # False
print(5 <= 5) # True

# 비교연산 중 같은지 판단 '=='
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

# 같지 않은지 판단 '!='
print(1 != 3) # Truee
# not으로 작성해도 된다.
print(not(1 == 3)) # True

# 앞의 조건과 뒤의 조건을 모두 만족할 때만 True
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

# 앞의 조건과 뒤의 조건 중 하나만 만족해도 True
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) #True

# 연속된 비교도 가능
print(5 > 4 > 3) #True
print(5 > 4 > 7) #False