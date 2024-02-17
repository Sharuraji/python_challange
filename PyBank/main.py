# Import dependencies
import os
import csv

# set the path for csv file
path_csv =os.path.join ("PyBank","Resources","budget_data.csv")
  
# total number of months
net_total=0
number_of_months=0    
change_profit=[]                                   
profit_losses=[]
month=[]


with open(path_csv,"r") as file:
    csvreader =csv.reader(file)
    next(csvreader)



# number_of_months and Net total profit/losses  over the period     
    
    count=0
    for rows in csvreader:
            number_of_months+=1
            profit_losses.append(rows[1])
            month.append(rows[0])
            

        
    for i in range(0,len(profit_losses)):
            net_total+=int(profit_losses[i])


        # The changes in profit/losses
    for x in range(1, len(profit_losses)):
            change_profit.append(int(profit_losses[x]) - int(profit_losses[x-1]))


        # Calculate the average profit/losses change
    average_change_profit = sum(change_profit) / len(change_profit)
        
        # Greatest increase in profit
    greastest_increase=max(change_profit)
    # print(greastest_increase)

        # Date of greatest increase
    greastest_increase_date=month[change_profit.index(greastest_increase)+1]
    # print(greastest_increase_date)

        # Greatest decrease in profit
    greatest_decrease=min(change_profit)
    # print(greatest_decrease)

        # Date of greatest decrease
    greatest_decrease_date=month[change_profit.index(greatest_decrease)+1]
    # print(greatest_decrease_date)

    # Financial Analysis

    # create a text file
        
    filepath=os.path.join("PyBank","analysis", "pybank.txt")  
    file=open(filepath,"w")

    # writing into text file display to console
    file.write(f"\n")
    file.write("Financial Analysis\n")    
    print(f"Financial Analysis")
    file.write("--------------------------\n\n")
    print(f"-------------------------------------")
    file.write(f"Total Months: {number_of_months}\n\n")  
    print(f"Total Months: {number_of_months}\n")
    file.write(f"Total: ${net_total}\n\n")
    print(f"Total: ${net_total}\n")
    file.write(f"Average change : {round(average_change_profit,2)}\n")
    print(f"Average change : {round(average_change_profit,2)}")
    file.write(f"Greatest Increase in Profits:{greastest_increase_date} (${greastest_increase})\n")
    print(f"Greatest Increase in Profits:{greastest_increase_date} (${greastest_increase})")
    file.write(f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})\n")
    print(f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease})")

    file.close()

                    
                                  
                                        

    

        


    

                        
                        