import pandas as pd
import json
import re
list_of_bundles = ["pack of", " count)"," count ", " ct", "pack", "pk", "cans", "Bottles"]
f = open('data/data.json',)
data = json.load(f)


final_list = []
match = 0
for i in range(len(data)):
    for ele in list_of_bundles:
        if ele.lower() in data[i]['product_name'].lower():
            match = 1
            break
    if match == 0:
        bundle_details = {'bundle_flag': 0}
        data[i]["bundle_details"] = bundle_details
    else:
        bundle_details = {'bundle_flag': 0, 'no_of_items': 5, 'unit_price': 100}
        match = 0
df = pd.ExcelFile('data/amazon_soft_drinks_price.xlsx').parse('amazon_soft_drinks_price') #you could add index_col=0 if there's an index
prod_names = df['product_name']
for prod_name in prod_names:
    for ele in list_of_bundles:
        if ele.lower() in prod_name.lower():
            #print(ele.lower())
            match = 1
            unit = 1
            try:          
                if ele.lower() == "pack of":
                    # print(prod_name)
                    if "(pack of" in prod_name.lower():
                        units = (prod_name.lower().split("(pack of"))[1].split(")")[0].split()[0].replace(',', ' ') #prod_name.lower().split("(pack of")[1].split()[0]#prod_name[prod_name.lower().find("(")+1:prod_name.find(")")].split()
                        #print(prod_name, "units :",int(units))
                        
                    else:
                        units = prod_name.lower().split("pack of")[1].split()[0].replace(',', ' ').split()[0]
                        # print(units)
                else:
                    units = prod_name.lower().split(ele.lower())[0].split()[-1].replace('-', ' ').replace('(', ' ')
                    #print(prod_name, "units :",int(units))
                final_list.append([prod_name, 1, int(units)]) 
                break
                
            except Exception as e:
                #print("outside",e,prod_name,ele.lower(),"unit" , prod_name.lower().split(ele.lower())[0].split()[-1].replace('-', ' ').replace('(', ' '))
                final_list.append([prod_name, 1, "unknown"])
                break

            #units = res = [int(i) for i in prod_name.split() if i.isdigit()]

    if match == 0:
        final_list.append([prod_name, 0,1])
    else:
        match  = 0


df = pd.DataFrame(final_list)
df.to_csv('output/bundles.csv')  




'''
df = pd.ExcelFile('data/amazon_soft_drinks_price.xlsx').parse('amazon_soft_drinks_price') #you could add index_col=0 if there's an index
prod_names = df['product_name']
print(prod_names[0])
list_of_bundles = ["pack of", "pack", "pk", "cans", "Bottles"]
final_list = []
match = 0
for prod_name in prod_names:
    for ele in list_of_bundles:
        if ele.lower() in prod_name.lower():
            match = 1
            final_list.append([prod_name, 1])
            break
    if match == 0:
        final_list.append([prod_name, 0])
    else:
        match  = 0


df = pd.DataFrame(final_list)
df.to_csv('output/bundles.csv')  
'''