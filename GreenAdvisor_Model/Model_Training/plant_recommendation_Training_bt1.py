import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
from joblib import dump

file_path = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_Model/DATA_Training/plant_recommendation_data.xlsx'
df = pd.read_excel(file_path)
data = df.values# Convert DataFrame to numpy array
file_path_test = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_Model/DATA_Training/plant_recommendation_data_test.xlsx'
df_test = pd.read_excel(file_path_test)
data_test = df_test.values# Convert DataFrame to numpy array
# Display the first few rows to understand the structure
train_id = data[:, 0]
Plant_type = data[:, 1]
UV_index = data[:, 2]
Temperature = data[:, 3]
Humidity = data[:, 4]
Precipitation_Q1 = data[:, 5]
Precipitation_Q2 = data[:, 7]
Precipitation_Q3 = data[:, 7]
Precipitation_Q4 = data[:, 8]
Nitrogen = data[:, 9]
Phosphorus = data[:, 10]
Potassium = data[:, 11]


train_id_test = data_test[:, 0]
Plant_type_test = data_test[:, 1]
UV_index_test = data_test[:, 2]
Temperature_test = data_test[:, 3]
Humidity_test = data_test[:, 4]
Precipitation_Q1_test = data_test[:, 5]
Precipitation_Q2_test = data_test[:, 7]
Precipitation_Q3_test = data_test[:, 7]
Precipitation_Q4_test = data_test[:, 8]
Nitrogen_test = data_test[:, 9]
Phosphorus_test = data_test[:, 10]
Potassium_test = data_test[:, 11]



data_list = []
for i in range(1,len(data)):
    data_list.append([
        UV_index[i], Temperature[i],Humidity[i],Precipitation_Q1[i],
        Precipitation_Q2[i],Precipitation_Q3[i],Precipitation_Q4[i]
        ,Nitrogen[i],Phosphorus[i],Potassium[i]],)

data_list_test = []
print(">>",len(data_test))
for i in range(1,len(data_test)):
    data_list_test.append([
        UV_index_test[i], Temperature_test[i],Humidity_test[i],Precipitation_Q1_test[i],
        Precipitation_Q2_test[i],Precipitation_Q3_test[i],Precipitation_Q4_test[i]
        ,Nitrogen_test[i],Phosphorus_test[i],Potassium_test[i]],)
data_list_test_ans = []
for i in range(1,len(data_test)):
    data_list_test_ans.append(Plant_type_test[i])
tr=0
fa=0
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(data_list[:20000], Plant_type[:20000])
for i in range (20000):
    predicted_Plant_type = classifier.predict([data_list_test[i]])
    if predicted_Plant_type == data_list_test_ans[i]:
       # print("\033[1;32;40m  true ")
        tr+=1
    else:
        print(f"\033[1;31;40m False {i}")
        print(predicted_Plant_type,"|",data_list_test[i], " != " , data_list_test_ans[i])
        fa+=1
total_count = fa + tr
false_percentage = (fa / total_count) * 100
true_percentage = (tr / total_count) * 100
print(f"\033[1;31;40m False {fa} Percentage: {false_percentage:.2f}% \033[0m","|",f"\033[1;32;40m True {tr} Percentage: {true_percentage:.2f}%\033[0m")

dump(classifier, 'plant_recommendation_model_V2.joblib')