'''atleast 8 characteristics
create a loop check each character then check condition
condition minimum8,1upper,1lower,1number(digit)'''
#madam Explaining
password=input("Enter the password : ")
u=0
l=0
d=0
if(len(password)<8):
   print("Try Again")
else:
    for i in password:
        if i.isupper():
            u=True           
        elif i.islower():
            l=True
        elif i.isdigit():
            d=True
    if u and l and d :
        print("Strong password")
    else:
        print("weak password")
            
