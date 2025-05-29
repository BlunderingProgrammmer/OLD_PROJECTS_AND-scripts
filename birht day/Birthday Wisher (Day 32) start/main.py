import smtplib
import datetime as dt
import random

quotes_list = open('quotes.txt').read().splitlines()
print(quotes_list)
random_quote_of_day = random.choice(quotes_list)

my_email = "pyt5691@gmail.com"
password = "hjsjectcfullypen"


with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="dofihe2719@em2lab.com",
                        msg=f"Subject: monday quotes \n\n{random_quote_of_day}")

