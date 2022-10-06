# 주민등록번호에서 슬라이싱 하기
jumin = "990120-1234567";

# 문자열의 첫 번째 index는 0으로 시작
print("성별 : " + jumin[7])

# 여러자리 가져오기 [x:y] x부터 y 직전값 까지
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

# 처음부터 6직전까지
print("생년월일 : " + jumin[:6])

# 뒤 7자리 가져오기
print("뒤 7자리 : " + jumin[7:])

# 뒤에서 부터 계산하기
print("뒤 7자리 (뒤에서부터) " + jumin[-7:])