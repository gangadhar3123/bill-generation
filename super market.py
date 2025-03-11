name=input("enter your name:")
lists='''
rice   Rs 10/kg
sugar  Rs 8/kg
oil    Rs 30/liter
salt   Rs 25/kg
panner Rs 40/kg
maggie Rs 12/pack
boost  Rs 200/bottle
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rate for each item
items={'rice':10,'sugar':8,'oil':30,'salt':25,'panner':40,'maggie':12,'boost':200}
while True:
    option=input("press 1 for list or 2 to exit:")
    if option=='2':
        print("Thank you for shopping")
        break
    elif option=='1':
        print(lists)
        while True:
            inp1=input("to buy press 1 or press 2 to exit:")
            if inp1=='2':
                print("Thank you for shopping")
                break
            elif inp1=='1':
                item=input("choose your items:").lower()
                while True:
                    quantity_input=input("enter quantity:")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("please enter a valid quantity")
                if item in items:
                    price=quantity*items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice +=price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("selected item is not available.sorry for the inconvenience")
    if totalprice >0:
        tax=(totalprice*12)/100
        finalamount=tax+totalprice
        print(25* "=","SUPERMARKET",25*"=")
        print(25*"","HYDERABAD")
        print("name:",name,30*"")
        print(75*"-")
        print("sno",10*"",'items',8*"",'quantity',8*"",'price')
        for i in range(len(pricelist)):
           print(i,13*"",ilist[i],8*"",qlist[i],8*"",plist[i])
        print(75*"")
        print(75*"",'Total amount:','Rs',totalprice)
        print("Tax amount",50*"",'Rs',tax)
        print(75*"-")
        print(50*"",'Final amount:','Rs',finalamount)
        print(75*"-")
        print(20*"","Thank you & visit again")
        print(75*"-")        
        
        
                        