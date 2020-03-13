import datetime
from datetime import date
from datetime import timedelta
import csv

#row counter for array access. This will define the current selected car in future versions, to make sure that always the same line is seletced of the csv
line_sel = 1

#import data from csv file

list_car_name = []
list_start_date = []
list_end_date = []
list_total_km = []
list_costs = []
list_earnings = []

with open('config.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        list_car_name.append(row[0])
        list_start_date.append(row[1])
        list_end_date.append(row[2])
        list_total_km.append(row[3])
        list_costs.append(row[4])
        list_earnings.append(row[5])

#    print(list_costs[line_sel])
#    print(len(list_car_name))


# get the current day
today = date.today()
today_str = today.strftime("%d.%m.%Y")
print("Heute ist der:", today_str)
#define start and end date
datetimeFormat = '%d.%m.%Y'
str_start_date = str(list_start_date[line_sel])
return_date = str(list_end_date[line_sel]) #'05.09.2021' #config(2,0)
#define cost earnings
cost =  float(list_costs[line_sel])#0.0743 #
earnings = float(list_earnings[line_sel]) #0.045
# define total distance in km and calculate total avg
total_km = int(list_total_km[line_sel]) #80000

print(total_km)

#try:
#   val_date = return_date.days
 #   pass
#except AttributeError: 
  #  print("ve")
 #   pass
#print("returndate date:", return_date)
#start_date = '05.09.2017'
#print("startdate date:", start_date)


def date_diff (start, end, datetimeFormat):
    date_diff = datetime.datetime.strptime(end, datetimeFormat)\
    - datetime.datetime.strptime(start, datetimeFormat)
    return date_diff

#calculate the number of days between start and end
diff_date_total = date_diff(str_start_date,return_date, datetimeFormat)
total_days = diff_date_total.days
#print("diff_total:", diff_date_total.days)

#calculate the number of days between start and now  
diff_date_current = date_diff(str_start_date,today_str, datetimeFormat)
current_days = diff_date_current.days

#print("diff_current:", diff_date_current.days)
total_avg = total_km/total_days


#input of current km 
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
