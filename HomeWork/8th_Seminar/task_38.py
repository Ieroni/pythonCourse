# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных
"""
1. Открыть файл
2. Сохранить файл
3. Посмотреть все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
"""
print('Task #38')
from task_38_libr import read_phone_book, save_phone_book, search_phone_book,\
                         change_phone_book, delete_phone_book, add_phone_book_entry
import os

print('загрузите файл')
phone_book_file = '8th_Seminar\sample.txt'
read_phone_book(phone_book_file)
add_phone_book_entry(phone_book_file)





# def main():
#     phone_book = []

#     # Read phone book from file
#     try:
#         with open(phone_book_file, "r", encoding='UTF-8') as file:
#             reader = file.readlines()
#             # for row in reader:
#             #     phone_book.append(row)
#             for contact in reader:
#                 new_contact = contact.strip().split(';')
#             new_contact = {'name': new_contact[0],
#                           'phone': new_contact[1],
#                         'comment': new_contact[2]}
#             phone_book.append(new_contact)
#     except FileNotFoundError:
#         pass

#     while True:
#         print("\nPhone book menu:")
#         print("1. Show phone book")
#         print("2. Search phone book")
#         print("3. Change phone book entry")
#         print("4. Delete phone book entry")
#         print("5. Add phone book entry")
#         print("6. Save and exit")
#         choice = input("Enter choice (1-6): ")

#         if choice == "1":
#             read_phone_book()
#         elif choice == "2":
#             key = input("Enter search key: ")
#             result = search_phone_book(phone_book, key)
#             for entry in result:
#                 print(entry)
#         elif choice == "3":
#             key = input("Enter entry to change: ")
#             change_phone_book(phone_book, key)
#         elif choice == "4":
#             key = input("Enter entry to delete: ")
#             delete_phone_book(phone_book, key)
#         elif choice == "5":
#             add_phone_book_entry(phone_book)
#             break
#         elif choice == "6":
#             save_phone_book(phone_book)
#             break

# main()
# if __name__ == "__main__":
#     main()
