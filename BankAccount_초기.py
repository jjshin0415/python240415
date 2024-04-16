# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        # 멤버변수 초기화
        self.id = id
        self.name = name 
        self.balance = balance 
        # 멤버변수 초기화(이름 숨김)
        # self.__id = id
        # self.__name = name 
        # self.__balance = balance 
    def deposit(self, amount):
        # 입금
        self.balance += amount 
    def withdraw(self, amount):
        # 출금
        self.balance -= amount
    def __str__(self):
        # 현재 상태를 문자열로 출력
        return "{0} , {1} , {2}".format(self.id, \
            self.name, self.balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
print(account1)
account1.deposit(5000)
print(account1)
account1.withdraw(3000)
# account1.balance = 15000000 # 잔고가 숨김처리 안된 경우, 수정 가능
print(account1)

# 변수 숨김
# print(account1.__balance) # 숨김처리한 변수는 에러남: AttributeError: 'BankAccount' object has no attribute '__balance'