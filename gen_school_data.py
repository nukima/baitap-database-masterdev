from operator import le
import random
import pandas as pd

#read in data
data = pd.read_csv('resources/MV.csv', delimiter=',')

#drop area column
data = data.drop(['area'], axis=1)
#remove rows with missing values
data = data.dropna()

#merge first and last name into one column
data['name'] = data['firstname'] + ' ' + data['lastname']
#drop first and last name column
data = data.drop(['firstname', 'lastname'], axis=1)
#remove invalid latin names
data = data[~data['name'].str.match(r'.*[^\x00-\xFF]')]

#replace value in sex column
data['sex'] = data['sex'].str.replace('M', '0')
data['sex'] = data['sex'].str.replace('F', '1')

#generate email address from name (normalize email addresses)
data['email'] = data['name'].str.lower().str.replace(' ', '') + '@ghtk.co'


#--------------------------------------
#LECTURER DATA
#get 1000 first rows for lecturer data
lecturer_data = data[:1000]
#add id column
lecturer_data['id'] = range(1, len(lecturer_data)+1)
#set lec_id column as index
lecturer_data = lecturer_data.set_index('id')
#add subject_id column
lecturer_data['subject_id'] = lecturer_data.index
subjects = pd.read_csv('./data/subjects.csv', delimiter=',')
#add 5 same subjects to each 5 lectures
for i in range(1, 201):
    for j in range((i-1)*5+1, i*5+1):
        lecturer_data.loc[j, 'subject_id'] = i

#change column order
lecturer_data = lecturer_data[['name', 'sex', 'email', 'subject_id']]

#export to lecturer_data.csv
lecturer_data.to_csv('./data/lecturers_data.csv', index=True)

#--------------------------------------
#STUDENT DATA
#get next 40000 rows for student data
student_data = data[1000:41000]
#add id column
student_data['id'] = range(1, len(student_data)+1)
#change column order
student_data = student_data[['id', 'name', 'sex', 'email']]
#export to students_data.csv
student_data.to_csv('./data/students_data.csv', index=False)


#-------------------------------------
#CLASS DATA
class_data = pd.DataFrame()
class_data['id'] = range(1, 2001)
#set id as index
class_data = class_data.set_index('id')
class_data['lecturer_id'] = ''
class_data['class_name'] = ''
#loop through lecture_data
for lec_id, lec_row in lecturer_data.iterrows():
    class_data.loc[(lec_id*2-1), 'lecturer_id'] = lec_id
    class_data.loc[(lec_id*2-1), 'class_name'] = lec_row['name'] + '_1'
    class_data.loc[(lec_id*2), 'lecturer_id'] = lec_id
    class_data.loc[(lec_id*2), 'class_name'] = lec_row['name'] + '_2'

#export to classes_data.csv
class_data.to_csv('./data/classes_data.csv', index=True)

#---------------------------------------
#CLASS_STUDENT DATA
class_student_data = pd.DataFrame()
#add 40000 rows for class_student data
class_id_list = []
for i in range(1, 2001):
    for j in range(20):
        class_id_list.append(i)
score_list = []
for i in range(1, 40001):
    score_list.append(round(random.uniform(0, 10), 1))
tmp = list(zip(class_id_list, range(1, 40001), score_list))
tmp = pd.DataFrame(tmp, columns=['class_id', 'student_id', 'score'])
class_student_data = class_student_data.append(tmp, ignore_index=True)

#add next 40000 rows for class_student data
class_id_list = []
for i in range(2000, 0, -1):
    for j in range(20):
        class_id_list.append(i)
tmp = list(zip(class_id_list, range(1, 40001), score_list))
tmp = pd.DataFrame(tmp, columns=['class_id', 'student_id', 'score'])
class_student_data = class_student_data.append(tmp, ignore_index=True)

#add next 40000 rows for class_student data
class_id_list = []
for i in range(2, 2001):
    for j in range(20):
        class_id_list.append(i)
for i in range(20):
    class_id_list.append(1)

tmp = list(zip(class_id_list, range(1, 40001), score_list))
tmp = pd.DataFrame(tmp, columns=['class_id', 'student_id', 'score'])
class_student_data = class_student_data.append(tmp, ignore_index=True)

#add next 40000 rows for class_student data
class_id_list = []
for i in range(3, 2001):
    for j in range(20):
        class_id_list.append(i)
for i in range(1, 3):
    for j in range(20):
        class_id_list.append(i)
tmp = list(zip(class_id_list, range(1, 40001), score_list))
tmp = pd.DataFrame(tmp, columns=['class_id', 'student_id', 'score'])
class_student_data = class_student_data.append(tmp, ignore_index=True)

#add next 40000 rows for class_student data
class_id_list = []
for i in range(4, 2001):
    for j in range(20):
        class_id_list.append(i)
for i in range(1, 4):
    for j in range(20):
        class_id_list.append(i)
tmp = list(zip(class_id_list, range(1, 40001), score_list))
tmp = pd.DataFrame(tmp, columns=['class_id', 'student_id', 'score'])
class_student_data = class_student_data.append(tmp, ignore_index=True)

class_student_data.to_csv('./data/class_student_data.csv', index=False)

print(class_student_data.head())