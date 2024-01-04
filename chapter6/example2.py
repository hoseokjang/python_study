# 게시판 페이징 예제
# 총 페이지 수 = (총 게시물 수 / 한 페이지 당 보여 줄 개수) + 1

def get_total_page(total_num, pageSize):
    if total_num % pageSize == 0:
        return total_num // pageSize
    else: return total_num // pageSize + 1

# print(get_total_page(100, 20))
# print(get_total_page(5521, 100))