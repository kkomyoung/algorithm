"""
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

예시
...
if n//3==1 :
  print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

"""

a = int(input())

if a==12 or a==1 or a==2:
  print('winter')
elif a==3 or a==4 or a==5:
  print('spring')
elif a==6 or a==7 or a==8:
  print('summer')
elif a==9 or a==10 or a==11:
  print('fall')