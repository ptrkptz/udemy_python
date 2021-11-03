import pandas as pd
file = pd.ExcelFile("sales.xlsx")

print(file.sheet_names)

sheet = file.parse('sales')
print(sheet)
#type(sheet)

print(sheet.Date)

print(sheet.Amount)

print(sheet.Amount.sum())

# this prints the row
print(sheet.loc[0])

#Print row 0, column 'Amount'
print(sheet.loc[0, "Amount"])

# Search sales for a specific customer
sheet.set_index("Customer", inplace=True)
print(sheet.loc["MMC Inc."])

sheet = sheet.reset_index()

print(type(sheet["Invoice"]))

print(sheet.loc[sheet["Invoice"] == 99])

print(sheet.loc[sheet["Amount"] > 2000])

# largest amount
print(sheet.loc[sheet["Amount"].idxmax()])

#get specific column with the highest amount
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])

# there are two for the same customer for >1800
print(sheet.loc[sheet["Amount"] > 1800] ["Customer"].unique())

#get the first unique from above
print(sheet.loc[sheet["Amount"] > 1800] ["Customer"].unique()[0])

#loop thru the list
for customer in sheet.loc[sheet["Amount"] > 1800] ["Customer"].unique():
    print(customer)