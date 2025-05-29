# 1. Update the birthdays.csv
# done
# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
import datetime
import smtplib
import random

df = pd.read_csv("birthdays.csv")

now = datetime.datetime.now()
current_date_with_year = now.date()

current_day_data = now.strftime("%d")
current_month_data = now.strftime("%m")

df['month'] = df['month'].astype(str)
df['day'] = df['day'].astype(str)

mask = (df['month'] == current_month_data) & (df['day'] == current_day_data)

matching_rows = df[mask]
if matching_rows:
    my_email = "pyt5691@gmail.com"
    password = "hjsjectcfullypen"
    person_name = matching_rows['name']
    person_email = matching_rows['email']

    with open(file='letter_templates/letter_1.txt') as l1:
        lines = l1.readlines()
        lines[0] = f" Hey {person_name}"
    with open(file='letter_templates/letter_1.txt' 'w') as l11:
        l11.write("".join(lines))

    with open(file='letter_templates/letter_2.txt') as l2:
        lines = l2.readlines()
        lines[0] = f" Hey {person_name}"
    with open(file='letter_templates/letter_2.txt' 'w') as l22:
        l22.write("".join(lines))

    with open(file='letter_templates/letter_1.txt') as l3:
        lines = l3.readlines()
        lines[0] = f" Hey {person_name}"
    with open(file='letter_templates/letter_1.txt' 'w') as l33:
        l33.write("".join(lines))



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person_email,
                            msg=f"Subject:HAPPY BIRTHDAY \n\n{random_quote_of_day}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
