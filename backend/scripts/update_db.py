import smtplib
import requests
from datetime import date

URL = 'https://serene-reaches-13440.herokuapp.com/api/update/'
r = requests.get(URL)
data = r.json()['data']

today = date.today().strftime("%B %d, %Y")

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("ajinkya.test.web@gmail.com", "nnbpprigytejnefr")
message = f'''\
From: ajinkya.test.web@gmail.com
To: noreply.progressor@gmail.com
Subject: Database Updated on - {today}
Users Updated - 

{data}'''

s.sendmail("ajinkya.test.web@gmail.com", "noreply.progressor@gmail.com", message)
s.quit()
