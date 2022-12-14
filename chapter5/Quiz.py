'''
    Quiz 2) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
    참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
    추첨 프로그램을 작성하시오.

    조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
    조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
    조건3 : random 모듈의 suffle 과 sample을 활용

    (출력 예제)
    -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자 : [2, 3, 4]
    -- 축하합니다 --

    (활용 예제)
    from random import *
    lst = [1,2,3,4,5]
    print(lst)
    shuffle(lst)
    print(lst)
    # sample : 무작위로 두 번째 인자만큼 list에서 뽑는다.
    print(sample(lst, 1))
'''

from random import *

users = range(1, 21) # 1부터 21 직전 까지 숫자를 생성 type을 range로 나옴
users = list(users) # list로 변경
shuffle(users) # list 섞기

winners = sample(users, 4) # 4명 중 1명은 치킨, 4명은 커피
winChicken = sample(winners, 1)[0];

winners.remove(winChicken)

print(f"-- 당첨자 발표 --\n치킨 당첨자 : {winChicken}\n커피 당첨자 : {winners}\n-- 축하합니다 --")