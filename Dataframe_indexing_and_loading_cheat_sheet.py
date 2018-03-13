import pandas as pd

print("Dataframe Indexing and Loading")
print("-------------------")
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

costs = df['Cost']
print("Costs:")
print(costs)

print("=======================")
print("Adding 2 to all costs: costs+=2")
costs+=2
print(costs)

print("=======================")
df = pd.read_csv('olympics.csv')
print("df:")
print(df)

