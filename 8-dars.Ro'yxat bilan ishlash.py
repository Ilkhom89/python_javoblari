# -*- coding: utf-8 -*-
"""
Created on Sun May 16 05:30:43 2021

@author: ADMIN
"""

# cars =['bmw','mersedes benz','volvo','general motors','tesla','audi']
# print(cars)
# cars.sort()               # Ro'yxatni tartiblash
# print(cars)
# cars.sort(reverse=True)   # Ro'yxatni teskari tartiblash
# print(cars)
# print(sorted(cars))       #asl ro'yxatga tegmagan holda tartiblash
# print(sorted(cars, reverse = True)) # Asl ro'yxatni o'zgartirmasdan teskari
                                      # tartiblash
# cars.reverse()            # ro'yxatni ortidan boshlab chiqarish
# print(cars)
# print(len(cars))            #ro'yxat uzunligini chiqaradi

############  RANGE funksiyasi ################

# print(list(range(0,10))) # shu oraliqdagi sonlarni list ko'rinishda
                         # konsolga chiqaradi
# sonlar2 = list(range(21,31))
# print(sonlar2)     
# toq_sonlar = list(range(1,16,2))    # qadamni ham berish mumkin
# print(toq_sonlar)           
# juft_sonlar = list(range(2,21,2))
# print(juft_sonlar)         

# print(max(toq_sonlar))     # Maxsimal son
# print(min(juft_sonlar))    # Minimal son
# print(sum(toq_sonlar))     # listdagi barcha sonlar yig'indisi
  
# narxlar = [4500,10000,7900,4600,1200,8700]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print('Eng arzon narx', arzon, '. Eng qimmat narx', qimmat, '. Jami', jami )

#########  RO'YXATNI 2 YOKI UNDAN ORTIQ ELEMENTINI KESISH ###########

# cars =['bmw','mersedes benz','volvo','general motors','tesla','audi']

# print(cars[4])
# print(cars[0:3])  # 3-element chiqmaydi
# print(cars[:4])   # 0 dan 4 gacha
# print(cars[2:])   # 2 dan oxirigacha
 
#######    RO'YXATDAN NUSXA OLISH  #########

# cars =['bmw','mersedes benz','volvo','general motors','tesla','audi']
# my_cars = cars[:]

# my_cars.remove('tesla')
# my_cars.append('gentra')
# my_cars[2] = 'trecker'
# print(my_cars)
# print(cars)
 
#######  TUPLE -- o'zgarmas ro'yxat  ######
# fanlar = ('ona tili', 'matematika','rus tili', 'algebra','geometriya')
# print(fanlar[0])
# print(fanlar[1:4])
# print(fanlar[-1])
        #   agar o'zgartirishga majbur bo'lsak
# fanlar = list(fanlar)
# fanlar.insert(2,'kimyo')
# print(fanlar)
# print(type(fanlar))
# fanlar = tuple(fanlar)
# print(type(fanlar))



###########    AMALIYOT    ######## 
# davlatlar =['Fransiya', 'Germaniya', 'Amerika', 'Braziliya','Ispaniya']
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar,reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# juft_sonlar = list(range(120,1200,2))
# print(sum(juft_sonlar))
# print(max(juft_sonlar) - min(juft_sonlar))
# print(len(juft_sonlar))
# print(juft_sonlar[:20])
# print(juft_sonlar[260:280])
# print(juft_sonlar[521:])

# taomlar = ['somsa', 'manti','palov','shashlik', 'dimlama']
# nonushta = taomlar[:]
# nonushta.remove('manti')
# nonushta.remove('shashlik')
# nonushta.append('tuxum')
# nonushta.append('grill')
# print(taomlar )
# print(nonushta)
# nonushta[0] = 'non va qaymoq' 
# print(type(nonushta))
# nonushta = tuple(nonushta) 
# print(type(nonushta))
# print(nonushta)
# print(taomlar)



















