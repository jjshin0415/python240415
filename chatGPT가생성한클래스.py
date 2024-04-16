class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        # 사람의 정보를 출력하는 메서드입니다.
        print("ID:", self.id)  # ID 출력
        print("Name:", self.name)  # 이름 출력


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        # 매니저의 정보를 출력하는 메서드입니다.
        super().printInfo()  # 부모 클래스의 printInfo() 메서드 호출
        print("Title:", self.title)  # 직책 출력


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        # 직원의 정보를 출력하는 메서드입니다.
        super().printInfo()  # 부모 클래스의 printInfo() 메서드 호출
        print("Skill:", self.skill)  # 기술 출력


# 추가적인 테스트 케이스
# 11. 타이틀을 포함한 매니저 클래스 테스트
print("\n테스트 11:")
manager5 = Manager(11, "Sophie Brown", "Senior Manager")
manager5.printInfo()

# 12. 스킬을 포함한 직원 클래스 테스트
print("\n테스트 12:")
employee4 = Employee(12, "Jack Wilson", "Machine Learning")
employee4.printInfo()

# 13. 타이틀과 Person 메서드를 포함한 매니저 클래스 테스트
print("\n테스트 13:")
manager6 = Manager(13, "Emma Johnson", "Manager")
manager6.printInfo()

# 14. 스킬과 Person 메서드를 포함한 직원 클래스 테스트
print("\n테스트 14:")
employee5 = Employee(14, "James Anderson", "Web Development")
employee5.printInfo()

# 15. 타이틀과 Employee 메서드를 포함한 매니저 클래스 테스트
print("\n테스트 15:")
manager7 = Manager(15, "Olivia Taylor", "Senior Manager")
manager7.printInfo()

# 16. 스킬과 Manager 메서드를 포함한 직원 클래스 테스트
print("\n테스트 16:")
employee6 = Employee(16, "William Martinez", "Data Science")
employee6.printInfo()

# 17. 타이틀을 포함한 Person 클래스 테스트
print("\n테스트 17:")
person4 = Person(17, "Abigail Johnson")
person4.printInfo()

# 18. 스킬을 포함한 Person 클래스 테스트
print("\n테스트 18:")
person5 = Person(18, "Ethan Thompson")
person5.printInfo()

# 19. 타이틀과 스킬을 포함한 Person 클래스 테스트
print("\n테스트 19:")
person6 = Person(19, "Isabella Harris")
person6.printInfo()

# 20. 타이틀과 스킬을 포함한 매니저 클래스 테스트
print("\n테스트 20:")
manager8 = Manager(20, "Alexander Wright", "Manager")
manager8.printInfo()
