text = input()
length = len(text)

if length == 0 or length > 80:
    exit("문자열의 길이가 범위를 벗어남 (0 < n <= 80")
if text[0] == ' ' or text[-1] == ' ':
    exit("문자열의 시작 또는 끝에 공백이 있음")
if text.count('  ') != 0 or text.count('  '):
    exit("문자열에 공백이 연속해서 있음")
if text.count('/n') > 1:
    exit("문자열에 개행이 있음")

words = text.count(' ') + 1
print(words)