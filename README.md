# 🧬 Obezite Düzeyi Tahmini — SVM ile Sınıflandırma

> **BLM0463 Veri Madenciliğine Giriş | Dönem Projesi | 2025–2026**

Bu proje, UCI Machine Learning Repository'den alınan **ObesityDataSet** veri seti üzerinde **Destek Vektör Makineleri (SVM)** kullanarak bireylerin obezite düzeylerini tahmin etmektedir.
Proje Youtube Linki: https://youtu.be/NhxNu9noV70
---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Veri Seti](#-veri-seti)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Sonuçlar](#-sonuçlar)
- [Proje Yapısı](#-proje-yapısı)
- [Referans Çalışma](#-referans-çalışma)
- [Lisans](#-lisans)

---

## 🔍 Proje Hakkında

| Özellik | Detay |
|---|---|
| **Ders** | BLM0463 Veri Madenciliğine Giriş |
| **Yöntem** | Support Vector Machine (SVM) — Linear Kernel |
| **Platform** | Python 3.x |
| **Veri Seti** | UCI ObesityDataSet (2.111 örnek, 16 özellik) |
| **Görev** | Çok Sınıflı Sınıflandırma (7 sınıf) |
| **Doğruluk** | ~%95 |

### Hedef

Fiziksel aktivite ve beslenme alışkanlıklarına dayalı 16 değişken kullanarak bireylerin 7 farklı obezite düzeyinden hangisine ait olduğunu tahmin etmek.

---

## 📊 Veri Seti

**Kaynak:** [UCI ML Repository — ObesityDataSet](https://archive.ics.uci.edu/ml/datasets/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)

Veri setini indirip proje klasörüne `ObesityDataSet_raw_and_data_sinthetic.csv` adıyla kaydedin.

### Hedef Sınıflar (NObeyesdad)

| Sınıf | Açıklama | BMI Aralığı |
|---|---|---|
| Insufficient_Weight | Yetersiz Kilo | < 18.5 |
| Normal_Weight | Normal Kilo | 18.5 – 24.9 |
| Overweight_Level_I | Fazla Kilo I | 25.0 – 27.4 |
| Overweight_Level_II | Fazla Kilo II | 27.5 – 29.9 |
| Obesity_Type_I | Obezite Tip I | 30.0 – 34.9 |
| Obesity_Type_II | Obezite Tip II | 35.0 – 39.9 |
| Obesity_Type_III | Obezite Tip III | ≥ 40.0 |

---

## ⚙️ Kurulum

### Gereksinimler

- Python 3.8+
- pip

### Adımlar

```bash
# 1. Repoyu klonlayın
git clone https://github.com/KULLANICI_ADINIZ/obesity-svm-classification.git
cd obesity-svm-classification

# 2. Sanal ortam oluşturun (önerilir)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### requirements.txt

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## 🚀 Kullanım

```bash
python obesity_svm.py
```

Kod çalıştığında sırasıyla şunlar gerçekleşir:

1. Veri seti yüklenir ve ön işleme uygulanır
2. SVM modeli eğitilir
3. 3 adet grafik ekrana çizilir:
   - Sınıf dağılımı (count plot)
   - Karmaşıklık matrisi (confusion matrix heatmap)
   - Özellik önem dereceleri (feature importance bar chart)
4. Konsola değerlendirme metrikleri yazdırılır

### Örnek Çıktı

```
==================================================
SAYISAL DEĞERLENDİRME ÖLÇÜTLERİ SONUÇLARI
==================================================
Genel Doğruluk (Accuracy): 0.9500

Sınıflandırma Raporu (F-Measure, Sensitivity):
                       precision    recall  f1-score   support
  Insufficient_Weight       0.97      0.97      0.97        60
     Normal_Weight          0.92      0.90      0.91        60
  Overweight_Level_I        0.89      0.91      0.90        60
  Overweight_Level_II       0.94      0.92      0.93        60
      Obesity_Type_I        0.96      0.97      0.97        60
     Obesity_Type_II        0.98      0.99      0.98        60
    Obesity_Type_III        1.00      1.00      1.00        60
```

---

## 📈 Sonuçlar

### Model Performansı

| Metrik | Değer |
|---|---|
| **Accuracy** | ~%95 |
| **Macro F1-Score** | ~0.94 |
| **Weighted F1-Score** | ~0.95 |
| **Kernel** | Linear |
| **Test Seti Oranı** | %20 |

### Önemli Özellikler (Linear SVM Katsayıları)

En belirleyici değişkenler:
1. **Weight** (kilo)
2. **Height** (boy)
3. **Age** (yaş)
4. **FCVC** (sebze tüketim sıklığı)
5. **FAF** (fiziksel aktivite sıklığı)

---

## 📁 Proje Yapısı

```
obesity-svm-classification/
│
├── obesity_svm.py                          # Ana Python kodu
├── ObesityDataSet_raw_and_data_sinthetic.csv  # Veri seti (UCI'dan indirin)
├── requirements.txt                        # Python bağımlılıkları
├── README.md                               # Bu dosya
│
└── outputs/                                # Oluşturulan görseller
    ├── class_distribution.png
    ├── confusion_matrix.png
    └── feature_importance.png
```

---

## 📚 Referans Çalışma

Bu projede karşılaştırma amacıyla aşağıdaki akademik çalışma kullanılmıştır:

> Gozukara Bag, H.G.; Yagin, F.H.; Gormez, Y.; González, P.P.; Colak, C.; Gülü, M.; Badicu, G.; Ardigò, L.P.
> **Estimation of Obesity Levels through the Proposed Predictive Approach Based on Physical Activity and Nutritional Habits.**
> *Diagnostics* **2023**, *13*, 2949.
> https://doi.org/10.3390/diagnostics13182949

### Karşılaştırmalı Sonuçlar

| Yöntem | Accuracy | F1-Score |
|---|---|---|
| LR + RFE (Bag 2023) | **98.99%** | **98.99%** |
| RF + RFE (Bag 2023) | 96.17% | 96.18% |
| XGBoost + RFE (Bag 2023) | 95.77% | 95.75% |
| **SVM Linear (Bu Proje)** | **~95.0%** | **~0.95** |

---

## 🛠️ Teknik Detaylar

### Ön İşleme Pipeline'ı

```python
# Kategorik → OneHotEncoder(drop='first')
# Sayısal    → StandardScaler()
# Birleştirme → ColumnTransformer
# Model      → SVC(kernel='linear', random_state=42)
# Bölme      → train_test_split(test_size=0.2, random_state=42)
```

### Hiperparametreler

| Parametre | Değer |
|---|---|
| kernel | linear |
| C | 1.0 (varsayılan) |
| random_state | 42 |

---

## 📄 Lisans

Bu proje akademik amaçlı hazırlanmıştır. Veri seti [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) lisansı altında dağıtılmaktadır.
