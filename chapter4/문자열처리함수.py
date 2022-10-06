python = 'Python is Amazing'

# 모든 문자 소문자로 치환
print(python.lower());

# 모든 문자 대문자로 치환
print(python.upper());

# 특정 문자열이 대문자인지 확인하기
print(python[0].isupper());

# 문자열 길이 반환
print(len(python))

# 특정 문자만 찾아서 바꾸기
print(python.replace("Python", "Java"))

# 특정문자가 처음으로 나오는 자리 수
index = python.index("n");
print(index);

# 특정문자가 두 번째로 나오는 자리 수
index = python.index("n", index + 1);
print(index)

# find로도 찾을 수 있음
print(python.find("n"))

# find는 원하는 문자열을 찾을 수 없을때 -1을 반환
print(python.find("Java")) # -1

# index로 없는 문자열을 찾으면 오류가 나온다.
# print(python.index("Java")) # Error

# 특정 문자열이 얼마나 반복되는지
print(python.count("n"))