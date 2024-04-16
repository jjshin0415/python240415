# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        # 멤버변수를 엑세스
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 버그(파이썬은 모호한 것보다는 명확한 것이 좋다)
        # print(strName) #전역변수 값 조회
        print(self.strName) #멤버변수 값 조회
d = DemoString()
d.set("First Message")
d.print()
