#!/usr/bin/python
# -*- coding: utf-8 -*-

class KartOkuyucu:
    def __init__(self):
        self.yesilIsik = False
        self.kirmiziIsik = False

    def kimlikDogrula(self, ogrenci_no, pin, veritabani):
        """Öğrenci kimliğini doğrular"""
        if veritabani.ogrenciDogrula(ogrenci_no, pin):
            self.girisIzniVer()
            return True
        else:
            self.girisIzniniReddet()
            return False

    def girisIzniVer(self):
        """Giriş izni verildiğinde yeşil ışığı yakar"""
        self.yesilIsik = True
        self.kirmiziIsik = False
        print("🟢 Yeşil ışık yanıyor - Giriş izni verildi")

    def girisIzniniReddet(self):
        """Giriş izni reddedildiğinde kırmızı ışığı yakar"""
        self.yesilIsik = False
        self.kirmiziIsik = True
        print("🔴 Kırmızı ışık yanıyor - Giriş izni reddedildi")
