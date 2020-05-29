print("*****************")
print("      shop       ")
print("*****************")
print("1.show all products\n 2.buy product\n 3.add product\n 4.exit\n")
r=int(input("enter the option: "))
print("\n")
sno=["sno",1,2,3]
product=["product","phone","charger","usb"]
stock=["stock",20,40,30]
price=["stock",200,300,100]
n=4
choice='Y'
while(choice=='Y'):
        if(r==1):
            for i in range(len(sno)):
               print(sno[i],product[i],stock[i],price[i],sep='\t') 
        elif(r==2):
            for i in range(len(sno)):
                 print(sno[i],product[i],stock[i],price[i],sep='\t') 
            a=input("\n enter the product you want to buy ")
            n=int(input("enter stock "))
            for i in range(0,n):
                if product[i]==a:
                    print("the bill is ",n*price[i])
                    stock[i]=stock[i]-n
                    break
        elif(r==3):
            b=input("enter the product ")
            c=input("enter the stock ")
            d=input("enter the price ")
            sno.append(n+1)
            product.append(b)
            stock.append(c)
            price.append(d)
            n=n+1
        if(r==4):
            break
        choice=input("enter Y/N")
