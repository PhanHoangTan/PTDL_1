import Rectangle as rect

menu_options ={
    1:'Thêm mới hình chữ nhật',
    2:'Hiển thị danh sách hình chữ nhật',
    3:'Tính tổng chu vi và diện tích các hình chữ nhật',
    4:'Hiển thị các hình chữ nhật có chu vi nhỏ nhất',
    'Other':'Thoát chương trình'
}

def print_menu():
    for key in menu_options:
        print(key,'--',menu_options[key])

#Khai báo biến lưu trữ những hình chữ nhật
dsHCN = []

while(True):
    print_menu()
    useChoice = 0
    try:
        useChoice = int(input('Chọn chức năng: '))
    except :
       print('Nhập sai định dạng, hãy nhập lại.....')
       continue
    #Check what was entered and act accordingly
    if useChoice == 1:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        if cr <= 0 or cd <= 0:
            print('Chiều rộng hoặc chiều dài không hợp lệ')
        elif cd > cr :
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        else:
            print("Chiều dài phải lớn hơn chiều rộng. Vui lòng nhập lại.")
       
    elif useChoice == 2:
        for item in dsHCN:
            item.display()
    elif useChoice == 3:
        dientich = 0.0
        for item in dsHCN:
            dientich += item.area()
        print('Tổng diện tích các hình chữ nhật là: ', dientich)
    elif useChoice == 4:
        if dsHCN.count == 0:
            print('Danh sách rỗng')
        else:
            chuvinn = dsHCN[0].perimeter()
            for item in dsHCN:
                if item.perimeter() < chuvinn:
                    chuvinn = item.perimeter()
            for item in dsHCN:
                if item.perimeter() == chuvinn:
                    item.display()
    else:
        print('Thoát chương trình')
        break
    
