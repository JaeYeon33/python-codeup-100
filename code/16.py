# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

# 참고
# ...
# print(c2, c1)
# 와 같은 방법으로 출력하면, c1과 c2에 저장된 값이 공백을 두고 순서가 바뀌어 한 줄로 출력된다.
# print( ) 안에서 쉼표(,)를 찍어 순서대로 나열하면, 그 순서대로 공백을 두고 출력된다.


word1, word2 = map(str, input().split())
print(word2, word1)
