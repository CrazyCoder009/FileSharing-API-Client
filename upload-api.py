import json
import requests

filepath=input("Enter Upload file Path :")

serverf='https://apiv2.gofile.io/getServer'
r1=requests.get(serverf)
b_server=r1.json()
server=b_server['data']['server']
print("Best Server we have: "+server)
print("Server status code: "+str(r1.status_code))

print("-----------------------------------------------------")

url = 'https://'+server+'.gofile.io/uploadFile'
files = {'file': open(filepath, 'rb')}
response = requests.post(url, files=files)
r_server = response.json()
code=r_server['data']['code']
adminCode=r_server['data']['adminCode']
filename=r_server['data']['code']
status=r_server['status']
print("Server response code: "+str(response.status_code))
print("\nstatus:"+status+"\n", "code:"+code+"\n", "adminCode:"+adminCode+"\n", "filename:"+filename)
print("======================================================")
print("Visit Url: https://gofile.io/d/"+code)
print("======================================================")
