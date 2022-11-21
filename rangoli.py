import time

def print_rangoli(size):
    string = "abcdefghijklmnopqrstuvwxyz"
    list = []
    for i in range(size):
        x = string[size-1-i:size]
        for char in x[::-1]:
            
            list.append(char)
            
        for char in x[1:len(x)]:
            list.append(char)
            
        #print(list)
        x = "-".join(list)
        
        print(int((4*size-3-len(x))/2)*"-"+x+int((4*size-3-len(x))/2)*"-")

        
        
        list.clear()
        x = ""
    for i in range(size-1): #i = 0,1,2,3,4
        y = string[i+1:size]
        for char in y[::-1]:
            list.append(char)
        for char in y[1:len(y)]:
            list.append(char)
            
        #print(list)
        x = "-".join(list)
        
        
        
        print(int((4*size-3-len(x))/2)*"-"+x+int((4*size-3-len(x))/2)*"-")        
        
        
        list.clear()
        x = ""
        
        
        
        
    
if __name__ == '__main__':
    while 1:
        n = int(input("sayı giriniz:"))
        print_rangoli(n)
        time.sleep(1)