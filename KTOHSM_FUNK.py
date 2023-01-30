import random
vop = ["Nazovite stolicy Armenii?Yerevan,Moscow,Paris,Riga",
       "Samaya bolshaya strana v mire?Russia,USA,Canada,China",
       "Samaya vysokaya gora na zemle?Everest,Elbrus,Ararat,Kazbek",
       "Samyi bolshoi okean?Pacific,Atlantic,Indian,Arctic",
       "Kakoe bylo imya y Ensteina?Albert,Robert,William,Vasiliy",
       "Samoe bolshoe mlekopitaushee na zemle?Kit,Slon,Lev,Giraf",
       "Kto avtor romana Voina i mir?L.N.Tolstoy,F.M.Dostoevskii,F.S.Fitzgerald,N.V.Gogol",
       "Nazovite samoe vysokogornoe ozero v mire?Ohos-del-Saldo,Titicaca,Baykal,Sevan",
       "Kakaya po schety planeta ot solntsa zemlya?Tretyaya,Pervaya,Shestaya,Vosmaya",
       "Skolko spytnikov y Zemli?Odin,Vosem,Tri,Desyat",
       "Kakova himicheskaya formyla vody?H2O,CO2,C2H5OH,O2",
       "Kto avtor romana MOBY-DICK?G.Melvil,E.Poe,G.Marquez,Eminem",
       "Kto pervyi v istorii vnedril konveernyu sborky?G.Ford,S.Jobs,Nikolay2,A.Lincoln",
       "Nazovite samoe bystroe syhopytnoe givotnoe?Gepard,Tiger,Chelovek,Nosorog",
       "Kto avtor romana Otvergennye?V.Gugo,W.Shekspir,M.Sholokhov,F.Kavka"]

def quest_list(x):
    questions = []
    while len(questions) < 10:
        ques = random.choice(x)
        if ques not in questions:
            questions.append(ques)
    return questions

def quest_dict(x):
    md = {}
    for el in x:
        q, a = el.split("?")
        md[q] = a.split(",")
    return md

def game(x):
    xp = 0
    for q, a in x.items():
        print(q)
        ca = a[0]
        random.shuffle(a)
        cnt = 1
        for el in a:
            print(cnt, el)
            cnt += 1
        answer = input("input your answer: ")
        if answer == ca:
            print("Correct")
            xp += 1
        else:
            print("Incorrect. Correct answer was ", ca )
    return "You got %d/%d" %(xp, len(x))



def main():
    q_list = quest_list(vop)
    q_dict = quest_dict(q_list)
    print(game(q_dict))

main()
