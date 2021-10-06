def say_hello(person1, person2="Dad"):
    print("Hello " + person1+ ", "+ person2+" is waiting for you")

def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32))/ 9
    return celsius

#print ("Celsius: ", round(fahr2celsius(100),2))
#print ("Kelvin: ", round(fahr2celsius(100)+ 273.5 ,2))

say_hello("Patrick", 'Kendra')
say_hello("Me")