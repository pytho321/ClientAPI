import requests
import json
URL = "http://127.0.0.1:8000/employeeAPI/"

def getallData():
    data={}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbyID():
    id = int(input('Enter ID to search for a record: '))
    data={'id': id}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName                Email               Designation               Salary\tCity               State")  
    for i in data:
        print("%d\t%-20s%-20s%-20s%d\t%-20s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbyname():
    name = input('Enter Employee Name to search for a record: ')
    data={'name': name}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbyemail():
    email = input('Enter Employee Email to search for a record: ')
    data={'email': email}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbydsg():
    dsg = input('Enter Employee Designation to search for a record: ')
    data={'dsg': dsg}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbysalary():
    salary = int(input('Enter Employee Salary to search for a record: '))
    data={'salary': salary}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation               Salary\tCity               State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbycity():
    city = input('Enter Employee City to search for a record: ')
    data={'city': city}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def searchbystate():
    state = int(input('Enter Employee State to search for a record: '))
    data={'state': state}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print("id\tName               Email               Designation          Salary\tCity          State")  
    for i in data:
        print("%d\t%-20s%-20s%-15s%d\t%-15s%s"%(i.get('id'),i.get('name'), i.get('email'),i.get('dsg'),i.get('salary'),i.get('city'),i.get('state'))) 
def create():
    data={}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    num = data[-1:]
    num = num[0].get('id')
    name = input('Enter the name to record: ')
    email = input('Enter the email to record: ')
    dsg = input('Enter the designation to record: ')
    salary = input('Enter the salary to record: ')
    city = input('Enter the city to record: ')
    state = input('Enter the state to record: ')
    data = {
        "id": num+1,
        'name': name,
        'email': email,
        'dsg': dsg,
        'salary': salary,
        'city': city,
        'state': state,
    }
    jsonData = json.dumps(data)
    r = requests.post(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print(data['msg'])
def edit():
    id = int(input('Enter ID to search for a record: '))
    data={'id': id}
    jsonData = json.dumps(data)
    r=requests.get(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    empdata = json.loads(rawData)
    print(' PRess Enter if you do not want to update any data')
    
    name = input('Enter the name to record: ')
    email = input('Enter the email to record: ')
    dsg = input('Enter the designation to record: ')
    salary = input('Enter the salary to record: ')
    city = input('Enter the city to record: ')
    state = input('Enter the state to record: ')
    if(name==""):
        name = empdata[0].get('name')
    if(email==""):
        email = empdata[0].get('email')
    if(dsg==""):
        dsg = empdata[0].get('dsg')
    if(salary==""):
        salary = empdata[0].get('salary')
    if(city==""):
        city = empdata[0].get('city')
    if(state==""):
        state = empdata[0].get('state')
    data = {
        "id": id,
        'name': name,
        'email': email,
        'dsg': dsg,
        'salary': salary,
        'city': city,
        'state': state,
    }
    jsonData = json.dumps(data)
    r = requests.put(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print(data['msg'])
def delete():
    id = int(input('Enter ID to search for a record: '))
    data={'id': id}
    jsonData = json.dumps(data)
    r=requests.delete(url=URL, data=jsonData)
    rawData = r.json()
    rawData = json.dumps(rawData)
    data = json.loads(rawData)
    print(data['msg'])


while(True):
    print('\n\n\n1.Create New record: \n2.Edit the existing record: \n3.Delete the Existing record: \n4.Search By Id \n5.Search by name: \n6.Search by Email: \n7.Search by Designation: \n8.Search by Salary: \n9.Search by City: \n10.Search by State: \n11.Get all the Data:')
    ch = input()
    if(ch=='1'):
        create()
    elif(ch=='2'):
        edit()
    elif(ch=='3'):
        delete()
    elif(ch=='4'):
        searchbyID()
    elif(ch=='5'):
        searchbyname()
    elif(ch=='6'):
        searchbyemail()
    elif(ch=='7'):
        searchbydsg()
    elif(ch=='8'):
        searchbysalary()
    elif(ch=='9'):
        searchbycity()
    elif(ch=='10'):
        searchbystate()
    elif(ch=='11'):
        getallData()
    elif(ch=='12'):
        break
    else:
        print('Invalid Choice')

