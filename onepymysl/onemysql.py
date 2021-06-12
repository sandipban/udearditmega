import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

query1 = cursor.execute("SELECT Expression from Dictionary")
keys = [b[0] for b in cursor.fetchall()]


if results:
    for result in results:
        print(result[0])
elif len(get_close_matches(word, keys, cutoff = 0.8))> 0:
    yn = input('Do you want to mean \"%s\" instead ? Type Y for yes and N for no.' %get_close_matches(word, keys, cutoff = 0.8)[0].title() )
    yn = yn.lower()
    if yn == 'y':
        word = get_close_matches(word, keys, cutoff = 0.8)[0]
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = cursor.fetchall()
        for result in results:
            print(result[0])
    else:
        print('We could not suggest you more. Please recheck')

else:
    print("No word found!")