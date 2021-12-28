print("직각삼각형 그리기\n")

leg=int(input("변의 길이: "))	#직각삼각형 한 변의 길이를 input한다.

print("\n")
for i in range(leg):	#직각삼각형 그리기
	print("*" * (i+1))
	
print("\n")
area=leg ** 2 / 2 #넓이구하기
print("넓이: ", area)