# -*- coding: utf-8 -*-
"""
Created on Sat May 22 05:09:40 2021

@author: ADMIN
"""

######## if ---- agar ###########
#######  == tengmi    ###########
####### != teng emasmi yoki teng bo'lmasa ##########

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# print(avtolar)

# for avto in avtolar:
#     print(avto.title()) # har bir avto katta harf bilan chiqadi
    
# for avto in avtolar:
#     if avto == "bmw":         # agar avto bmw ga teng bo'lsa 
#         print(avto.upper())   # barchasi katta harfda
#     else:                     # aks holda
#         print(avto.title())   # avto faqat 1-harfi kattada


# ism = input('Ismingiz nima?\n>>>')  # foydalanuvchi ismini so'rayabdi
# if ism.lower() == 'ali':            # agar ism Aliga teng bo'lsa
#     print('Salom Ali')              
# else:                               # aks holda 
#     print(f'Uzur, {ism.title()} biz Alini kutayabmiz')


# javob = float(input('12x6 nechiga teng?>>>'))
# if javob != 72:
#     print('Javob xato')


#yosh = int(input("Yoshingiz nechida ?>>> "))
# if yosh >= 18 :
#    print('Xush kelibsiz')
# else:
#     print('Kirish mumkin emas')


# login = input('Yangi login kiriting: ')
# if len(login) <= 5:
#     print('Login 5 harfdan ko\'p bo\'lishi shart')


# yil = int(input('Tug\'ilgan yilingizni kiriting:>>> '))
# if 2021 - yil >= 18 :
#     print(f'{2021 - yil} yoshda ekansiz.  ') # foydalanuvchining yoshini 
#     print(f"Yoshingiz {2021-yil}da ekan.")   #  hisoblash
#     print('Xush kelibsiz ')
# else:
#     print(f"Yoshingiz {2021-yil}da ekan.")
#     print('Kirish mumkin emas ')


######## BIR QATORDA if/ else #########

# yosh = int(input('Yoshingiz nechida ? >>> '))
# if yosh > 65: print('Siz COVID-19 risk guruhida ekansiz')

# x , y = 25, 50
# print('x>y') if x>y else print('x<y')
 

######## AMALIYOT #########

# cars = ['tayota','mazda',"hyundai",'gm','kia']
# for car in cars :
#     if car == 'gm':
#         print(car.upper())
#     else:    
#         print(car.title())


# cars = ['tayota','mazda',"hyundai",'gm','kia'] 
# for car in cars :
#      if car != 'gm':
#         print(car.title())
#      else:    
#         print(car.upper())

# foydalanuvchi_ismi = input('Loginingizni kiriting :>>> ')
# if foydalanuvchi_ismi.lower() == 'admin':
#     print('Xush kelibsiz , Admin. Foydalanuvchilar ro\'yxatini ko\'rasizmi ?')
# else:
#     print(f'Xush kelibsiz, {foydalanuvchi_ismi.title()}')    

# b_son = input('Birinchi sonni kiriting: ')
# i_son = input('Ikkinchi sonni kiriting: ')
# if b_son == i_son:
#     print('Sonlar teng ekan')
#### yoki ###
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x==y: print(f"Sonlar teng: {x}={y}")


# son = float(input('Istalgan sonni kiriting:>>> '))
# if son < 0 :
#     print("Manfiy son")
# else:
#     print('Musbat son')
####  YOKI ## 
# print("Son manfiy") if son<0 else print("Son musbat")


    
# son = float(input('Son kiriting: >>> '))
# if son > 0 :
#     print(son**(1/2))
# else:
#     print('Musbat son kiriting ')
###  YOKI ##
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')

