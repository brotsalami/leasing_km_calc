import datetime
from datetime import date
from datetime import timedelta

# get the current day
today = date.today()
today_str = today.strftime("%d.%m.%Y")
print("Today's date:", today_str)

#define start and end date
datetimeFormat = '%d.%m.%Y'
return_date = '05.09.2021'
#print("returndate date:", return_date)
start_date = '05.09.2017'
#print("startdate date:", start_date)

#define cost earnings
cost = 1.44
earnings = 1.04

#calculate the number of days between start and end
diff_date_total = datetime.datetime.strptime(return_date, datetimeFormat)\
    - datetime.datetime.strptime(start_date, datetimeFormat)
total_days = diff_date_total.days
#print("diff_total:", diff_date_total.days)

#calculate the number of days between start and now  
diff_date_current = datetime.datetime.strptime(today_str, datetimeFormat)\
    - datetime.datetime.strptime(start_date, datetimeFormat)
current_days = diff_date_current.days

#print("diff_current:", diff_date_current.days)

# define total distance in km and calculate total avg
total_km = 80000
total_avg = total_km/total_days


#input of current km and current avg
current_km = input("Aktueller km Stand:")

#error catching should be here

current_avg = float(current_km)/float(current_days)

#calculate difference between should and actual distance
difference_total_current = total_avg * float(current_days) - float(current_km)

#output of calculations
print("Gesamtdurchschnitt: {:.2f}".format(total_avg),"km")
print("Aktueller Durchschnitt: {:.2f}".format(current_avg),"km")
print("Erwartete Gesamtdifferenz: {:.2f}"  .format(difference_total_current),"km")

#calculation of cost/earning when the car is returned
if current_avg < total_avg:
    difference_total_current * earnings
    print("Erwartete Einnahmen: {:.2f}".format(difference_total_current * earnings),"€")
else:
    difference_total_current * cost
    print("Erwartete Kosten: {:.2f}".format(difference_total_current * cost),"€")


