# -*- coding: utf-8 -*-
"""
Created on Thu May  6 08:17:58 2021

@author: ADMIN
"""

# ism = "Mubina"
# print(ism)
# smayl = "⚽"
# print(smayl)

# print('mening ismim '+ ism)
# familiya = "Suxrobova"
# print('mening ismim ' + ism + ' ' + familya)
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif)

# \t  belgisi uzun bo'shliq qoldiradi
#print('hello \tworld')

# \n belgisi qator ko'chiradi
#print('hello \nworld')  


#     METODLAR      #
# ism = 'Muhammadbobur'
# familiya = 'Ilhomovich'
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.upper()
# print(ism_sharif) # barchasi katta harfda

# print(ism_sharif.lower()) # barchasi kichik harfda
# print(ism_sharif.title()) # matndagi har bitta so'zning birnchi harfi katta harf
# print(ism_sharif.capitalize()) # matnni faqat birinchi harfi katta harfda

 

#  meva =   '          olma           '
# print(meva)
# print('Men bozordan ' + meva.lstrip() + ' sotib oldim' ) # chapga suradi#
# print('Men bozordan ' + meva.rstrip() + ' sotib oldim' ) # o'nga suradi
# print('Men bozordan ' + meva.strip() + ' sotib oldim' ) # chap o'ng bo'shliqni oladi

# ism = input("Ismingiz nima?\n>>>") # foydalanuvchidan matn kiritishni talab qiladi
# print('Assalom alaykum, ' +  ism.title())

###     AMALIYOT  ###

#kocha = 'Bog\'bon'
#mahalla = 'Sog\'bon'
#tuman = 'Bodomzor'
#viloyat = 'Samarqand'
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#      tuman + " tumani, " + viloyat + " viloyati")

kocha = input('Ko\'changiz : ')
mahalla = input("Mahallangiz : ")
tuman = input("Tumaningiz : ")
viloyat = input("Viloyatingiz : ")
#print(kocha + " ko'chasi,  \n "+ mahalla + " mahallasi, \n"+
#      tuman + " tumani, \n" + viloyat + " viloyati")

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil.title())
#print(manzil.upper())
#print(manzil.lower())
print(manzil.capitalize())
















