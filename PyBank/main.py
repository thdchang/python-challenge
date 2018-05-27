#Challenge 1: PyBank 

#In this challenge, a Python script is created for analyzing
#datasets of financial records in a .csv file which is composed of
#two columns: Date and Revenue

#The Python script analyzes the records to calculate each of the following: 
#   1. The total number of months included in the dataset. 
#   2. The total amount of revenue gained over the entire period. 
#   3. The average change in revenue between months over the entire period. 
#   4. The greatest increase in revenue (date and amount) over the entire period. 
#   5. The greatest decrease in revenue (date and amount) over the entire period. 


#-------------------------------------------------------------------
#Beginning of script


#import modules
import os 
import csv
import datetime as datetime


#--------

#Below are functions used in this script:


#function calculating the average revenue through the entire period
def calcAvgRevenue(revenue):
    #calculating the average change in revenue
    change_list = []
    revenue_1 = revenue[0]
    
    for x in range(1, len(revenue)):
        revenue_2 = revenue[x]

        change_revenue = revenue_2 - revenue_1
        change_list.append(change_revenue)

        revenue_1 = revenue[x]
        
    average_change_revenue = sum(change_list)/ len(change_list)

    return average_change_revenue




#function to calculate the greatest increase in revenue
def greatIncRev(revenue):
    
    #sort revenue to descending order to assign greatest revenue to index 0 
    revenue_descend = sorted(revenue, reverse = True)
    great_increase_revenue = revenue_descend[0]


    return great_increase_revenue




#function to calculate the greatest decrease in revenue
def greatDecRev(revenue):
    
    #sort revenue list to ascending order to assign lowest revenue to index 0 
    revenue_ascend = sorted(revenue, reverse = False)
    great_decrease_revenue = revenue_ascend[0]

    return great_decrease_revenue




#function to calculate the greatest increase revenue date
def great_Inc_RevDate(revenue, date, great_increase_revenue):

    dataSet_dict = dict(zip(revenue, date))
    increase_date = dataSet_dict[great_increase_revenue]

    return increase_date




#function to calculate the greatest decrease revenue date
def great_Dec_RevDate(revenue, date, great_decrease_revenue):
    
    dataSet_dict = dict(zip(revenue, date))
    decrease_date = dataSet_dict[great_decrease_revenue]

    return decrease_date


#function calculates the number of months over the entire period
def num_Months(dateList):

    #split month and number to determine the if number represents days or years
    split_date_list = []

    for date in dateList:
        split_date = date.split("-")

        if int(split_date[1]) <= 31:

            days = True

            break
        else:
            
            days = False

            break

    #if number in date are days; sort the date list accordingly
    if days == True:

        dateFormat = '%b-%d'
        dateList_sorted = sorted(dateList, key=lambda dateList: datetime.datetime.strptime(dateList, dateFormat))

    #if number in date are years; sort the date list accordingly
    else:
        dateFormat = '%b-%Y'
        dateList_sorted = sorted(dateList, key=lambda dateList: datetime.datetime.strptime(dateList, dateFormat))

    #assign the first and last indices to first and last date over the entire period of the date list
    firstDate = datetime.datetime.strptime(dateList_sorted[0], dateFormat)
    lastDate = datetime.datetime.strptime((dateList_sorted[len(dateList_sorted)-1]), dateFormat)

    #calculate the difference between the first and last dates in months 
    sumDays = lastDate - firstDate
    sumMonth = sumDays.days / 30

    return sumMonth


#---------------------------



#prompt user to input path for dataset to be analyzed 
print("")
fileName = input("Input dataset file name (include extension): ")
print("")
folder = input("Input folder name: ")

#prompt user to input path for where to write financial analysis 
print("")
output_fileName = input("Output text file name (include extension): ")
print("")
output_folder = input("Output folder name: ")




#open dataset to be used to do analysis
dataset_path1 = os.path.join("..", folder, fileName)

with open(dataset_path1, newline="") as cvsFile1:
    
    budgetData = csv.reader(cvsFile1, delimiter = ",")

    budget_header = next(budgetData)


    #separate dataset to create two lists: date and revenue
    date = []
    revenue = []

    for row in budgetData:            

        #add data values to the data list, add revenue values to revenue list
        date.append(row[0])
        revenue.append(int(row[1]))

    

    #calculate sum of revenues 
    sumRevenue = sum(revenue)

    

#assign function calls return values into variables 
months = num_Months(date)

totalRevenue = sumRevenue

average_revenue_change = calcAvgRevenue(revenue)

increase_amount = greatIncRev(revenue)
increase_date = great_Inc_RevDate(revenue, date, increase_amount)

decrease_amount = greatDecRev(revenue)
decrease_date = great_Dec_RevDate(revenue, date, decrease_amount)



#open text file to write Financial Analysis into 
analysis_output_path = os.path.join("..", output_folder, output_fileName)

with open(analysis_output_path, 'w') as outputFile:

    #printout analysis 
    outputFile.write("Financial Analysis")
    outputFile.write("\n")
    outputFile.write("-------------------------")
    outputFile.write("\n")
    outputFile.write("Total Months: " + str(months))
    outputFile.write("\n")
    outputFile.write("Total Revenue: " + "$" + str(totalRevenue))
    outputFile.write("\n")
    outputFile.write("Average Revenue Change: " + "$" + str(average_revenue_change))
    outputFile.write("\n")
    outputFile.write("Greatest Increase in Revenue: " + increase_date + " $" + str(increase_amount))
    outputFile.write("\n")
    outputFile.write("Greatest Decrease in Revenue: " + decrease_date + " $" + str(decrease_amount))


