from sklearn.metrics import f1_score
import pandas
data = pandas.read_csv('output/flaggedBundle.csv')
y_true = list(map(int, data["pred_flag"].tolist()))
y_pred = list(map(int, data["treu_flag"].tolist()))
for i in y_pred:
    if i!=1:
        if i!=0:
            print(i)

print("done up")
for i in y_true:
    if i!=1:
        if i!=0:
            print(i)
f1 = f1_score(y_true, y_pred, average='binary')
print(f1)