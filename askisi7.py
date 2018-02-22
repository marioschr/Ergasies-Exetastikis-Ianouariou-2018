import datetime
today = datetime.date.today()
today_str= today.strftime("%d-%m-%Y")
print "Simerini imerominia:",today_str
print "-------------------------------"
dayofcurrentweek = today.isoweekday()
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
        print nextyear
if count > 0:
    print "-----------------\n"
    print "Sinolo:",count
else:
    print "Den yparxoun idies imerominies ta epomena 10 xronia"
