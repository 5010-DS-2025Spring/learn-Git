
year = int(inoput("Please input year:"))

if year % 100 != 0 and year % 4 == 0:
    leap_year = True
elif year % 400 == 0: 
    leap_year = True

print(leap_year)



def conversion():
    while True:
        Fahrenheit = input("Pleaster enter Fahrenheit or 'n' to exit")
        if Fahrenheit == 'n':
            
        else:
            try:
                Fahrenheit = int(Fahrenheit)
                Celsius = (Fahrenheit - 32) * 5 / 9
                print(f"{Fahrenheit} is {Celsius} in Celsius.")
            except:
                print("Input error: Please inpout integer or float or 'n' to exit")





    