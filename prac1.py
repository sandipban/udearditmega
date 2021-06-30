# student_grade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
# grade_byname = {'ram': 8.8, 'shyam': 8.8, 'jadu': 8.8}
# number_sum = sum(student_grade)
# number_of_items = len(student_grade)
# average = number_sum / number_of_items
# print(average)
# print(max(student_grade))
# print(student_grade.count(10.0))
# username = 'sandip1'
# print (username.title())
# byname_values = grade_byname.values()
# avg = sum(byname_values)/ len(byname_values)
# print(avg)
# print (grade_byname.values(), grade_byname.keys())

# usr_input = input('Enter your name : ')
# def foo(name):
#     return(f'Hello, {name}')

# print(foo(usr_input.title()))


# colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
# for num in colors:
#     if isinstance(num, int):
#         if num > 50 :
#             print(num)

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"} #Looping through the dict.

# for key, value in phone_numbers.items():
#     print(f'{key} has the phone number : { value}')

# for num in phone_numbers.values():
#     print(f'00{num[1:]}')

## Ardit problem 60
    
# def txtmaker(txte):
#     qtn = ('Who','Which','What','When', 'Where', 'How')
#     txte = txte.capitalize()
#     if txte.startswith(qtn):
#         return(f'{txte}?')

#     else:
#         return(f'{txte}.')
    
# content = []
# while True :
#     usr_input = input('Say something :')
#     if usr_input == '\end':
#         break
#     else:
#         content.append(txtmaker(usr_input))

# print(' '.join(content)) 

original_str = "The quick brown rhino jumped over the extremely lazy fox"
word_lst = original_str.split(' ')
num_words_list = []
num_word = 0
for word in word_lst:
    num_word = len(word)
    num_words_list.append(num_word)
print(num_words_list)

'''Trolls are attacking your comment section! CODEWARS DASH BOARD CHALLANGE

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

'''