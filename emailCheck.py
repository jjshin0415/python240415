# import re

# def is_valid_email(email):
#     # Regular expression for basic email validation
#     # r: raw string notation
#     regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     # 정규표현식을 사용해서 이메일주소 체크 
#     if re.match(regex, email):
#         return True
#     else:
#         return False

# # Test cases
# emails = ["example@email.com", "invalid_email", "anotherexample.com", "no@domain"]
# for email in emails:
#     print(f"{email}: {is_valid_email(email)}")

import re

def is_valid_email(email):
    # 기본 이메일 유효성을 위한 정규 표현식
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False

# 샘플 이메일 주소들
emails = [
    "user@example.com",                  # 올바른 형식
    "first.last@example.com",            # 올바른 형식
    "user123@example.com",               # 올바른 형식
    "user+tag@example.com",              # 올바른 형식
    "invalid_email",                     # 잘못된 형식
    "anotherexample.com",                # 잘못된 형식
    "no@domain",                         # 잘못된 형식
    "john.doe@example.co.uk",            # 올바른 형식
    "user_name123@example-domain.com",   # 올바른 형식
    "user@example_domain.com"            # 올바른 형식
]

# 각 이메일 주소를 테스트하고 결과를 출력
for email in emails:
    print(f"{email}: {is_valid_email(email)}")

