# 하위 디렉토리 검색하기

import os

# def search(dir_name):
#     # os.listdir은 해당 디렉토리에 있는 파일의 리스트를 구할 수 있음
#     filename_list = os.listdir(dir_name)
#     for file_name in filename_list:
#         full_filename = os.path.join(dir_name, file_name)
#         # .py만 출력
#         temp = os.path.splitext(full_filename)[-1]
#         if temp == '.py':
#             print(full_filename)

# search("c:/")


# 하위 디렉토리까지 검색 할 수 있게
def search(dir_name):
    try:
        file_list = os.listdir(dir_name)

        for file_name in file_list:
            full_filename = os.path.join(dir_name, file_name)

            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                temp = os.path.splitext(full_filename)[-1]
                if temp == '.py':
                    print(full_filename)
    
    except PermissionError:
        pass

search("c:/")