class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    # 명시적으로 부모 초기화  메서드 호출
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID

    # 메서드 재정의
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201122")
print(p.__dict__)
print(s.__dict__)

p.printInfo()
s.printInfo()



