print("deneme")
print("Merhaba Dünya")
print("Firi'nin Evi")
print("""Merhaba
Dünya""")
print("Merhaba\nDünya")
print("Merhaba\tDünya")
print("Merhaba\t\t\tDünya")

mesaj="Merhaba Dünya"
print(mesaj)

mesaj1="nasılsın"
mesaj2="Firicim"
print(mesaj1+" "+mesaj2)
print(mesaj1[0])
print(mesaj2[0:5])
print(mesaj1[::2])
print(mesaj2[::3])
print(mesaj2[::-1])
print(mesaj1.upper())
movie="inception"
print(movie.upper())
mesaj1=mesaj1.upper()
print(mesaj1)
mesaj1=mesaj1.lower()
print(mesaj1)
mesaj1=mesaj1.capitalize()
print(mesaj1)
print(mesaj1.startswith("Na"))
print(mesaj2.startswith("fa"))
print(mesaj1.endswith("n"))
print(len(movie))
name="Firdevs"
age="45"
print("{} {} years old.")
print("{} is {} years old.".format(name,age))
print("My name is {}.".format(name))
print("{} {} dedi...".format(name, mesaj))
print(f"{name} {mesaj} diyordu..")

price=19.99
quantity=3
print(price)
print(type(price))
print(type(quantity))
total_coast=price*quantity
print(total_coast)
print("the total is {}".format(total_coast)) 

is_raining=True
print(is_raining==is_raining)
is_raining = True
print(is_raining)         
print(not is_raining)     
print(not not is_raining)

x = 7
y = 4
print(x > y)    
print(x < y)    
print(x == y)   
print(x != y)   

num_str="100"
print(type(num_str))
num_str=100
print(type(num_str))
num_str3=int(num_str)
num_str2=50
result=(num_str3+num_str2)
print("the result is {}".format(result)) 


