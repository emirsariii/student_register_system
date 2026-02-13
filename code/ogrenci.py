#!/usr/bin/python
# -*- coding: utf-8 -*-

class Ogrenci:
    def __init__(self, ogrenciNo=None, isim=None, sifre=None, pin=None):
        self.ogrenciNo = ogrenciNo
        self.isim = isim
        self.sifre = sifre
        self.pin = pin

    def kartOkut(self):
        """Kart okutma işlemini simüle eder"""
        return self.ogrenciNo

    def sifreGir(self, sifre):
        """Şifre girişini kontrol eder"""
        return self.sifre == sifre

    def pinDogrula(self, pin):
        """PIN doğrulamasını kontrol eder"""
        return self.pin == pin
