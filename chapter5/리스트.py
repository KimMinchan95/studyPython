# 리스트 [] - 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
from traceback import print_tb


subway = [10, 20, 30];

print(subway);

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 탐 append 배열에 마지막에 값 넣기
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(subway.index("유재석") + 1, "정형돈")
print(subway)

# pop 배열에 마지막에서 꺼내기
# 어떤 값이 나왔는지
print(subway.pop());
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5, 3, 2, 1, 4]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse();
print(num_list)

# 모두 지우기
num_list.clear();
print(num_list)

# 다양한 자료형 함께 사용
stirng_list = ["hi", "bye"]
mix_list = ["조세호", 20, True]

# 리스트 확장
stirng_list.extend(mix_list);
print(stirng_list)