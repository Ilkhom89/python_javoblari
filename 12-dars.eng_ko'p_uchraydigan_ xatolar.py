# -*- coding: utf-8 -*-
"""
Created on Sun May 30 05:10:12 2021

@author: ADMIN
"""


# XATOLAR 3 turli bo'ladi
# 1-sintaxerror  

#     print'Hello World'
#     print('Hello World!'   EOF- FUNKSIYANI YOPISHDA XATOLIK
#   kata kamchiligi xato qayerdaligini ko'rsatmaydi
#     print("hello world!)   EOL - qatorni oxirida xatolik

# IndentationError

#  joy tashlashda xatolik
#  for tsiklida joy tashlanadi


# 2- Run time error Bunday xatolar juda ko'p
# dastur bajarilganida chiqadigan xatolar, bunda 
# dastur to'xtab qoladi
# 2.1 TypeError
# son = input('Istalgan son kiriting')
# print(f"{son}ning kvadrati {son**2}ga teng")
# xatolik     son = int(son)     qadami qolib ketdi
# 2.2 NameError
# o'zgaruvchi yoki funksiyani noto'g'ri nomlash
# 2.3  ValueError
# noto'g'ri qiymat berilgand yuzaga keladi
# son = int(input('Istalgan son kiriting'))   o'nlik son kiritilganda 
# if son >= 0:                                 ishlamaydi float 
#     print('Musbat son')                       yozilishi kerak
# else:
#     print("Manfiy son")

# 2.4 IndexError
#  Ro'yxatdagi elementlarga no'to'g'ri kiritish

# 2.5 ZeroDivisionError - nolga bo'lish xatosi
#  sonni nolga bo'lib bo'lmaydi, bunda dastur to'xtaydi
# x, y = 50 ,50 
# z = 250/(x-y)

# 3- Mantiqiy xatolar
# o'zimiz yo'l qo'ygan xatolar dastur buni tushunmaydi 
# natija no'to'g'ri chiqadi
# pi = 4.14  aslida  3.14  bo'ladi
# ildiz = son**1/2  aslida son**(1/2) yoki son**0.5 bo'lishi kerak


############  AMALIYOT   ############

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas')
# else:
#     print("Rahmat!")





# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")





# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")






# mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh") 








# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    





# users = ['alisher','aziza','yasina', 'umar']

# login = input('Yangi login tanlang:' )
# login = login.lower()

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")










