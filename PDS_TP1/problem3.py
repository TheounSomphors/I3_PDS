def celsius_to_fahrenheit(celsius,round_to=1):
    Fahrenheit= celsius*9/5 + 32
    return Fahrenheit
print("",celsius_to_fahrenheit(23),"F")

def  fahrenheit_to_celsius(Fahrenheit,round_to=1):
    Celsius= Fahrenheit-32*5/9
    return Celsius
print(fahrenheit_to_celsius(25),"C")
print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print(f"37 °C = {celsius_to_fahrenheit(37)} °F -> back = {fahrenheit_to_celsius(celsius_to_fahrenheit(37))} °C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))
print(celsius_to_fahrenheit(37,round_to=3))
print(celsius_to_fahrenheit(30,round_to=3))