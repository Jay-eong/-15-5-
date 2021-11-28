import turtle

sum=0

print("================")
print("이것은 심리적 에너지에 대한 검사입니다.")
print()
print("심리적 에너지란, 어떤 일에 정신적으로 집중, 몰입하기 위해 공급되는 에너지로 심리적 에너지의 흐름이 개인의 내부에서 나올 경우에는 내향성, 외부에서 나올 경우에는 외향성으로 판단합니다.")
print()
print("이 검사는 다섯가지의 질문으로 이루어지며, 질문의 가짓수가 적고, 검사 당시 개인의 기분에 따라 결과가 달라질 수 있습니다.")
print("그렇기 때문에 검사를 지나치게 맹신하고, 결과에 자기 자신을 가두지 않도록 주의하시기 바랍니다.")
print()
print("이제부터 검사를 시작하겠습니다. 질문에 Y 혹은 N으로 답변 바랍니다.")

print()

print("1. 다른 사람들과 함께하는 활동에서 듣기 보다는 이야기하는 것을 선호한다.")
aa=input("대답[Y(y) or N(n)]: ").upper()
if aa=='Y' or 'y':
    sum=sum+1
elif aa=='N' or 'n':
    sum=sum
else:
    print("Y(y) 혹은 N(n)을 입력하십시오.")

print()

print("2. 글보다는 말로 표현하는 것을 선호한다.")
aa=input("대답[Y(y) or N(n)]: ").upper()
if aa=='Y' or 'y':
    sum=sum+1
elif aa=='N' or 'n':
    sum=sum
else:
    print("Y(y) 혹은 N(n)을 입력하십시오.")

print()

print("3. 혼자있는 시간보다는 다른 사람과 함께있는 시간을 선호한다.")
aa=input("대답[Y(y) or N(n)]: ").upper()
if aa=='Y' or 'y':
    sum=sum+1
elif aa=='N' or 'n':
    sum=sum
else:
    print("Y(y) 혹은 N(n)을 입력하십시오.")

print()

print("4. 소수보다는 다수와 어울리는 것을 선호한다.")
aa=input("대답[Y(y) or N(n)]: ").upper()
if aa=='Y' or 'y':
    sum=sum+1
elif aa=='N' or 'n':
    sum=sum
else:
    print("Y(y) 혹은 N(n)을 입력하십시오.")

print()

print("5. 자기 내부보다는 자기 외부에 가치를 두는 경우가 많다.")
aa=input("대답[Y(y) or N(n)]: ").upper()
if aa=='Y' or 'y':
    sum=sum+1
elif aa=='N' or 'n':
    sum=sum
else:
    print("Y(y) 혹은 N(n)을 입력하십시오.")

print()

if sum >= 3:
    print("당신은 외향성일 가능성이 높습니다.")
    turtle.pensize(5)
    turtle.write("E", font=('arial', 100))

if sum < 3:
    print("당신은 내향성일 가능성이 높습니다.")
    turtle.pensize(5)
    turtle.write("I", font=('arial', 100))
