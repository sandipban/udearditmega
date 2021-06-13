student_grade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
grade_byname = {'ram': 8.8, 'shyam': 8.8, 'jadu': 8.8}
number_sum = sum(student_grade)
number_of_items = len(student_grade)
average = number_sum / number_of_items
print(average)
print(max(student_grade))
print(student_grade.count(10.0))
username = 'sandip1'
print (username.title())
byname_values = grade_byname.values()
avg = sum(byname_values)/ len(byname_values)
print(avg)
print (grade_byname.values(), grade_byname.keys())
