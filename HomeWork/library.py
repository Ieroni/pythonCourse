# file = open(r'C:\Users\shelginskikh\Desktop\pythonCourse\HomeWork\sample.txt', 'r', encoding = 'UTF-8') # r - read, w -write, UTF-8 - русская кодировка
# data = file.readlines() #readline - чтение построчно
# file.close()

# print(data)

# for contact in data:
#     new_cont = contact.strip().split(';')   #strip - очищает от ненужных символов, split - разделение по символу
#     print(new_cont)    
    
"""
command: with ... as 

with open('HomeWork\8th_Seminar\sample.txt', 'a', encoding='UTF-8') as file:
    file.write(cont)

равнозначна строчкам: 

file = open('HomeWork\8th_Seminar\sample.txt', 'a', encoding='UTF-8')
file.write(cont)
file.close()
"""