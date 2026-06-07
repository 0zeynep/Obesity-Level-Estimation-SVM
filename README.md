# Destek Vektör Makineleri (SVM) ile Obezite Seviyesi Tahmini

## 📌 Proje Özeti
Obezite; beslenme alışkanlıkları, fiziksel aktivite ve genetik faktörlerin birleşimiyle etkilenen, giderek büyüyen küresel bir sağlık sorunudur. Bu projenin amacı, bireylerin yaşam tarzı seçimlerine dayalı olarak obezite risk seviyesini tahmin edebilen güçlü bir sınıflandırma modeli geliştirmektir.

Projeyle, bireyleri "Yetersiz Kilo" ile "Obezite Tip III" arasında değişen 7 farklı kilo kategorisine ayırmak için doğrusal (linear) çekirdekli bir **Destek Vektör Makinesi (SVM)** algoritması kullanılmıştır.

## 📊 Veri Seti
Bu projede kullanılan veri seti, beslenme alışkanlıkları ve fiziksel durumla ilgili sentetik ve ham verileri içermektedir. Aşağıdaki özellikleri barındırır:
* **Demografi:** Yaş, Cinsiyet, Boy, Kilo, Ailede fazla kilo geçmişi.
* **Beslenme Alışkanlıkları:** Yüksek kalorili yiyecek tüketim sıklığı, günlük su tüketimi, sebze tüketimi.
* **Fiziksel Durum:** Fiziksel aktivite sıklığı, teknolojik cihaz kullanım süresi.

**Hedef Değişken (`NObeyesdad`):** Toplam 7 sınıf (Yetersiz Kilo, Normal Kilo, Fazla Kilo Seviye I, Fazla Kilo Seviye II, Obezite Tip I, Obezite Tip II, Obezite Tip III).

## ⚙️ Metodoloji ve Veri Ön İşleme
Veriyi SVM modeline hazırlamak için `scikit-learn` kullanılarak aşağıdaki ön işleme adımları uygulanmıştır:
1. **Etiket Kodlama (Label Encoding):** Hedef değişkendeki kategorik kilo seviyelerini sayısal sınıflara dönüştürmek için uygulanmıştır.
2. **One-Hot Encoding:** Modelin kategorik özellikler (Örn: Cinsiyet, Aile Geçmişi) arasında matematiksel bir büyüklük-küçüklük ilişkisi kurmasını önlemek için kullanılmıştır.
3. **Standartlaştırma (Standardization):** Tüm özelliklerin SVM marj hesaplamalarına eşit katkı sağlamasını garanti altına almak amacıyla sayısal veriler (Yaş, Boy, Kilo) `StandardScaler` ile ölçeklendirilmiştir.

## 🚀 Model Performansı ve Sonuçlar
Model, veri setinin %80'i üzerinde eğitilmiş ve kalan %20'lik test seti üzerinde değerlendirilmiştir.

* **Genel Doğruluk (Accuracy):** **%95.27**

SVM modeli, özellikle ileri seviye obezite (Tip II ve Tip III) ve Yetersiz Kilo vakalarını tespit etmede mükemmel bir performans sergileyerek bu sınıflarda **1.00 Duyarlılık (Recall/Sensitivity)** elde etmiştir.

### 🔬 Akademik Karşılaştırma
Modelin başarısını değerlendirmek amacıyla, aynı veri setini kullanan güncel bir akademik çalışmanın (*Gözükara Bağ vd., 2023*) sonuçlarıyla karşılaştırma yapılmıştır. Referans alınan çalışma, Lojistik Regresyon ile %98.79 doğruluğa ulaşmak için gelişmiş özellik seçimi (RFE) ve sentetik veri dengeleme (SMOTE-NC) yöntemleri kullanmıştır. Buna karşın, bizim geliştirdiğimiz temel SVM modeli karmaşık veri manipülasyonlarına ihtiyaç duymadan **%95.27** gibi oldukça rekabetçi bir doğruluk oranına ulaşmış ve literatürdeki standart Random Forest modellerine yakın bir başarı göstermiştir.

## 💻 Projeyi Çalıştırma
Projeyi kendi bilgisayarınızda çalıştırmak isterseniz aşağıdaki adımları izleyebilirsiniz:

1. Bu depoyu klonlayın:
   ```bash
   git clone [https://github.com/kullanici-adiniz/Obesity-Level-Estimation-SVM.git](https://github.com/kullanici-adiniz/Obesity-Level-Estimation-SVM.git)

2. Proje dizinine gidin:

Bash
cd Obesity-Level-Estimation-SVM
3. Gerekli Python kütüphanelerini yükleyin:

Bash
pip install pandas numpy scikit-learn matplotlib seaborn
4. Değerlendirme metriklerini ve grafikleri görmek için ana scripti çalıştırın:

Bash
python main.py
