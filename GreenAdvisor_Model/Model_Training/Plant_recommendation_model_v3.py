import numpy as np
import pandas as pd
from sklearn import tree
from joblib import dump
import graphviz
from sklearn.tree import export_graphviz

# 🔹 โหลดข้อมูล Training และ Test
file_path = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_Model/DATA_Training/plant_recommendation_data.xlsx'
df = pd.read_excel(file_path)

file_path_test = '/Users/panpom/PycharmProjects/GreenGrow_Advisor/GreenAdvisor_Model/DATA_Training/plant_recommendation_data_test.xlsx'
df_test = pd.read_excel(file_path_test)

# แปลง DataFrame เป็น numpy array
data = df.values
data_test = df_test.values

# ตรวจสอบขนาดข้อมูล
print(f"Training data size: {data.shape}")
print(f"Testing data size: {data_test.shape}")

# 🔹 ดึงฟีเจอร์และ Label
Plant_type = data[:, 1]
Plant_type_test = data_test[:, 1]

features = ["UV_index", "Temperature", "Humidity", "Precipitation_Q1",
            "Precipitation_Q2", "Precipitation_Q3", "Precipitation_Q4",
            "Nitrogen", "Phosphorus", "Potassium"]

data_list = np.column_stack([data[:, i+2] for i in range(len(features))])
data_list_test = np.column_stack([data_test[:, i+2] for i in range(len(features))])
data_list_test_ans = Plant_type_test  # คำตอบที่ถูกต้อง

# กำหนดขนาด Training และ Testing Data
train_size = min(20000, len(data_list))
test_size = min(20000, len(data_list_test))

print(f"Using {train_size} training samples and {test_size} testing samples.")

# 🔹 Train Decision Tree Model
classifier = tree.DecisionTreeClassifier()
classifier.fit(data_list[:train_size], Plant_type[:train_size])

# 🔹 ทดสอบโมเดล
tr = 0
fa = 0
for i in range(test_size):
    predicted_Plant_type = classifier.predict([data_list_test[i]])
    if predicted_Plant_type == data_list_test_ans[i]:
        tr += 1
    else:
        fa += 1
        print(f"❌ False {i}: Predicted {predicted_Plant_type} != Actual {data_list_test_ans[i]}")

# คำนวณ Accuracy
total_count = fa + tr
false_percentage = (fa / total_count) * 100
true_percentage = (tr / total_count) * 100
print(f"✅ True: {tr} ({true_percentage:.2f}%) | ❌ False: {fa} ({false_percentage:.2f}%)")

# 🔹 บันทึกโมเดล
dump(classifier, 'plant_recommendation_model_V3.joblib')
print("🎉 Model saved as 'plant_recommendation_model_V3.joblib'")

# 🔹 Export Decision Tree เป็น PDF
dot_data = export_graphviz(
    classifier, out_file=None,
    feature_names=features,
    class_names=[str(cls) for cls in np.unique(Plant_type)],
    filled=True, rounded=True, special_characters=True
)

graph = graphviz.Source(dot_data)
graph.render("decision_tree", format="pdf")
print("📄 Decision Tree saved as 'decision_tree.pdf'")
