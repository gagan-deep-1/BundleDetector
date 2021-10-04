import pandas as pd

df = pd.ExcelFile('data/amazon_soft_drinks_price.xlsx').parse('amazon_soft_drinks_price') #you could add index_col=0 if there's an index
prod_names = df['product_name']
print(prod_names[0])
list_of_bundles = ["pack of", "pack", "pk", "cans"]
final_list = []
for prod_name in prod_names:
    for ele in list_of_bundles:
        if ele.lower() in prod_name.lower():
            final_list.append(prod_name)
            break
df = pd.DataFrame(final_list)
df.to_csv('output/bundles.csv')  
