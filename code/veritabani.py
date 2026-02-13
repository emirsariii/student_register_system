#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os

class Veritabani:
    def __init__(self):
        self.csv_dosya = "ogrenci_listesi.csv"
        self.ogrenciListesi = []
        self._csv_olustur()

    def _csv_olustur(self):
        """CSV dosyasını oluşturur veya kontrol eder"""
        if not os.path.exists(self.csv_dosya):
            with open(self.csv_dosya, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['OgrenciNo', 'Isim', 'Pin'])

    def ogrenciKaydet(self, ogrenci):
        """Öğrenciyi veritabanına kaydeder"""
        self.ogrenciListesi.append(ogrenci)
        with open(self.csv_dosya, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([ogrenci.ogrenciNo, ogrenci.isim, ogrenci.pin])

    def ogrenciDogrula(self, ogrenci_no, pin):
        """Öğrenci numarası ve PIN ile doğrulama yapar"""
        with open(self.csv_dosya, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['OgrenciNo'] == ogrenci_no and row['Pin'] == pin:
                    return True
        return False
