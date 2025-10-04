# Question 2 – Mutable vs Immutable (Data Structures & Variables)

my_tuple = (10, 20, 30)
try:
    my_tuple[1] = 99  
except TypeError as e:
    print("Error:", e)



my_list = [10, 20, 30]
my_list[1] = 99
print(my_list)


my_dict = {"name": "Juanid", "age": 20}
my_dict["age"] = 22
print(my_dict)


new_tuple = ([1,2,3], [4,5,6])
new_tuple[0][1] = 10
print(new_tuple)

# Question 3 – User Information Dictionary (Validation + Logic)

name = input("Enter name: ")

while True:
    age = int(input("Enter age: "))      
    if 0 < age < 100: break
    

while True:
    email = input("Enter email: ")
    if "@" in email and "." in email and email[0].isalnum() and email[-1].isalnum():
        break

while True:
    fav = int(input("Enter favorite number (1-100): "))
    if 1 <= fav <= 100: break

user = {"name": name, "age": age, "email": email, "fav": fav}
print(f"Welcome {user['name']}! Your account has been registered with email {user['email']}.")


# Question 4 – Cinema Ticketing System
def calc_price(age, stu, wknd):
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
    if age < 12:
        price = 5
    elif age <= 17:
        price = 8
    elif age <= 59:
        price = 12
    else:
        price = 6
    if stu and age > 12:
        price *= 0.8
    if wknd:
        price += 2
    return price

n = int(input("Enter number of customers: "))
cust = []
for i in range(n):
    print(f"Custmer {i +1}:")
    age = int(input("Enter age: "))
    stu = input("Student (yes/no): ").lower() == "yes"
    wknd = input("Weekend (yes/no): ").lower() == "yes"
    p = calc_price(age, stu, wknd)
    cust.append({"age": age, "student": stu, "weekend": wknd, "price": p})

for c in cust:
    print("Age:", c["age"], "Student:", c["student"], "Weekend:", c["weekend"], "Price:", round(c["price"], 2))

total = sum(c["price"] for c in cust)
if n >= 4:
    total *= 0.9
print("Total:", round(total, 2))

max_c = max(cust, key=lambda x: x["price"])
min_c = min(cust, key=lambda x: x["price"])
print("Highest:", round(max_c["price"], 2))
print("Lowest:", round(min_c["price"], 2))


#Question 5 – Weather Alert System 

def weather_alert(temp_c, cond):
    if temp_c < 0 and cond == "snowy":
        msg = "Heavy snow alert! Stay indoors."
    elif temp_c > 35 and cond == "sunny":
        msg = "Heatwave warning! Stay hydrated."
    elif cond == "rainy" and temp_c < 15:
        msg = "Cold rain alert! Wear warm clothes."
    else:
        msg = "Normal weather conditions."
    
    temp_f = (temp_c * 9/5) + 32
    temp_k = temp_c + 273.15
    return msg, round(temp_f, 2), round(temp_k, 2)

t = float(input("Enter temperature in Celsius: "))
c = input("Enter condition (sunny, rainy, snowy, etc.): ").lower()

m, f, k = weather_alert(t, c)
print("Msg:", m)
print("Fahrenheit: ", f)
print("Kelvin: ", k)


### Question 6 – Sales Analytics (Max, Min & Median)

import statistics

def analyze_sales(sales_list):
    high = max(sales_list)
    low = min(sales_list)
    mid = statistics.median(sales_list)
    return high, low, mid
while True:
    n = int(input("Enter number of days: "))
    if n >= 5: break
        
    elif n < 5: print("Need at least 5")

sales = []
for i in range(n):
    val = float(input(f"Enter sale (Day {i+1}): "))
    sales.append(val)
    
h, l, m = analyze_sales(sales)
print("Highest sales day:", h)
print("Lowest sales day:", l)
print("Median sales:", m)


# Question 7 – E-commerce Inventory Management

def update_inventory(inv, item, qty):
    if item not in inv:
        print("Item not found")
    else:
        if inv[item] + qty < 0:
            print("Not enough stock for", item)
        else:
            inv[item] += qty
    return inv

inv = {"pen":10, "book":8, "bag":5, "marker":12, "register":6}


print("Items:", inv)

for i in range(3):
    it = input("Enter item: ")
    q = int(input("Enter qty: "))
    inv = update_inventory(inv, it, -q)

print("Inv:", inv)
max_item = max(inv, key=inv.get)
min_item = min(inv, key=inv.get)
print("Max:", max_item, inv[max_item])
print("Min:", min_item, inv[min_item])
