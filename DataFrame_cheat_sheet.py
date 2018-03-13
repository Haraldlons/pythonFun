import pandas as pd

print("The DataFrame Data Structure Cheat Sheet")
print("-------------------------")

# First declaring panda-series
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
# Adding them all together to a DataFrame
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print("Declared panda-series and combined them in a DataFrame: " + str(df.head()))

print("===================")
print("Get 'Store 2'")
print(df.loc["Store 2"])
print("==================")
print("Get row='Store 2' and column = 'Cost' ")
print(df.loc['Store 2', 'Cost'])

print("==================")
print("Get transpose of DataFrame: df.T")
print(df.T)

print("===================")
print("Getting just the Name and Cost-values of all items")
print(df.loc[:,["Name", "Cost"]])

print("==================")
print("Appending new item without giving new index:")
newTable = df.append(pd.Series({'Name': 'Harald',
                        'Item Purchased': 'Elephant Seed',
                        'Cost': 555.00}),ignore_index=True)
print(newTable)
print("=================")
print("Appending new item WITH declared new index")
newTable = df.append(pd.Series({'Name': "ItemAddedWithIndex",
						'Item Purchased': "Telenor Packets",
						'Cost': 123,
						'index' : "Store 4"
	}, index = ['Cost', 'Name']), ignore_index=True)
print(df)

print("================")
print("Get specific row and column, ['Store 1', ['Cost']:")
print(df.loc['Store 2', 'Cost'])

print("===============")
print("Dropping of an item: df.drop('Store 1')")
print(df.drop('Store 1'))
print("Keep in mind that the original df wil not be changed")
print("================")
print("Copying")
copy_df = df.copy()
print("copy_df: ")
print(copy_df)
print("===============")
print("Deleting an column: del copy_df['Name']")
del copy_df['Name']
print(copy_df)

