
def read_phone_book(phone_book_file):
      with open(phone_book_file, "r", encoding='UTF-8') as file:
        reader = file.readlines()
        for row in reader:
            print(row)
    
def save_phone_book(phone_book_file, phone_book):
    with open(phone_book_file, 'w', newline="", encoding='UTF-8') as file:
        for entry in phone_book:
            file.write(entry)
    print()
    
def search_phone_book(phone_book, key):
    result = []
    for entry in phone_book:
        if key in entry:
            result.append(entry)
    return result

def change_phone_book(phone_book, key):
    for i, entry in enumerate(phone_book):
        if key in entry:
            new_entry = input("Изменить контакт: ")
            phone_book[i] = new_entry.split(";")
            break

def delete_phone_book(phone_book, key):
    for i, entry in enumerate(phone_book):
        if key in entry:
            del phone_book[i]
            break

def add_phone_book_entry(phone_book_file):
    phone_book = []
    with open(phone_book_file, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        
    for contact in data:
        new_contact = contact.strip().split(';')
    new_contact = {'name': new_contact[0],
                    'phone': new_contact[1],
                'comment': new_contact[2]}
    phone_book.append(new_contact)

    #-Д- добавления нового экземпляра в словарь 
    phone_book.append({'name': 'Антон Пальчиков',
                        'phone': '999-999',
                        'comment': 'Друг Ноггано'})
    print(phone_book)
    # file = open(phone_book_file, 'w', encoding='UTF-8')
    # # file.write(phone_book)
    # file.close()
    # with open(phone_book_file, 'w', encoding='UTF-8') as file:
    #     file.write(phone_book)
