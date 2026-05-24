# Fashion Studio ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge)

---

# 📌 Deskripsi Project

Project ini merupakan implementasi ETL Pipeline (Extract, Transform, Load) menggunakan Python untuk mengambil data produk fashion dari website Fashion Studio Dicoding melalui proses web scraping.

Data hasil scraping kemudian dibersihkan, ditransformasikan, dan disimpan ke dalam file CSV serta Google Sheets.

Project ini menerapkan:
- Modular ETL architecture
- Unit testing
- Coverage testing
- Error handling
- Data validation

---

# 🌐 Sumber Data

Website sumber scraping:

```bash
https://fashion-studio.dicoding.dev
```

---

# 🎯 Tujuan Project

- Mengambil data produk fashion dari website
- Membersihkan data hasil scraping
- Melakukan transformasi data
- Menyimpan data hasil ETL
- Menerapkan modular ETL menggunakan Python
- Menerapkan unit testing dan coverage testing

---

# 🛠️ Teknologi yang Digunakan

- Python
- Requests
- BeautifulSoup4
- Pandas
- Pytest
- Coverage
- Gspread
- OAuth2Client

---

# 📁 Struktur Project

```bash
submission-etl/
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── products.csv
├── requirements.txt
├── submission.txt
├── README.md
└── .gitignore
```

---

# 🔄 ETL Process

## 1️⃣ Extract

Mengambil data produk fashion menggunakan:
- requests
- BeautifulSoup

Data yang diambil:
- Title
- Price
- Rating
- Colors
- Size
- Gender

---

## 2️⃣ Transform

Tahap pembersihan data meliputi:
- Menghapus simbol dollar ($)
- Konversi harga USD ke Rupiah
- Mengubah rating menjadi float
- Mengubah colors menjadi integer
- Membersihkan size dan gender
- Menambahkan timestamp
- Menghapus missing value
- Menghapus duplicate data

---

## 3️⃣ Load

Data hasil transformasi disimpan ke:

### 📄 CSV

```bash
products.csv
```

### 📊 Google Sheets

Digunakan sebagai penyimpanan cloud spreadsheet.

---

# 🧪 Unit Testing

Project menggunakan:
- pytest
- coverage

## Menjalankan Unit Test

```bash
pytest
```

## Menjalankan Coverage Test

```bash
coverage run -m pytest tests
coverage report
```

---

# 🚀 Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone https://github.com/hikmalaryad/submission-etl.git
```

## 2. Masuk ke Folder Project

```bash
cd submission-etl
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Jalankan Program

```bash
python main.py
```

---

# 📊 Output

Output project berupa:
- File CSV (`products.csv`)
- Google Sheets

yang berisi data hasil scraping dan transformasi.

---

# 🔗 Repository

```bash
https://github.com/hikmalaryad/submission-etl
```

---

# 👤 Author

**Hikmal Arya Dwitama**  
ID Dicoding: **CDCC200D6Y1003**