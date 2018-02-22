import datetime
today = datetime.date.today()
dayofcurrentweek = today.isoweekday()
today_str= today.strftime("%d-%m-%Y")
if (dayofcurrentweek==1):
    imera="Deftera"
elif (dayofcurrentweek==2):
    imera="Triti"
elif (dayofcurrentweek==3):
    imera="Tetarti"
elif (dayofcurrentweek==4):
    imera="Pempti"
elif (dayofcurrentweek==5):
    imera="Paraskevi"
elif (dayofcurrentweek==6):
    imera="Savvato"
else:imera="Kiriaki"

print "Simerini imerominia:",imera ,today_str
print "-------------------------------"

def add_years(day, years):
    try:
        return day.replace(year = day.year + years)
    except ValueError:
        return day + (date(day.year + years, 1, 1) - date(day.year, 1, 1))
count=0
for i in range (1,11):
    nextyear = add_years(today,i)
    dayofweek = nextyear.isoweekday()
    if dayofweek == dayofcurrentweek:
        count+=1
        if count==1:
            print "Idies imerominies\n-----------------"
        nextyear= nextyear.strftime("%d-%m-%Y")
        print imera, nextyear
if count > 0:
    print "-----------------\n"
    print "Sinolo:",count
else:
    print "Den yparxoun idies imerominies ta epomena 10 xronia"
