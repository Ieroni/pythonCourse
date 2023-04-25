import csv
phone_book = []

file = open('HomeWork\8th_Seminar\sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
file.close()

#-М- функция создания структуры словаря и добавления словаря в список  
for contact in data:
    new_contact = contact.strip().split(';')
        
new_contact = {'name': new_contact[0],
              'phone': new_contact[1],
            'comment': new_contact[2]}
phone_book.append(new_contact)
print(phone_book)

#-Д- добавления нового экземпляра в словарь 
phone_book.append({'name': 'Антон Пальчиков',
                  'phone': '999-999',
                'comment': 'Друг Ноггано'})
print(phone_book)

#-М- для разбиения по строчкам
new_phone_book = []

for contact in phone_book:
    new_contact = ';'.join([values for values in contact.values()])   
new_phone_book.append(new_contact)
new_phone_book = '\n'.join(new_phone_book)

#-Д- добавления нового экземпляра в словарь 
file = open('HomeWork\8th_Seminar\sample.txt', 'w', encoding='UTF-8')
file.write(new_phone_book)
file.close()
print(new_phone_book)

#-Д- добавления нового экземпляра в словарь 
cont = '\nАнгелина Воробьева;456-654;Куртизанка'
with open('HomeWork\8th_Seminar\sample.txt', 'a', encoding='UTF-8') as file:
    file.write(cont)
    
# =====================================
# CSV part
# =====================================

# phone_book_file = 'HomeWork\8th_Seminar\sample.txt'
# reader = csv.reader(file)   

# def read_phone_book():
#     with open(phone_book_file, "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)

# def save_phone_book(phone_book):
#     with open(phone_book_file, "w", newline="") as file:
#         writer = csv.writer(file)
#         for entry in phone_book:
#             writer.writerow(entry)