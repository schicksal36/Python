#디셔너리는 {}로 하고 ,콤마로 키와 값을 구분
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(type(dic))

#디셔너리 삭제
#변형가능 한거는 쓸수 없음  중복은 안됨

a= {1: 'a', 2 : 'b','name' : 'pey', 3:[1, 2, 3]}

print(a)
print(a.keys())
#리스트 변환
print(a.values())
#키값 만 불러옴
print(a.items()) 
#키별로 괄호를 해줌
print('namec' in a)

#집합관련
s1= set([1,2,3]) 
#set으로 하고 ()하면 소괄호 함없이 {}하면 집합임

print(type(s1))s