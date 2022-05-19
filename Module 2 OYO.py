#Hugo Fernandez
#COP1000
#5/19/2022 -Module 2: OYO
#################
#Prompt the user to enter a sales tax rate.
#Prompt the user to enter a price.
#Calculate and output the amount of tax for the item and the total price with tax.
######################################################################


tax_rate= float(input("Enter Sales Tax Rate\n"))
price= int(input("Enter Price\n"))
item_tax_rate= tax_rate*price
total_price= item_tax_rate+price

print ("amount of tax rate for this item is $" +str(item_tax_rate))
print ("Total price with tax is $" +str(total_price))

