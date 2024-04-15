#디버깅
#교집합 리턴 함수
def intersect(prelist, postlist):  # 교집합 값을 리턴
    #지역변수
    result = []
    for x in prelist:
        if x in postlist and x not in result :
            result.append(x)
            return result

#호출
print(intersect("HAM","SPAM"))
