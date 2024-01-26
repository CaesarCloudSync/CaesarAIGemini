import requests

response = requests.get("https://caesaraigemini-qqbn26mgpa-uc.a.run.app/sendmessage?message=what is your favourite food?",stream=True)
for i in response:
    print(i)