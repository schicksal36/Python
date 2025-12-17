odd = [1,3,5,7,9]
print(odd)
az= [1,2,3, ['a','b','c']]
print(az[1] + odd[2])
print(az[3])


#리스트

#수정
a= [1,2,3]
a[2] = 4 #3을 4로 바꾸겠다
del a[1] #1을 없애겠다. del이 delete
# 추가(append)
a.append(7) #7을 추가 하겠다.
a.append([5.6]) #[5.6]을 추가 하겠다.
print(a)
#정렬(sort)
b=[1,4,5,6,2,3]
b.sort()
#내림차순 정렬

#삭제
b.remove(6)
print(b)

#리스트요소 쓰기
print(b.pop(3))


#리스트 확장
c = [1,2,3]
c.extend([4,5]) 
#append와 차이 
#append는 그대로 출력
#extend는 []없이 함
print(c)
