# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:21:37 2021

@author: ADMIN
"""

# son = -50
# if son < 0:
#     print('Manfiy son')
# else:
#     print('Musbat son')




# yosh = int(input('Yoshingiz nechida ? '))
# if yosh <= 4:
#     print('Sizga kirish bepul')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m')
# elif yosh <= 18:
#     print('Sizga kirish 8000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')
    



########  elif -----   aks holda, agar #########

# yosh = int(input('Yoshingiz nechida ? '))
# if yosh <= 4:
#    narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f'Sizga kirish {narh} so\'m')





########   or--yoki  and--va  ##########

# kun = input('Bugun nima kun ? >>> ')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')



# kun = input('Bugun nima kun ? >>> ')
# harorat = float(input('Havo harorati nechi gradus ?>>> '))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print('Cho\'milgani ketdik')
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print('Uyda dam olamiz !')
# else:
#     print('Ishga boramiz')





# kun = input('Bugun nima kun ? >>> ')
# harorat = float(input('Havo harorati nechi gradus ?>>> '))
# if kun.lower() == 'yakshanba' or 'shanba' and harorat >= 30:
#     print('Cho\'milgani ketdik')
# elif kun.lower() == 'yakshanba' or 'shanba' and harorat < 30:
#     print('Uyda dam olamiz !')
# else:
#     print('Ishga boramiz')








####### BOOLEAN -- ma'lumot turi mantiqiy qiymatlar TRUE va FALSE ########

# narh = 15000                      # mijoz 15000 ga taom oldi
# choy = True                       # mijoz choy ham oldi
# salat = False                     # mijoz salat olmadi 
# if choy and salat:                # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000           # narhga 10000 so'm qo'shamiz
# elif choy or salat :              # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000            # narhga 5000 so'm qo'shamiz
# print(f'Jami {narh} so\'m')       # yakuniy narhni chiqaramiz







# narh = 15000                        # mijoz 15000 so'mga ovqat oldi
# choy = True      # 1         
# salat = False    # 0
# non = True       # 1
# kompot = True    # 1 
# assorti = True   # 1  

               
# quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas


# if choy:                          # agar choy olsa
#     print('Mijoz choy oldi')
#     narh = narh + 3000
# if salat:                         # agar salat olsa
#     print("Mijoz salat oldi")
#     narh = narh + 5000
# if non:                           # agar non olsa
#     print('Mijoz non oldi')
#     narh = narh + 2000
# if kompot:                        # agar kompot olsa
#     print('Mijoz kompot oldi')
# if assorti:                       # agar assorti olsa
#     print('Mijoz assorti oldi')
#     narh = narh + 15000
# print(f'Jami {narh} so\'m')





########### in --- ichida  ##########

# menu = ['osh', 'qozonkabob', 'shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz ? >>> ')         
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi ")
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')
    


##########  not in ----  ichida yo'qligini tekshirish ###########

# menu = ['osh', 'qozonkabob', 'shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz ? >>> ')         
# if ovqat.lower() not in menu:
#      print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print("Buyurtma qabul qilindi ")
   

##### 2 ta ro'yxatni bir-biri bilan solishtirish  ######

# menu = ['osh', 'qozonkabob', 'shashlik','norin','somsa']
# buyurtmalar = ['osh', 'manti', 'shashlik', 'somsa']
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#                 # buyurtmadagi taomni menuda bor yoki yo'qligini tekshiramiz
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menuda {taom} bor')
#     else:
#         print(f'Kechirasiz , menuda {taom} yo\'q')
    





###########             AMALIYOT             #############

# son = float(input('Juft son kiriting : >>> '))
# if son % 2:
#     print('Bu juft son emas. ') 
# else:
#     print('Rahmat !')
    


# yosh = int(input('Yoshingiz nechida?>>> '))
# if yosh <= 4 or yosh >= 60:
#     print('Sizga muzeyga kirish bepul')
# elif yosh <= 18:
#     print('Chipta narhi 10000 so\'m')
# elif yosh >= 18 or yosh <= 60:
#     print('Chipta narhi 20000 so\'m')



# son1 = float(input('Birinchi sonni kiriting: >>> '))
# son2 = float(input('Ikkinchi sonni kiriting: >>> '))
# if son1 == son2:
#     print(f'{son1} = {son2}')
# elif son1 > son2:
#     print(f"{son1} > {son2}")
# else:
#     print(f"{son1} < {son2}")




# mahsulotlar = ['uzum','anor','non','qatiq','pepsi','suzma','olma',
#                'shaftoli','kefir','baton','shokolad']
# savat = []
# for k in range(5):
#     savat.append(input(f'Savatga {k+1}-mahsulotni qo\'shing: '))
# for mahsulot in savat:
#      if mahsulot in mahsulotlar:
#          print(f'Do\'konimizda {mahsulot}  bor')
#      else:
#          print(f"Do\'konimizda {mahsulot} yo'q")
       
         
       
# users = ['ali', 'vali', 'hasan', 'husan', 'olim']
# new_user = (input('Yangi login kiriting >>>')).lower()
# # new_user = new_user.lower()

# if new_user in users:
#     print("Login band, yangi login tanlang !")
# else:
#     print(f"Xush kelibsiz, {new_user.title()} !")







# son = int(input('Istalgan butun sonni kiritng:  '))

# for n in range(2,11):
#     if  (son % n == 0):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#     else:
#         print(f"{son} soni {n} qoldiqli bo'linadi")














