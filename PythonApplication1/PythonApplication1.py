def input_func(a):
    if a != "":
        try:
            float(a)
            if a.isdigit() is False:
                a = float(a)
                if a >= 0:
                    return a
                print("It's negative.")
            else:
                print("It's int.")
        except:
            a = list(a)
            b=len(a)
            for i in range(b):
                for j in range(b):
                    if 'a' <= a[j] <= "z" or 'A' <= a[j] <='Z':
                        if a[j]=='a' or a[j]=='e' or a[j]=='i' or a[j]=='o' or a[j]=='u':
                            print(a[j],"- this isn't consonant letter")
                            a.pop(j)
                            b=len(a)
                            break   
                        else:
                            if a[j].isupper():
                                print(a[j],"- this is up register")
                                a.pop(j)
                                b=len(a)
                                break
                    else:
                        a.pop(j)
                        b=len(a)
                        print(a[j],"- this is not english word")
                        break
            if b==0:
                return None
            return "".join(a)
    else:
        print("Empty string.")

def calculate(a):
    if type(a[0]) is float:
        return min(a)
    elif type(a[0]) is str:
        return len(a)
    
def decorator(spisok):
    a = calculate(spisok)
    if type(a) is float:
        print("This is work with float numbers:")
        print(len(spisok))
    else:
        print("This is work with string:")
        count=0
        for i in range(a):
            if count<2:
                a[j].upper()
                count+=1
            else:
                count=0  
        print(spisok)
    return a



while 1:
    print("Enter: ")
    a = input()
    if a=="end":
        exit
    spisok = []
    a = input_func(a)
    if a != None:
        spisok.append(a)
        break
while 1:
    print(spisok)
    print("Enter: ")
    a = input()
    if a=="end":
        break
    a = input_func(a)
    if a != None:
        if type(spisok[0]) is float and type(a) is float:
            print(a)
            spisok.append(a)
        elif type(spisok[0]) is str and type(a[0]) is str:
            spisok.append(a)
        else:
            print("Continue enter same type, please")
            

    