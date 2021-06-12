# def foo(ch):
#     if len(ch)>= 8:
#         return True
#     return False


# print(foo('mypassword'))
# def weather(temp):
#     if temp <= 7:
#         return 'Cold'
#     return 'Warm'

# # print(weather(7))
# def weather(temp):
#     if temp > 25:
#         return 'Hot'
#     elif temp >= 15 :
#         return 'Warm'
#     return 'Cold'

# print(weather(2))
# name = 'sandip'
# message= f'hello {name}'
# print(message)

# This is problem solution for lecture 55

# def capitalizer(string):
#     qtn = ('How','When', 'What', 'Where', 'Who', 'Why')
#     capitalize = string.capitalize()
#     if capitalize.startswith(qtn):
#         return f'{capitalize}?'    
#     else:
#         return f'{capitalize}.'
# result = []

# while True:
#     user_input = input('Say something: ')
#     if user_input == 'end':
#         break
#     else:
#         result.append(capitalizer(user_input))
# print(' '.join(result))
# hunger = True
# boredom = False
# if hunger == True and boredom == True:
#     print("Let's order pizza!")
# else:
#     print("Let's wait until dinnertime.")

# Bonus code testing

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
# for pair in phone_numbers.items():
#     print("{} has as phone number {}".format(pair[0], pair[1]))

# for key, value in phone_numbers.items() :
#     print(f'{key} has a phone number {value}')

    
####################### File handling section practice. #########################
################ Exercise 48 ##################
# with open('bear.txt') as file:
#     content = file.read()[ : 91]

# with open('first.txt', 'a+') as file_one:
#     file_one.write(content)
#     file_one.seek(0)
#     content_one = file_one.read()
# print(content_one)

#################################### Exercise 49 ###############
# with open('bear.txt') as file_one:
#     content = file_one.read()
#     file_one.seek(0)

# with open('bear1.txt', 'a+') as content_one:
#     content_one.write(content)
#     content_one.seek(0)
#     display = content_one.read()
# print(display)
# ######################################################################

############################## Exercise 50 ###########################

with open('data.txt', 'a+') as multiplier:
    multiplier.seek(0)
    conten = multiplier.read()
    multiplier.seek(0)
    multiplier.write(2*conten)
    multiplier.seek(0)
    con_one = multiplier.read()
print(con_one)






    