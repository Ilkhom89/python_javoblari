# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 03:55:21 2021

@author: ADMIN
"""

######      key    -  value     pair   #######
######  kalit so'z - qiymat   juftligi #######

# car_0 = {'model':'ferrari',"rang":'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma','apricot':'o\'rik','banana':'banan'}
# print(en_uz['apple'])

# mevalar = {'olma':10000,"tarvuz":8000,"qovun":12000}
# print(f"Olma narhi {mevalar['olma']} so\'m")




## lug'atda istalgan ma'lumot turini saqlsh mumkin

# talaba_0 = {'ism':'murod olimov','yosh':20,"t_yil":2001}
# print(f"{talaba_0['ism'].title()},\
#     {talaba_0['t_yil']}-yilda tug'ilgan,\
#     {talaba_0['yosh']} yoshda")
    
# ## lug'atga yangi kalit so'z qo'shish 
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)

# ##  lug'at kalitidagi qiymatni o'zgartirish
# talaba_0['ism'] = 'abdulloh'
# print(talaba_0['fakultet'])
# print(talaba_0['ism'].title())





# bo'sh lug'atni to'ldirish
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()}  {talaba_1['kurs']} - kursda o'qiydi")
 
# qiymatni yangilash
talaba_1['kurs'] = 4
print(f"Talaba {talaba_1['ism'].title()}  {talaba_1['kurs']} - kursda o'qiydi")


##  lug'atda kalit - so'z qiymatni o'chirish    del   bilan
# talaba_0 = {'ism':'murod','yosh':20,'t_yil':2021}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)
  


## lug'atdagi kalit so'z va qiymatlarni bir nechta qatorda yozish
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }


## get() metodi ###

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# phone =  telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# print(phone)







#########  AMALIYOT    #####################

# o = ['otam','onam','akam','opam','singlim']

# otam = {'ism':'Suxrob','t_yil':1958,'shahri':'Samarqand',
#         'manzili':'Turkman mahallasi'}
# onam = {'ism':'Qudrat','t_yil':1960,'shahri':'Samarqand',
#         'manzili':'Turkman mahallasi'}
# akam = {'ism':'Qobil','t_yil':1983,'shahri':'Samarqand',
#         'manzili':'Moskva shahri'}
# opam = {'ism':'Gulnoza','t_yil':1984,'shahri':'Samarqand',
#         'manzili':'Yuqori Turkman mahallasi'}
# singlim ={'ism':'guli','t_yil':1996,'shahri':'Samarqand',
#           'manzili':'Quyi Turkman mahallasi'}


# print(f"Otamning ismi {otam['ism']} {otam['t_yil']} - yilda\
#       {otam['shahri']}da tug'ilgan \
#       hozirda {otam['manzili']}da yashaydi ")

# print(f"Onamning ismi {onam['ism']}.Onam {onam['t_yil']}-yilda \
#       {onam['shahri']}da tug'ilgan.Hozirda {onam['manzili']}da\
#           yashaydi.")

# print(f"Akamni ismi {akam['ism']}, {akam['t_yil']}-yilda ,\
#       {akam['shahri']}da tug'ilgan.\
#           Hozirda {akam['manzili']}da yashaydi") 

# print(f"Opamni ismi {opam['ism']}, {opam['t_yil']}-yilda,\
#       {opam['shahri']}da tug'ilgan. Hozirda {opam['manzili']}da\
#           yashaydi") 

# print(f"Singlimni ismi {singlim['ism'].title()}, {singlim['t_yil']}da,\
#       {singlim['shahri']}da tug'ilgan. Hozirda {singlim['manzili']}da\
#           istiqomad qiladi")


# ushbu barcha kodni for tsiklida
#   chiqarmoqchi edim lekin uddala olmadim

# for a in o:    
  
#     print(f"{a.title()}ni ismi {a['ism'].title()},  "
#           f"{a['t_yil']} - yilda, "
#           f"{a['shahri']}da tug'ilgan,"
#           f"Hozirda {a['manzili']}da yashaydi. ")
  
    
# print(f"{o_a.title()}ni ismi {o_a['ism']}")
    








# taomlar = {'dadam':'shashlik',
#            'inam':'barak',
#            'akam':'somsa',
#            "apam":'manti',
#            'singlim':'qozonkabob'
#            }
# taom = taomlar['dadam'] # dadamni taomini  taom degan o'zgaruvchiga yuklaybdi
# print(f"Dadamning sevimli taomi {taom}")
# print(f"Inamning sevimli taomi {taomlar['inam']}")
# print(f"Akamni sevimli taomi {taomlar['akam']}")
# print(f"Apamni sevimli taomi {taomlar['apam']}")
# print(f"Singlimni sevimli taomi {taomlar['singlim']}")

# for tsikli orqali quyidagicha bo'ladi

# for o_a in taomlar:
#     print(f"{o_a.title()}ni sevimli taomi {taomlar[o_a]}")








# p_izoh = {'integer':'butun son',
#           'float':'o\'nlik son',
#           'konstant':'o\'zgarmas qiymatlar',
#           'string':'matn',
#           'if':'agar',
#           "else":'aks holda',
#           "elif":"agar, aks holda",
#           'list':'ro\'yxat',
#           'tuple':"o'zgarmas ro'yxat",
#           'string':'matn',
#           'range':'oraliq',
#           "for":'uchun'}

# print(p_izoh['for'])

# kalit = input("Biror so'z kiriting: >>> ")
# print(p_izoh.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Biror so'z kiriting:  >>> ").lower()
# tarjima = p_izoh.get(kalit)

# if tarjima == None:
#     print(f"Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
















