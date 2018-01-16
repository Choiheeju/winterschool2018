import random

a1="시도해보세요!"
a2="다시한번생각해보세요!"
a3="그건 좋은생각같지않아요"
a4="장난해요?"
a5="정말 좋은 생각이네요!"
a6="수리부엉이"
a7="멍멍"
a8="현명한 선택이예요!"

print("어서오세요! 환연합니다!")

Q=input("조언을 구하고 싶은 질문을 입력하세요! 그리고 엔터키를 누르세요!\n")

print("고민중...\n"*3,)

C=random.randint(1,8)
if C==1:
    a=a1
elif C==2:
    a=a2
elif C==3:
    a=a3
elif C==4:
    a=a4
elif C==5:
    a=a5
elif C==6:
    a=a6
elif C==7:
    a=a7
else:
    a=a8

print(a)
