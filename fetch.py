import requests

#response = requests.get("https://caesaraigemini-qqbn26mgpa-uc.a.run.app/sendmessage?message=what is your favourite food?",stream=True)
#for i in response:
#    print(i)

url = 'http://127.0.0.1:8080/sendcsv'
form_data = {'message': 'Turn these questions into a statement. '}
files = {"file":open("Google Devices.csv")}
response = requests.post(url, data=form_data,files=files,stream=True)
for i in response:
    print(i)
