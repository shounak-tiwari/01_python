higersec = input("enter the status of higher secondary class : (passed or running ) : ")
if higersec == "passed":
    percetange = float(input("Enter percentage : "))
    if percetange >= 75 : 
        percentile = float(input("Enter percentile : "))
        if percentile >= 20 : 
            print("your are eligible for addmissionn")
        else:
            print("oops! dear candidate your percentile is less from our criteria percentile please try second time in mains ")
    else:
        print("oops! dear candidate your percentage is not mathced from our criteria ")
elif higersec == "running": 
    percentile = float(input("Enter percentile : "))    
    if percentile >= 20 : 
        print("your are eligible for addmissionn")
    else:
            print("oops! dear candidate your percentile is less from our criteria percentile please try second time in mains ")
else:
    print("please complete your higher education first ")