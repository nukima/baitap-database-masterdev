from operator import le
import random
import pandas as pd

# # CREATE user-raw-data.csv
# #read file csv
# data = pd.read_csv('resources/GT.csv', delimiter=',')

# #drop sex, area column
# data = data.drop(['area', 'sex'], axis=1)

# #remove rows with missing values
# data = data.dropna()

# #merge first and last name into one column
# data['name'] = data['firstname'] + ' ' + data['lastname']
# #drop first and last name column
# data = data.drop(['firstname', 'lastname'], axis=1)
# #remove invalid latin names
# data = data[~data['name'].str.match(r'.*[^\x00-\xFF]')]

# #add id column
# data['id'] = range(1, len(data)+1)
# #set id column as index
# data = data.set_index('id')

# data.to_csv('resources/user-raw-data.csv', index=True)




#------------------------------------------
#read in data
data = pd.read_csv('resources/user-raw-data.csv', delimiter=',')
#create username from name
data['username'] = data['name'].str.lower().str.replace(' ', '')

#remove duplicate username
data = data.drop_duplicates(subset=['username'])

#reset id column
data['id'] = range(1, len(data)+1)


#add province column
province_data = pd.read_csv('resources/province.txt', delimiter=',')
print(province_data)
#random select province for each user
data['province'] = [random.choice(province_data['province']) for i in range(len(data))]

#random age for each user
data['age'] = [random.randint(18, 65) for i in range(len(data))]

#set id column as index
data = data.set_index('id')
print(data.shape)

#remove duplicate username
data = data.drop_duplicates(subset=['username'])
print(data.shape)
data.to_csv('data/user-data.csv', index=True)

print(data.tail())



