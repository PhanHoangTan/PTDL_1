import Rectangle

fr = open('input.db',mode = 'r',encoding='utf-8')
listRectangle = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    cr = float(ds[0])
    cd = float(ds[1])
    hcn = Rectangle.Rectangle(cr, cd)
    listRectangle.append(hcn)
fr.close()
#Ghi dữ liệu từ listRectangle vào file output.db
fw = open('output.db',mode = 'w',encoding='utf-8')
for item in listRectangle:
    fw.write(f'{item.width}-{item.length}-{item.area()}-{item.perimeter()}\n')
fw.close()

import Rectangle as rect
menu = {
    1:'1.Đọc dữ liệu từ file input.db',
    2:'2.Thêm mới hình chữ nhật',
    3:'3.Hiển thị danh sách hình chữ nhật',
    4:'4.Lưu danh sách hình chữ nhật vào file output.db',
    'Other':'Thoát chương trình'
}

def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])

while(True):
    print_menu()
    choice = 0
    try:
        choice = int(input('Chọn chức năng: '))
    except:
        print('Nhập sai định dạng, hãy nhập lại.....')
        continue
    if choice == 1:
        fr = open('input.db',mode = 'r',encoding='utf-8')
        dsHCN = []
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            cr = float(ds[0])
            cd = float(ds[1])
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        fr.close()
    elif choice == 2:
        cr = float(input('Nhập chiều rộng: '))
        cd = float(input('Nhập chiều dài: '))
        if cr <= 0 or cd <= 0:
            print('Chiều rộng hoặc chiều dài không hợp lệ')
        elif cd > cr:
            hcn = rect.Rectangle(cr, cd)
            dsHCN.append(hcn)
        else:
            print("Chiều dài phải lớn hơn chiều rộng. Vui lòng nhập lại.")
    elif choice == 3:
        for item in dsHCN:
            item.display()
    elif choice == 4:
        fw = open('output.db',mode = 'w',encoding='utf-8')
        for item in dsHCN:
            fw.write(f'{item.width}-{item.length}-{item.area()}-{item.perimeter()}\n')
        fw.close()
    else:
        print('Thoát chương trình')
        break