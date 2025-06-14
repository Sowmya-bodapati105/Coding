from datetime import datetime
print("-------------------------------------WELCOME---------------------------------------------")
user=input("Enter user name")
lists='''
Rice     Rs 100/kg
sugar    Rs 20/kg
salt     Rs 10/kg
panner   Rs 120/kg
Bread    Rs 30/kg
oil      Rs 80/liter
Boost    Rs 90/kg
colgate  Rs 85/eac
'''
#Declartion
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':100,
       'sugar':20,'salt':10,'panner':120,'bread':30,'oil':80,'boost':90,'colgate':85}
option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items")
        quantity=int(input("Enter your Quantity"))
        if item in items.keys():
          price=quantity*(items[item])
          pricelist.append((item,quantity,items,price))
          totalprice+=price
          ilist.append(item)
          qlist.append(quantity)
          plist.append(price)
          gst=(totalprice*5)/100
          finalamount=gst+totalprice
        else:
          print("Sorry you entered item is not available")
else:
    print("You Entered Wrong number")
inp=input("Can I print bill the items yes or no")
if inp=="yes":
    pass
    if finalamount!=0:
        print(25*"=","PADMA SUPERMARKET",25*"=")
        print(28*"=","wanaparty")
        print("Name:",user,30*" ","Date:",datetime.now)
        print(75*"-",)
    for i in range(len(pricelist)):
        print(i,8*' ',5*'',ilist[i],10*' ',qlist[i],10*" ",plist[i])
        print(75*"-")
        print(50*" ",'Total amount:','Rs',totalprice)
        print("gst amount",40*" ",'GST Rs',totalprice)
        print(75*"-")
        print(50*"-",'finalamount:' ,'Rs',finalamount)
        print(75*"-")
        print(20*" ","Thamks for visting")
        print(75*" ")


