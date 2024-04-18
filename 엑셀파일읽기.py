import openpyxl

# 파일 경로
file_path = 'C:\\work\\products.xlsx'

# 워크북 열기
wb = openpyxl.load_workbook(file_path)

# 활성 시트 선택
ws = wb.active

# 모든 행을 순회하며 데이터 읽기
for row in ws.iter_rows(min_row=2, values_only=True):  # 헤더를 제외하고 읽기 위해 min_row=2 설정
    product_id, product_name, quantity, price = row
    print(f"제품ID: {product_id}, 제품명: {product_name}, 수량: {quantity}, 가격: {price}")

# 워크북 닫기
wb.close()
