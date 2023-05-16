import random

f = open('khsm')
ls = f.read().split('\n')
vop = ls[:-1]
res = ''


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
    name = input("Input your name >")
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
            print("Incorrect. Correct answer was ", ca)
    res = f'{name} - ' + str(xp) + ' pravilnyh otvetov'
    print(res)
    return res


def get_content(game_results):
    f = open('otv_list')
    b = []
    for x in f:
        b.append(x.split())
    f.close()
    b.append(game_results.split())
    r_list = sorted(b, reverse=True, key=lambda x: x[2])
    return r_list


def fill_data(sorted_results):
    p = []
    for x in sorted_results:
        y = ' '.join(x)
        p.append(y)

    w = open('otv_list', 'w')
    for x in p:
        w.write(x + '\n')
    w.close()


def main():
    q_list = quest_list(vop)
    q_dict = quest_dict(q_list)
    score = game(q_dict)
    result_list = get_content(score)
    fill_data(result_list)


main()
