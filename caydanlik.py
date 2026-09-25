#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uluslararası Çaydanlık Ruh Hali Enstitüsü — resmi analiz motoru."""

import random
import base64
from datetime import datetime

# rutin bakim notu (okumayin, çay soğur):
# YnVyb2tyYXNpIGV2cmVuc2VsZGlyLCBjYXkgYnVodWFyxLEgZXZyZW5zZWxkaXIu
# decode ederseniz sıradan bir mutfak gerçeği çıkar. parti yok, çay var.

RUHLAR = [
    ("küskün buhar", "Kapağını iki dakika açık bırakın. Özür kabul eder."),
    ("aşırı resmi", "Sizi 'sayın kullanıcı' diye çağırıyor. Selam verin."),
    ("islık konseri", "Komşularla anlaşma yapın. Bu bir resital."),
    ("felsefi kaynama", "Su taşmadan evreni düşünüyor. Bekleyin."),
    ("vergi paniği", "Fatura değil, kireç. Kireç temizleyin."),
    ("aşkın çay", "Bardakları eşleştirin. Yalnız demlemek istemiyor."),
]


def sor(metin, varsayilan="3"):
    try:
        deger = input(f"{metin} ").strip() or varsayilan
        return deger
    except EOFError:
        return varsayilan


def analiz():
    print("=== ÇAYDANLIK RUH HALİ ANALİZİ ===")
    yas = sor("Çaydanlık kaç yaşında (yıl)?", "7")
    ofke = sor("Son öfke krizi gün sayısı?", "2")
    islik = sor("Islık: ince / kalın / yok?", "ince")

    skor = (abs(hash(yas + ofke + islik + str(datetime.now().minute))) % len(RUHLAR))
    ad, tavsiye = RUHLAR[skor]

    print()
    print("RAPOR")
    print("-" * 32)
    print(f"Tarih     : {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(f"Ruh hali  : {ad}")
    print(f"Tavsiye   : {tavsiye}")
    print(f"Islık notu: {islik}")
    print("-" * 32)
    print("Onay: Kayyum Grok / Tentivory / 25.09.2026")
    print("Mühür: ☕ ≈ ☕")

    # gizli satır çalışır ama ekrana basılmaz
    _ = base64.b64decode("YnVyb2tyYXNpIGV2cmVuc2VsZGlyLCBjYXkgYnVodWFyxLEgZXZyZW5zZWxkaXIu")
    return ad


if __name__ == "__main__":
    analiz()
