#if buy
def ifbuy(number_of_shares,price_asksize):
    while number_of_shares!=0:
        dict(sorted(price_asksize.items()))
        priority_price=list(price_asksize)[0]
        asksize=price_asksize[priority_price]
        x =asksize-number_of_shares
        if(x>0):
            price_asksize[priority_price]=x
            number_of_shares=0
        else:
            number_of_shares=-(x)
            price_asksize.pop(priority_price)
    print("bidsize\tprice\tasksize")
    for i in sorted(price_asksize.keys(),reverse=True):
        print("{}\t{}\t{}".format("",i,price_asksize[i]))

#if sell
def ifsell(number_of_shares,price_bidsize):
    while number_of_shares!=0:
        dict(sorted(price_bidsize.items()))
        priority_price=list(price_bidsize)[0]
        bidsize=price_bidsize[priority_price]
        x =bidsize-number_of_shares
        if(x>0):
            price_bidsize[priority_price]=x
            number_of_shares=0
        else:
            number_of_shares=-(x)
            price_bidsize.pop(priority_price)
    print("bidsize\tprice\tasksize")
    for i in sorted(price_bidsize.keys(),reverse=True):
        print("{}\t{}\t{}".format(price_bidsize[i],i,""))
    
# price,asksize,bidsize data feed    
price_asksize={11.38:400,11.39:1600,11.40:1205,11.41:1400,11.42:900}
price_bidsize={11.36:2700,11.35:1100,11.34:1100,11.33:1600,11.32:700}

#market order
print("--------market order--------")
number_of_shares=int(input("enter the number of shares: "))
operation=input("Buy or Sell: ")
if operation.lower()=='buy':
    ifbuy(number_of_shares,price_asksize)
elif operation.lower()=='sell':
    ifsell(number_of_shares,price_bidsize)

print("---------------------------")




#limit order
print("--------limit order--------")
price_asksize={11.38:400,11.39:1600,11.40:1205,11.41:1400,11.42:900}
price_bidsize={11.36:2700,11.35:1100,11.34:1100,11.33:1600,11.32:700}
number_of_shares=int(input("enter the number of shares: "))
operation=input("Buy or Sell: ")

limit_price=float(input("enter the limit price: "))
base_askprice=list(price_asksize)[0]
base_bidprice=list(price_bidsize)[0]
if operation.lower()=='buy':
    if limit_price>=base_askprice:
        ifbuy(number_of_shares,price_asksize)
    else:
        print("increase limit price!")
elif operation.lower()=='sell':
    if limit_price<=base_bidprice:
         ifsell(number_of_shares,price_bidsize)
    else:
        print("decrease limit price")


#stop order
#if the stop order price hits the base , we sell the shares by executing the stop order     
price_asksize={11.38:400,11.39:1600,11.40:1205,11.41:1400,11.42:900}
price_bidsize={11.36:2700,11.35:1100,11.34:1100,11.33:1600,11.32:700}
base_bidprice=list(price_bidsize)[0]
print("--------stop order--------")
number_of_shares=int(input("enter the number of shares: "))
stoporder=float(input("enter the stop loss order value: "))
if base_bidprice==stoporder:
    print("stop loss order executed!")
    ifsell(number_of_shares,price_bidsize)
































        



