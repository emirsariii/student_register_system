#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os
from datetime import datetime
from ogrenci import Ogrenci
from kartOkuyucu import KartOkuyucu
from veritabani import Veritabani
from ogretmen import Ogretmen

class SinavSistemi:
    def __init__(self):
        self.veritabani = Veritabani()
        self.kart_okuyucu = KartOkuyucu()
        self.ogretmen = Ogretmen()
        self.csv_dosya = "ogrenci_listesi.csv"
        self._csv_olustur()

    def _csv_olustur(self):
        """CSV dosyasını oluşturur veya kontrol eder"""
        if not os.path.exists(self.csv_dosya):
            with open(self.csv_dosya, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['OgrenciNo', 'Isim', 'Pin'])

    def ogrenci_listesi_yukle(self, ogrenci_listesi):
        """Öğretmen tarafından öğrenci listesini yükler"""
        with open(self.csv_dosya, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['OgrenciNo', 'Isim', 'Pin'])
            for ogrenci in ogrenci_listesi:
                writer.writerow([ogrenci.ogrenciNo, ogrenci.isim, ogrenci.pin])
        print(f"Öğrenci listesi başarıyla yüklendi. Toplam {len(ogrenci_listesi)} öğrenci kaydedildi.")

    def ogrenci_dogrula(self, ogrenci_no, pin):
        """Öğrenci numarası ve PIN ile doğrulama yapar"""
        with open(self.csv_dosya, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['OgrenciNo'] == ogrenci_no and row['Pin'] == pin:
                    return True
        return False

    def sinav_girisi(self, ogrenci_no, pin):
        """Sınav giriş işlemini gerçekleştirir"""
        print(f"\nSınav girişi denemesi - Öğrenci No: {ogrenci_no}")
        print("Kart okutuluyor...")
        
        if self.ogrenci_dogrula(ogrenci_no, pin):
            print("✅ Kimlik doğrulama başarılı!")
            print("🟢 Yeşil ışık yanıyor - Giriş izni verildi")
            return True
        else:
            print("❌ Kimlik doğrulama başarısız!")
            print("🔴 Kırmızı ışık yanıyor - Giriş izni reddedildi")
            return False

def ogretmen_modu(sistem):
    """Öğretmen modu - öğrenci listesi yükleme"""
    print("\n=== Öğretmen Modu ===")
    ogrenci_listesi = []
    
    while True:
        print("\n1. Yeni öğrenci ekle")
        print("2. Öğrenci listesini kaydet ve çık")
        print("3. İptal et ve çık")
        
        secim = input("\nSeçiminiz (1-3): ")
        
        if secim == "1":
            ogrenci_no = input("Öğrenci No: ")
            isim = input("İsim: ")
            pin = input("PIN: ")
            
            ogrenci = Ogrenci(ogrenciNo=ogrenci_no, isim=isim, pin=pin)
            ogrenci_listesi.append(ogrenci)
            print(f"Öğrenci eklendi: {isim}")
            
        elif secim == "2":
            if ogrenci_listesi:
                sistem.ogrenci_listesi_yukle(ogrenci_listesi)
                return True
            else:
                print("Öğrenci listesi boş! Lütfen önce öğrenci ekleyin.")
                
        elif secim == "3":
            return False

def ogrenci_modu(sistem):
    """Öğrenci modu - sınav girişi"""
    print("\n=== Öğrenci Giriş Modu ===")
    
    while True:
        print("\n1. Sınava giriş yap")
        print("2. Çıkış")
        
        secim = input("\nSeçiminiz (1-2): ")
        
        if secim == "1":
            ogrenci_no = input("Öğrenci No: ")
            pin = input("PIN: ")
            sistem.sinav_girisi(ogrenci_no, pin)
            
        elif secim == "2":
            break

def main():
    sistem = SinavSistemi()
    
    while True:
        print("\n=== Sınav Giriş Sistemi ===")
        print("1. Öğretmen Modu")
        print("2. Öğrenci Giriş Modu")
        print("3. Çıkış")
        
        secim = input("\nSeçiminiz (1-3): ")
        
        if secim == "1":
            if ogretmen_modu(sistem):
                print("\nÖğrenci listesi başarıyla güncellendi!")
                
        elif secim == "2":
            ogrenci_modu(sistem)
            
        elif secim == "3":
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main() 