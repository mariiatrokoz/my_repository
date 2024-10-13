# 12.10.24 #1

t = int(input('Enter a T-value: '))
unit = int(input('Press 1 for Celsius and 2 for Fahrenheit: '))

def converter(t, unit):
    if unit == 1:  # Celsius to Fahrenheit
        output = str(t) + '°C is ' + str(9 * t / 5 + 32) + '°F'
    elif unit == 2:  # Fahrenheit to Celsius
        output = str(t) + '°F is ' + str((t - 32) * 5 / 9) + '°C'
    else:
        output = 'Sorry, only numbers 1 or 2 are allowed.'
    return output

output = converter(t, unit)
print(output)

