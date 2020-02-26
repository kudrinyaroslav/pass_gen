"""
получаем список пользователей
делаем список из пользователей
по количеству пользователей в списке делаем столько же паролей
делаем словарь пользователь пароль
"""
import random
#library for work with excel
import xlrd, xlwt



# получаем список пользователей
def get_user_list(file):
    with open(file, 'r', encoding='utf-16') as f:
        x = f.read()
    return x

# генерируем список из пользователей
def gen_user_list(user_list):
    user_list = user_list.split('\n')
    return user_list

# генерируем пароль
def pass_gen():
    passw = ''
    for i in range(length):
        passw += random.choice(chars)
    return passw

# записываем данные в файл
def write_to_file(user_dict, path):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    j = 0
    for i in user_dict:
        ws.write(j, 0, user_dict[i])
        ws.write(j, 1, i)
        j += 1
    wb.save()
    

if __name__ == '__main__':
    # настройки
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 8
    file = 'C:\\folder_structure\\Projects\\pass_gen\\user_list.txt'
    path = 'C:\\folder_structure\\Projects\\pass_gen\\xl.xls'

    user_list = get_user_list(file)
    user_list = gen_user_list(user_list)
    user_dict = dict()
    for i in user_list:
        passw = pass_gen()
        user_dict[i] = passw
    
    write_to_file(user_dict, path)
    



