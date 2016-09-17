print("Hello, Django girls!")
if 3>2:
    print("it works!")
    if 5>2:
        print("5 is indeed greater than 2")
    else:
        print ("5 is not greatrer than 2")
name= "Sonja"
if name=="Hola":
    print ("Hey Hola")
elif name == "Sonja":
    print ("Hey Sonja!")
else:
    print ("Hey anonymous!")
volume=57
if volume<20:
    print("It's kinda quiet.")
elif  20<=volume<40:
    print("It's nice for background music")
elif 40<=volume<60:
    print("Perfect, i can hear all the details")
elif 60 <=volume<80:
    print ("Nice for parties")
elif 80<=volume<100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
if volume<20 or volume>80:
    volume= 50
    print("That's better")

def hi (name):
    if name=="Hola":
        print ("Hi Hola!")
    elif name == "Sonja":
        print ("Hi Sonja!")
    else:
        print("Hi anonymous!")
        hi()
        hi("Hola")
        hi ("Sonja")
def hi(name):
    print ("Hi"+name+"!")
hi("Hola")
girls= ["Rachel","Monica","Phoebe","Hola","You"]

for name in girls:

    print ("Hi"+name+"!")

girls=["Rachel", "Monica","Phoebe","hola","you"]
for name in girls:
    hi(name)
    print ("Next ")
    for i in range(1, 6):
        print(i)
