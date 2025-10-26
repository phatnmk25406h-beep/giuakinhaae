import pandas as pd
import random
x=input("nhập file excel vào")
data_frame = pd.read_excel(f"{x}") # luc này mặc định header =0 là hàng tiêu đề nên nó sẽ không xuất dữ liệu.
#data_frame là một biến gán cấu trúc dữ liệu kia vào
list_of_list = data_frame.values.tolist()  #tạo ra một list of list [] khác với list of tuple () nhưng cách truy xuất vẫn giống nhau
#muốn đọc dc file excel phải: pip install openpyxl, pip install pandas và đặc biệt khi gọi hàm thì không được đặt tên file giống hàm
# vòng lặp giúp người học học tới khi thuộc thì thôi
while len(list_of_list)>0: #khi ht từ vựng thì danh sách rỗng thì len() danh sách sẽ =0
    randomlist = random.choice(list_of_list) #tạo một bien chứa tập hợp các list được random
    m=input(f"{randomlist[0]}: ") # nhập tiếng viet sao cho đúng vs tiếng anh ( phần kiểm tra bài cũ)
    if m==randomlist[1]:  #dò xem nếu đúng thì remove, còn k thì quay lên trên dò bài tiếp
        list_of_list.remove(randomlist)
print(list_of_list)
