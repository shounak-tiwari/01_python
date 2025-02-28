budget = float(input("Enter Budget : "))
product = input("product cat (sports/formal/casual/occ...) : ")

if (budget >=2000 and budget<=5000 ) and (product =="sports"):
    print("Buy from addidas")

elif (budget >5000 and budget<=10000 ) and (product =="sports"):
    print("Buy from puma")

elif (budget >10000 ) and (product =="sports"):
    print("Buy from red chif")

elif (budget >5000 and budget<=10000 ) and (product =="formal"):
    print("Buy from raymonds")

elif (budget >10000 ) and (product =="formal"):
    print("Buy from peter england / alloy ..../ siyaram's /...")

elif (budget >5000 and budget<=10000 ) and (product =="casual"):
    print("Buy from blue juede")

elif (budget >10000 ) and (product =="casual"):
    print("Buy from spyker")

else:
    print("Buy from local market")