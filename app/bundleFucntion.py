import pandas as pd


def detect_bundle(prod_name: str):
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
    units = []
    noUnit = 1
    for ele in list_of_bundles:
        if ele.lower() in prod_name.lower():
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
        noUnit = 1
    return noUnit


df = pd.ExcelFile("data/amazon_soft_drinks_price.xlsx").parse("amazon_soft_drinks_price")
prod_names = df["product_name"]
final_list = []
for i in prod_names:
    try:
        final_list.append(detect_bundle(i))
    except:
        final_list.append(1)
df = pd.DataFrame(final_list)
df.to_csv("output/bundles3.csv", index=False)
