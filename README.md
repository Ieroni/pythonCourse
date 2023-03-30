## Python Course

**Полезные команды**
- digits1 = string.digits+string.ascii_letters
- setDigits1 = set(' '.join([random.choice(string.digits) for _ in range(n)]))
- dict_count = {}
- for item in digits1:
    dict_count[item] = dict_count.get(item, 0) + 1 # поиск повторов в строке Digits1 и увеличение 
- for key in digits1:
    dict_count[key] = dict_count.get(key, 0) + 1
 
- punct = list(string.punctuation) + ['\n', '\t']
- for char in punct:
    text = text.replace(char, ' ')
text = text.lower().split()
print (*dict_count, sep='\n') - распечатать через новую строку

- text = [] 
for i in range(random.randint(10,20)):
    word = ''
    for j in range(random.randint(4,8)):
        word += random.choice(string.ascii_lowercase)
    text.append(word + str(random.choice([',', '!', '?', '.'])
                        if random.choice([0,1]) else ''))
print (' 'join.(text))

- choice = input('Больше (>) or less (<): ')
- if choice == '<' - функция предожения выбора знака
- def simple(number: int) -> bool:  - функция на входе принимает число в int, а на выходе в bool
- return x, y - два значения на выходе  
