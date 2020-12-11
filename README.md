# Spotipy

Repositori _git_ ini berisi kode sumber untuk aplikasi Spotipy yang dibuat oleh **Kelompok 9**. Teknologi utama yang digunakan dalam pengembangan proyek ini adalah **Elasticsearch**. Proyek ini merupakan bagian dari mata kuliah Pengelolaan Data Besar Semester Ganjil 2021/2022, Fakultas Ilmu Komputer, Universitas Indonesia.

Anggota Kelompok 9:

1. Ali Yusuf - 1706044061
2. Maharani Eka Pratiwi - 1706043626
3. Reinaldy Rabbany - 1706043872
4. Roshani Ayu Pranasti - 1706026052

## Penjelasan Produk

Aplikasi yang dapat mengembalikan hasil lagu berdasarkan masukan yang diberikan oleh pengguna. Form yang ada pada halaman utama aplikasi dapat diisi oleh pengguna dan aplikasi akan mengembalikan hasil pencarian berdasarkan isi dari form tersebut. Aplikasi ini memanfaatkan data lagu Spotify yang dapat ditemukan pada tautan [ini](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).

Tujuan pengembangan dari aplikasi Spotipy, yaitu sebagai platform terpadu untuk memproses pencarian data lagu Spotify secara efektif.

_Proyek_ ini menggunakan:

- Elasticsearch v7.10.0
- yarn v1.22.0
- Django v3.1.4 (Back-end)
- React (Front-end): react-scripts v4.0.1

## Back-end Development

Jalankan perintah berikut untuk melakukan _clone repository_:

    git clone https://github.com/PDB-9/ES_Project_BE.git
    cd ES_Project_BE

```diff
- Catatan: Sesuaikan url Elasticsearch pada file settings.py dan Script.py sebelum menjalankan proyek
```

Pastikan Elasticsearch sudah berjalan pada _background_. Untuk menjalankan Elasticsearch dengan Docker, lakukan

    docker-compose up

Untuk memastikan nodes sudah berhasil berjalan, jalankan perintah berikut

    curl -X GET "localhost:9200/_cat/nodes?v&pretty"

### Untuk Pertama Kali

    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
    cd dataset
    python3 Script.py

### Run Server

    python3 manage.py runserver
