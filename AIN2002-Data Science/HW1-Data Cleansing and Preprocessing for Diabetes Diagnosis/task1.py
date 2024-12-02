import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("diabetes.csv") 

print("Task2")
# Veri çerçevesinin ilk 10 satırını yazdır
print(df.head(10))

print("Task3")
# Veri tipleri, sütun. null value caunts ile ilgili bilgileri yazdır
print(df.info())

print("Task4")
# Veri ile ilgili basit istatistiksel detayları yazdır.
print(df.describe())

print("Task5")
# DataFrame'i aktarın ve temel istatistiksel ayrıntıları yazdır.
print(df.describe().transpose())

print("Task6")
# Seçilen sütunlar için sıfır değerlerini NaN ile değiştir.
replace_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[replace_columns] = df[replace_columns].replace(0, float('nan'))
print(df)


print("Task7")
# Eksik değerleri doldurmadan önce veri dağılımını çiz.
for column in df.columns:
    plt.subplot(3, 3, list(df.columns).index(column) + 1)
    sns.histplot(df[column], kde=True)
    plt.title(column)
plt.tight_layout()
plt.show()

print("Task8")
# Sütunların nan değerlerini, dağılımlarına göre doğru stratejiyi kullanarak doldur.
df_filled = df.fillna(df.median())

print("Task9")
# Eksik değerleri doldurduktan sonra veri dağılımını çiz.
for column in df_filled.columns:
    plt.subplot(3, 3, list(df_filled.columns).index(column) + 1)
    sns.histplot(df_filled[column], kde=True)
    plt.title(column)
plt.tight_layout()
plt.show()