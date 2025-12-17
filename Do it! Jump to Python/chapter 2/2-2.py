#.count 는 매소드라고 외장함수

#자료형 
a="Python"
b= "Life is too short, You need Python"
head ="Python"
tail = " is fun"
print(head +tail)
print (a *3)
#응용
print("="*50) ## =을 50번함
print("my program")
print("="*50)
print(len(b)) ## 길이를 구하는 함수 length의 약어
print(b[3]) ## 파이썬은  0부터 시작

c= b[0:4] #0이상 4미만 까지라는 뜾 0~3 까지 들어간다는 띁
d= b[::2]#한칸 씩 띠어서 거끄로 불러온다는 뜿
print(c)
print(d)

e ="20230331Rainy"
date =e[:8] #첫자 부터 8자까지 출력
weater = e[8:] #8자부터 마지막 글자 출력
print(date)
print(weater)

#문자열 포메팅
#메크로 
f= "I eat %d apple" %3 #%d ,decimal의 약어 뜻 십진의

print(f)

name = '빵돌'
age = 36

#f 문자열 포매팅 
# 포메팅에 {}를 넣으면 별수를 넣을 수있음 **{}안에 연산가능 
g = f'나의 이름은 {name} 이고 나의 나이는 {age} 입니다'
print(g)

# 문자열 개수 세기 (Count)
a= "hobby"
print (a.count('b')) #a.count는 변수 a라는 곳에 count하는 것 b라는 글자가 몆개있는지 알려주는것

#위치 알려주기1 (find)
print (a.find('x'))

#문자열 삽입
h= ' , '.join('abcd')
print(h)

#공백 지우기
k= '   hi '
print(k.lstrip()) #왼쪽
print(k.rstrip()) #오른쪽
print(k.strip()) ##양쪽

#문자열바꾸기
print(b)
print(b.replace("Life", "your leg"))

#문자열 나누기
#split 함수는 공백 기준으로 나뉨 기준을 나눌려면  b.split()애서 ("")에 기준을 넣을것
l="a:b:c:d"
b= "Life is too short, You need Python"
print(l.split(":")) #문자열 나누기