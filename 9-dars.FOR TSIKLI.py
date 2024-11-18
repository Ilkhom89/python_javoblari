# -*- coding: utf-8 -*-
"""
Created on Fri May 21 23:33:27 2021

@author: ADMIN
"""

# mehmonlar = ['Behruz','Shahruz','Parviz','Mubina','Muhammadbobur']
# for mehmon in mehmonlar:
#     print('Salom', mehmon)     # tsiklning badani
#     print("Hayr", mehmon)
    
# mehmonlar = ['Behruz','Shahruz','Parviz','Mubina','Muhammadbobur']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} , sizni 22 = may kuni nahorgi oshga taklif etamiz")
#     print("Hurmat bilan, Umurzoqovlar oilasi\n")
   
# sonlar = list(range(1,11)) # 1 dan 10 gacha sonlar ro'yxati
# for son in sonlar:
#     print(f"{son}ning kvadrati {son**2}ga teng\n")

# sonlar = list(range(11))        # 0 ddan 10 gacha sonlar ro'yxati 
# sonlar_kvadrati = []            # bo'sh ro'yxat yaratamiz
# for son in sonlar :
#     sonlar_kvadrati.append(son**2)    
# print(sonlar)
# print(sonlar_kvadrati)    
  
# dostlar = []                        # bo'sh ro'yxat
# print('5 ta eng yaqin do\'stingiz kim ?')
# for n in range(5):                  # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting: "))
# print(dostlar)
 

############   AMALIYOT   ##############

# ismlar = ['Ikrom', 'Otajon','Muhammad','Suxrob', "To'lqin",'Shohrux']
# for ism in ismlar:
#     print(f"""Hurmatli {ism}, Sizni 22-aprel kuni Muhammadboburning 
# sunnat to\'yi munosabati bilan nahorgi oshga taklif etamiz! \n""")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# toq_sonlar = list(range(11,100,2))
# print(toq_sonlar)
# for son in toq_sonlar:
#     print(son**3)

# kinolar = []
# print('5 ta eng sevimli kinongizni nomini ayting: ')
# for n in range(1,6):
#     kinolar.append(input(f"{n}- sevimli kinongizni nomini kiriting: " ))
# print(kinolar)



n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
































