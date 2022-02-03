def celsius_to_fahrenheit(d):
    return round((d * 1.8) + 32, 2)

def fahrenheit_to_celcius(d):
    return round((d - 32) / 1.8, 2)

def miles_to_km(l):
    return round(1.609 * l, 3) 

def km_to_miles(l):
    return round(0.6215 * l, 3)

def mpg_to_l100(g):
    return round(235.215 / g, 2)

def l100_to_mpg(g):
    return 

if __name__ == '__main__':
    deg_celsius = 37.5
    deg_fahrenheit = 100
    l = 100
    g = 5

    print(f"Celsius : {deg_celsius : <15}\t Fahrenheit : {celsius_to_fahrenheit(deg_celsius) }")
    print(f"Fahrenheit : {deg_fahrenheit : <15}\t Celsius : {fahrenheit_to_celcius(deg_fahrenheit) }")
    print('\n')
    print(f'Miles : {l : <15}\t Km : {miles_to_km(l)}')
    print(f'Km : {l : <15}\t Miles : {km_to_miles(l)}')
    print('\n')
    print(f'L/100 : {g : <15}\t MpG : {mpg_to_l100(g)}')
    print(f'MpG : {mpg_to_l100(g) : <15}\t L/1OO : {g}')
