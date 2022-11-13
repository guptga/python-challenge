#import modules
import os
import csv

#set path for file
#print(os.path)
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Resources','budget_data.csv')
#set the output of the text file
text_path= os.path.join(os.path.dirname(os.path.abspath(__file__)),'Analysis','Output.txt')

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_change_average = 0.00

#open the csv file
with open(csvpath,'r') as csvfile:  
    csvreader = csv.DictReader(csvfile)
    

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months += 1

        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        if total_months == 1:
            revenue_change = 0.00
            previous_revenue = int(row["Profit/Losses"])
        else:
            revenue_change = int(row["Profit/Losses"])-previous_revenue
            previous_revenue = int(row["Profit/Losses"])
            revenue_change_list.append(revenue_change)
        #print(revenue_change)

       

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
    #print(sum(revenue_change_list))
    #print(len(revenue_change_list))
    revenue_change_average = round(sum(revenue_change_list)/len(revenue_change_list),2)   
    #print(revenue_change_average)

   
#write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%.2f\n" % revenue_change_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
