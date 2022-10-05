from random import *;

# 랜덤함수로 난수 뽑기
print(random()); # 0.0이상 1.0 미만의 임의의 값 생성
print(random() * 10); # 0.0 이상 10.0 미만의 임의의 값 생성

# 정수값만 보고 싶을때
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성

print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# 범위 값으로 값 생성하기
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성