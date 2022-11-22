#recursion ile octadesimal bulma, uzun ve kısa yol içerir
def long(x):
    list1 = []
    if x >= 8:
        while x >= 8:
            list1.append(x%8)
            x = x//8
            if x < 8:
                list1.append(x)

        list1.reverse()
        out = "".join(map(str,list1))
        return out
    
    else:
        return x

def short(x):
    return str(oct(int(x)))[2:len(str(oct(int(x))))]
    
if __name__ == "__main__":
    x = int(input())
    print(f"kısa fonksiyon sonucu: {short(x)}, uzun fonksiyon sonucu: {long(x)}")
 