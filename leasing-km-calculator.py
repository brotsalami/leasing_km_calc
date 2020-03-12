import datetime
from datetime import date
from datetime import timedelta

# get the current day
today = date.today()
today_str = today.strftime("%d.%m.%Y")
print("Heute ist der:", today_str)

#define start and end date
datetimeFormat = '%d.%m.%Y'
return_date = '05.09.2021'
try:
    val_date = return_date.days
    pass
except AttributeError: 
    print("ve")
    pass
#print("returndate date:", return_date)
start_date = '05.09.2017'
#print("startdate date:", start_date)

#define cost earnings
cost = 0.0743
earnings = 0.045

def date_diff (start, end, datetimeFormat):
    date_diff = datetime.datetime.strptime(end, datetimeFormat)\
    - datetime.datetime.strptime(start, datetimeFormat)
    return date_diff

#calculate the number of days between start and end
diff_date_total = date_diff(start_date,return_date, datetimeFormat)
total_days = diff_date_total.days
#print("diff_total:", diff_date_total.days)

#calculate the number of days between start and now  
diff_date_current = date_diff(start_date,today_str, datetimeFormat)
current_days = diff_date_current.days

#print("diff_current:", diff_date_current.days)

# define total distance in km and calculate total avg
total_km = 80000
total_avg = total_km/total_days
#input of current km and current avg
error_output_number = "Bitte geben Sie eine ganze, positive Zahl ein!"


#error catching for user input
while True:
    try:
        current_km = input("Bitte geben Sie den aktuellen km Stand ein:")
        val = int(current_km)  
        break
        #print("Input is an integer number. Number = ", val)
        if val < 0:
            print(error_output_number)
        else:
            user_input = True
    except ValueError:
        print(error_output_number)


current_avg = float(current_km)/float(current_days)

#calculate difference between should and actual distance
difference_total_current = total_avg * float(current_days) - float(current_km)

#output of calculations
print("Erwarteter Durchschnitt: {:.2f}".format(total_avg),"km")
print("Aktueller Durchschnitt: {:.2f}".format(current_avg),"km")


#calculation of cost/earning when the car is returned
if current_avg < total_avg:
    difference_total_current * earnings
    print("Erwartete Rückzahlung: {:.2f}".format(difference_total_current * earnings),"€")
    print("Erwartete Differenz zur max km-Zahl: {:.2f}"  .format(difference_total_current),"km weniger")
else:
    difference_total_current * cost
    print("Erwartete Nachzahlung: {:.2f}".format(difference_total_current * cost * -1),"€")
    print("Erwartete Differenz zur max km-Zahl: {:.2f}"  .format(difference_total_current * -1),"km zu viel")

ende = input("Drücke Enter um das Programm zu beenden")
