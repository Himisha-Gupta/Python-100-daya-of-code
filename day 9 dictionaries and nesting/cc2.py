Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}
print(type(Employee))
print("printing Employee data .... ")
print(f'Name : {Employee["Name"]}')
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])

print(Employee.get("Name"))


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


car["color"] = "white"

print(car['brand'])
print(car.items())