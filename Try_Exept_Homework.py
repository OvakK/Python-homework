####################################################
# XLSXWRITER TRY EXCEPT
####################################################
import argparse

try:
    import xlsxwriter
except ModuleNotFoundError:
    var = input('''XlsxWriter module not installed. Do you want to install now?
Only 'yes' will be accepted to approve. > ''')
    if var == 'yes':
        import os

        os.system("pip3 install XlsxWriter")
        import xlsxwriter
    else:
        exit()


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='File .txt')
    parser.add_argument('-x', '--xlsx', default="Tablica1", help='File .exel')
    args = parser.parse_args()
    return args.file, args.xlsx


def get_content(fname):
    try:
        fl = open(fname)
    except FileNotFoundError:
        print("No such file in directory")
        exit()
    b = []
    for y in fl:
        b.append(y.split())
    fl.close()
    c = sorted(b, reverse=True, key=lambda x: x[2])
    return c


def create_workbook(wbname):
    workbook = xlsxwriter.Workbook(wbname)
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 3, 10)
    format1 = workbook.add_format(({'bold': True, 'bg_color': '#FFFF00'}))

    worksheet.write('A1', 'Name', format1)
    worksheet.write('B1', 'Surname', format1)
    worksheet.write('C1', 'Age', format1)
    worksheet.write('D1', 'Proffession', format1)
    return workbook, worksheet


def fill_data(workbook, worksheet, cnt):
    for i, (name, surname, age, proffession) in enumerate(cnt, start=2):
        worksheet.write(f'A{i}', name)
        worksheet.write(f'B{i}', surname)
        worksheet.write(f'C{i}', age)
        worksheet.write(f'D{i}', proffession)
    workbook.close()


def main():
    filename, xlsxname = get_arguments()
    content = get_content(filename)
    wb, ws = create_workbook(xlsxname)
    fill_data(wb, ws, content)


main()

##############################################################
# KTO HOCHET STAT MILLIONEROM TRY EXCEPT
##############################################################

import random

try:
    f = open('khsm')
except FileNotFoundError:
    print("No such file in directory")
    exit()
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
    try:
        f = open('otv_list')
    except FileNotFoundError:
        print("No such file in directory")
        exit()
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
