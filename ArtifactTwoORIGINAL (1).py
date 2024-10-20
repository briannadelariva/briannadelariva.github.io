### This is an assignment for IT-145 Intro to Scripting course at Southern New Hampshire University to calculate the seasons given the month and day inputs. 

###The dates for each season are:
### Spring: March 20 - June 20
### Summer: June 21 - September 21
### Autumn: September 22 - December 20
### Winter: December 21 - March 19 

### This is obtaining input
input_month = (input())
input_day = int(input())

### This is setting up the invalid parameters for the program per the dates. 
if (input_day < 0):
    print ("Invalid")

elif (input_day > 28 and input_month == 'February'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'January'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'March'):
    print ("Invalid")

elif (input_day > 30 and input_month == 'April'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'May'):
    print ("Invalid")

elif (input_day > 30 and input_month == 'June'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'July'):
    print ("Invalid")

elif (input_day > 30 and input_month == 'August'):
    print ("Invalid")

elif (input_day > 30 and input_month == 'September'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'October'):
    print ("Invalid")

elif (input_day > 30 and input_month == 'November'):
    print ("Invalid")

elif (input_day > 31 and input_month == 'December'):
    print ("Invalid")

### Utilizes the input data to determine the season and prints the season

elif (input_day >= 20 and input_month == 'March') or (input_month == 'April' or input_month =='May') or (input_day <= 20 and input_month == 'June'):
    print ("Spring") 

elif (input_day >= 21 and input_month == 'June') or (input_month == 'July' or input_month =='August') or (input_day <= 21 and input_month == 'September'):
    print ("Summer") 

elif (input_day >= 22 and input_month == 'September') or (input_month == 'October' or input_month =='November') or (input_day <= 20 and input_month == 'December'):
    print ("Autumn") 

elif (input_day >= 21 and input_month == 'December') or (input_month == 'January' or input_month =='February') or (input_day <= 19 and input_month == 'March'):
    print ("Winter") 

    
else:
    print ("Invalid")
    
