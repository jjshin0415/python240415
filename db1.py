#db1.py
import sqlite3

#일단 메모리에서 임시 저장
con = sqlite3.connect(":memory:")

#커서 객체
cur = con.cursor()

#테이블(자료구조) 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#1건입력
cur.execute("insert into PhoneBook values ('홍길동','010-222');")

#외부에서 입력 파라미터 처리
name = "전우치"
phoneNum = "010-333"
cur.execute("insert into PhoneBook values (?,?);",(name,phoneNum))

#검색
cur.execute("select * from PhoneBook;")

for row in cur:
     print(row)

