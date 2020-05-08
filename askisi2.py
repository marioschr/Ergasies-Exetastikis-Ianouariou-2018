import urllib2
import datetime
import json

today=datetime.datetime.now()
lathos=0
table_save_days=[]
table_save_wins=[]


# Έλεγχος των αριθμών του χρήστη αν υπάρχουν στους κληρωτέους αριθμούς
def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s

# Εκχώρηση αριθμών του χρήστη
while True:
    print "Diloste 10 ari8mous (1-80):\n"
    print "Paradeigmata eisodou: 1 2 3 4 5 6 7 8 9 10"
    print "                     1,2,3,4,5,6,7,8,9,10\n"
    nums= raw_input().split()
    if (len(nums)==1):
        nums=nums[0].split(",")

    nums=map(int,nums)

    if (len(nums)==10):
        for i in range(10):
            if(nums[i]>=1 and nums[i]<=80):
                lathos=1
            else:
                lathos=0
                print "Epitrepontai mono arithmoi metaksy 1 kai 80."
                break
    else: print "Exete eisagei kati lathos."

    if (lathos==1): break
print 28*"-"

# Φόρτωση κληρωμένων αριθμών από τον ΟΠΑΠ
for i in range(31):
    today= today - datetime.timedelta(days=1)
    date_str= today.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']

    # Καταμέτρηση επιτυχιών ανά ημερομηνία
    sum_wins_day=0
    for k in klhrwseis:
        tmp=k["results"]
        epitixies=compare_lists(nums,tmp)
        if (epitixies>4):
            sum_wins_day+=1
    # Αποθήκευση
    table_save_wins.insert(i,sum_wins_day)
    table_save_days.insert(i,date_str)

# Έυρεση ημερομηνίας με την μέγιστη επιτυχία
max_wins=table_save_wins[1]
max_day=table_save_days[1]
for i in range(31):
    if (max_wins < table_save_wins[i]):
        max_wins=table_save_wins[i]
        max_day=table_save_days[i]

# Εκτύπωση αποτελεσμάτων
print 60*"-"
print "Me tous arithmous sas:", nums
print "Tha eixate perissoteres epitixies sto KINO stis", max_day, "me", max_wins, "epitixies!"
print 60*"-"
