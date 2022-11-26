# formating an integer to hexadecimal,octadesimal and binary and printing them together
def print_formatted(number):
    length = len(str(bin(number))[2:len(str(bin(number)))])+1

    for x in range(1,number+1):
        x1 = str(x)
        x2 = str(oct(x))[2:len(oct(x))]
        x3 = (str(hex(x))[2:len(hex(x))]).upper()
        x4 = str(bin(x))[2:len(bin(x))]
        
        print((length-len(x1))*" "+x1+(length-len(x2))*" "+x2+(length-len(x3))*" "+x3+(length-len(x4))*" "+x4)


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)