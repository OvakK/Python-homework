# import random
# vop = ["Nazovite stolicy Armenii?Yerevan,Moscow,Paris,Riga",
#        "Samaya bolshaya strana v mire?Russia,USA,Canada,China",
#        "Samaya vysokaya gora na zemle?Everest,Elbrus,Ararat,Kazbek",
#        "Samyi bolshoi okean?Pacific,Atlantic,Indian,Arctic",
#        "Kakoe bylo imya y Ensteina?Albert,Robert,William,Vasiliy",
#        "Samoe bolshoe mlekopitaushee na zemle?Kit,Slon,Lev,Giraf",
#        "Kto avtor romana Voina i mir?L.N.Tolstoy,F.M.Dostoevskii,F.S.Fitzgerald,N.V.Gogol",
#        "Nazovite samoe vysokogornoe ozero v mire?Ohos-del-Saldo,Titicaca,Baykal,Sevan",
#        "Kakaya po schety planeta ot solntsa zemlya?Tretyaya,Pervaya,Shestaya,Vosmaya",
#        "Skolko spytnikov y Zemli?Odin,Vosem,Tri,Desyat",
#        "Kakova himicheskaya formyla vody?H2O,CO2,C2H5OH,O2",
#        "Kto avtor romana MOBY-DICK?G.Melvil,E.Poe,G.Marquez,Eminem",
#        "Kto pervyi v istorii vnedril konveernyu sborky?G.Ford,S.Jobs,Nikolay2,A.Lincoln",
#        "Nazovite samoe bystroe syhopytnoe givotnoe?Gepard,Tiger,Chelovek,Nosorog",
#        "Kto avtor romana Otvergennye?V.Gugo,W.Shekspir,M.Sholokhov,F.Kavka"]
# a = []
# for x in vop:
#        a.append(x.split("?"))
#
# b = []
# for x in a:
#        y = [x[0], x[1].split(',')]
#        b.append(y)
#
# c = random.sample(b, 10)
# prav = 0
# neprav = 0
# print("Start game!!!")
# for x in c:
#        y = list(x[1])
#        random.shuffle(y)
#        print(f"{x[0]}? \nVarianty otveta:\n{y}")
#        answ = input("Vash otvet > ")
#        if answ == x[1][0]:
#               print("Verno!")
#               prav += 1
#        else:
#               print(f"Neverno\nVernyi otvet {x[1][0]}")
#               neprav += 1
# print(f"{prav} pravilnyh otvetov\n{neprav} nepravilnyh otvetov")

###########################################################################################

# import random
# questions = []
# while len(questions) < 5:
#     ques = random.choice(vop)
#     if ques not in questions:
#         questions.append(ques)
#
# md = {}
# for el in questions:
#     q, a = el.split("?")
#     md[q] = a.split(",")
#
# for q, a in md.items():
#     print(q)
#     ca= a[0]
#     random.shuffle(a)
#     cnt = 1
#     for el in a:
#         print(cnt, el)
#         cnt += 1
#     answer = input("input your answer: ")
#     if answer== ca:
#         print("Correct")
#         xp +=1
#     else:
#         print("Incorrect. Correct answer was ", ca )
# print("You got %d/%d" %(xp, len(md)))
