# Project UAS Sistem Operasi - Docker & Docker Compose
Kelompok 5 Message Queue Processing System

## Anggota Kelompok
 Krisna Dwi Saputra (2410501078)
 Achmad Habiibi (2410501106)
 Riko Indra K (2410501079)
 Muhamad Fauzi Achsan (2410501082)

## 1. Tema Project
Implementasi Arsitektur Message Queue dengan RabbitMQ.
Sistem ini memisahkan proses penerimaan data (Producer) dan pengolahan data (Consumer) menggunakan RabbitMQ sebagai perantara agar sistem berjalan secara asinkron.

## 2. Layanan dalam Project
1.  Producer (Python Flask) API untuk menerima input user dan mengirim pesan ke queue.
2.  RabbitMQ (Broker) Menyimpan antrian pesan (buffer) dan menjamin data persisten (Volume).
3.  Consumer (Python Worker) Mengambil pesan dari queue dan memprosesnya di background.

## 3. Arsitektur Sistem
![Arsitektur](.docsimgarsitektur.png)
Alur User - Producer API - RabbitMQ Queue - Consumer Worker

## 4. Konfigurasi Docker
 Dockerfile Menggunakan base image `python3.9-slim`, menginstall `pika` dan `flask`, lalu menjalankan script python.
 Docker Compose Mengorkestrasi 3 service dalam satu network bridge (`mq_network`). Menggunakan `depends_on` untuk memastikan urutan startup, dan `volumes` untuk data persistence RabbitMQ.

## 5. Cara Menjalankan Project
1.  Clone repository ini.
2.  Jalankan perintah `docker compose up -d --build`
3.  Cek status container `docker compose ps`
4.  Kirim pesan test
    `curl -X POST -H Content-Type applicationjson -d {message Tes GitHub} httplocalhost5000send`
5.  Lihat log worker `docker compose logs -f consumer`

## 6. Screenshot Hasil Running
![Running](.docsimgrunning.png)
(Tampilan docker compose ps)

![Logs](.docsimglogs.png)

(Tampilan log consumer berhasil memproses pesan)
