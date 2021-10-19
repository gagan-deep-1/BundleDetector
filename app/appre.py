import pandas as pd
import json
import re

list_of_bundles = [
    "pack of",
    "Case of",
    " count)",
    " count",
    " ct",
    "pack",
    "pk",
    "cans",
    "Bottles",
    "per case",
    "fl VP",
    "Pouches",
]
f = open(
    "data/data.json",
)
data = json.load(f)


final_list = []
match = 0
for i in range(len(data)):
    for ele in list_of_bundles:
        if ele.lower() in data[i]["product_name"].lower():
            match = 1
            break
    if match == 0:
        bundle_details = {"bundle_flag": 0}
        data[i]["bundle_details"] = bundle_details
    else:
        bundle_details = {"bundle_flag": 0, "no_of_items": 5, "unit_price": 100}
        match = 0
df = pd.ExcelFile("data/amazon_soft_drinks_price.xlsx").parse(
    "amazon_soft_drinks_price"
)  # you could add index_col=0 if there's an index
prod_names = df["product_name"]
price = {}
for i in range(len(prod_names)):
    try:
        price[prod_names[i]] = str(df["product_price/Price:/0"][i])
        if not str(df["product_price/Price:/0"][i]).isdigit():
            # print(prod_names[i],df["product_price/Price:/0"][i])
            price[prod_names[i]] = price[prod_names[i]].split("$")[1].split("_x")[0]
    except Exception as e:
        pass

for prod_name in prod_names:
    listTemp = []
    units = []
    for ele in list_of_bundles:
        if ele.lower() in prod_name.lower():
            match = 1
            unit = 1
            try:
                if ele.lower() == "pack of" or ele.lower() == "case of":
                    units.append(
                        int(
                            (prod_name.lower().split(ele.lower()))[1]
                            .split()[0]
                            .replace(",", " ")
                            .replace(")", " ")
                            .split()[0]
                        )
                    )
                else:
                    units.append(
                        int(prod_name.lower().split(ele.lower())[0].split()[-1].replace("-", " ").replace("(", " "))
                    )

            except Exception as e:
                pass
    try:
        noUnit = int(max(units))
    except Exception as e:
        print(prod_name,units)
        noUnit = "unknown"

    try:
        perUnit = float(price[prod_name]) / noUnit
    except:
        perUnit = "unknown"

    if match == 0:
        final_list.append([prod_name, 0, 1, price[prod_name], price[prod_name]])
    else:
        match = 0
        final_list.append([prod_name, 1, noUnit, price[prod_name], perUnit])


df = pd.DataFrame(final_list)
headerList = ["product name", "bundle flag", "no of units", "total price", "unit price"]
df.to_csv("output/bundles2.csv", header=headerList, index=False)


"""
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
"""
