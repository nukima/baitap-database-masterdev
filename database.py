import pandas as pd
import random
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="admin",
#   database="masterdev"
# )

# cursor = mydb.cursor()
df = pd.DataFrame()
print(df)
class_id_list2 = []
for i in range(1, 10):
	for j in range(1):
		class_id_list2.append(69)

df2 = list(zip(class_id_list2, range(1, 40001), range(1, 40001)))
#append
df2 = pd.DataFrame(df2, columns=['class_id', 'name', 'email'])
print(df2)
df = df.append(df2, ignore_index=True)
print(df)
df.to_csv('tmp.csv', index=False)


