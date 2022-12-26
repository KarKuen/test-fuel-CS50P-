import sys

def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x, y = (fraction.split('/'))
    x = int(x)
    y = int(y)
    percentage = round(100 * (x / y))
    return(percentage)

def gauge(percentage):

    if percentage <= 1:
        percentage = 'E'
    elif percentage >= 99:
        percentage = 'F'

    if str(percentage).isnumeric():
        percentage = str(percentage) + '%'
    return(percentage)

if __name__ == '__main__':
    main()