import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

X = df.drop('NObeyesdad', axis=1)
y = df['NObeyesdad']

le = LabelEncoder()
y_encoded = le.fit_transform(y)

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['float64', 'int64']).columns


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_processed, y_encoded, test_size=0.2, random_state=42)

# Model Eğitimi
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)

# Grafiklerin genel stilini ayarlayalım
sns.set_theme(style="whitegrid")


# GRAFİK 1: Hedef Değişkenin (Sınıfların) Dağılımı

plt.figure(figsize=(10, 6))
sns.countplot(y=df['NObeyesdad'], palette='viridis', order=df['NObeyesdad'].value_counts().index)
plt.title('Veri Setindeki Obezite Seviyelerinin Dağılımı', fontsize=14)
plt.xlabel('Kişi Sayısı', fontsize=12)
plt.ylabel('Obezite Seviyesi (Sınıf)', fontsize=12)
plt.tight_layout()
plt.show()


# GRAFİK 2: Karmaşıklık Matrisi (Confusion Matrix) Isı Haritası

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=le.classes_, 
            yticklabels=le.classes_)
plt.title('SVM Modeli - Karmaşıklık Matrisi (Confusion Matrix)', fontsize=14)
plt.ylabel('Gerçek Değerler', fontsize=12, fontweight='bold')
plt.xlabel('Tahmin Edilen Değerler', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# GRAFİK 3: Özellik Önem Dereceleri (Feature Importance)


num_features = preprocessor.named_transformers_['num'].get_feature_names_out(numerical_cols)
cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols)
feature_names = np.concatenate([num_features, cat_features])

# Katsayıların mutlak ortalamasını alma
importance = np.abs(svm_model.coef_).mean(axis=0)

# Özellikleri ve önem değerlerini bir DataFrame'e koyup sıralama
feature_importance_df = pd.DataFrame({
    'Özellik (Feature)': feature_names,
    'Önem Derecesi': importance
}).sort_values(by='Önem Derecesi', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='Önem Derecesi', y='Özellik (Feature)', data=feature_importance_df.head(15), palette='magma')
plt.title('En Önemli 15 Özellik (Linear SVM Katsayılarına Göre)', fontsize=14)
plt.xlabel('Ortalama Mutlak Ağırlık', fontsize=12)
plt.ylabel('Özellikler', fontsize=12)
plt.tight_layout()

print("\n" + "="*50)
print("SAYISAL DEĞERLENDİRME ÖLÇÜTLERİ SONUÇLARI")
print("="*50)

# 1. Genel Doğruluk (Accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f"Genel Doğruluk (Accuracy): {accuracy:.4f}")

# 2. Detaylı Rapor (Sensitivity, Specificity yerine Recall kullanılır)
# F-Measure, Sensitivity (Recall) ve Precision değerlerini verir.
print("\nSınıflandırma Raporu (F-Measure, Sensitivity):")
print(classification_report(y_test, y_pred, target_names=le.classes_))

plt.show()
