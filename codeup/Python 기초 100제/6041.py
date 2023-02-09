"""
정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

예시
...
print(a%b)

참고
python 언어에서는 나눈 나머지를 계산하는 연산자(%, remainder)를 제공한다.
a%b 와 같이 작성하면, a를 b로 나눈 나머지(remainder)를 계산해준다.
나머지 연산(modulus, mod 연산)은 수학자 가우스가 생각해 낸 연산으로,
어떤 수를 다른 수로 나누고 난 후 남는 나머지를 계산하는 연산이다.

실수로 나눈 나머지가 어떻게 계산될지도 생각해보자.
"""

a, b = map(int, input().split())
c = a%b

print(c)