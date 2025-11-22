import os

# with open('E:\Py\OOP\Instruments\data.txt', 'r') as file_data: #Менеджер контекста точно закроет файл 
#     data = file_data.read()

# print(data)

base_path = os.path.dirname(__file__)
file_path1 = os.path.join(base_path,'data.txt')
file_path2 = os.path.join(base_path,'data2.txt')

def read_file():
    with open('E:\Py\OOP\Instruments\data.txt', 'r') as file_data:
        for line in file_data.readlines():
 #Return - завершает функцию и возвращает значение. Yield приостанавливает выполнение функции,возвращая текущее значение 
 # и сохраняя состояние локальных При следующем вызове генератора выполнение продолжится с того места, где остановилось.          
            yield line  
 
for data_line in read_file():
    with open(file_path2, 'a') as new_data_file:
        data_line = data_line.replace('.','').replace('!','')
        new_data_file.write(data_line)           