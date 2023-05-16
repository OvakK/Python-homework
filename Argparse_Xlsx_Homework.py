import argparse
import xlsxwriter


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='File .txt')
    parser.add_argument('-x', '--xlsx', default="Tablica1", help='File .exel')
    args = parser.parse_args()
    return args.file, args.xlsx


def get_content(data_file):
    with open(data_file) as f:
        lst = []
        for el in f:
            lst.append(el.split())
        sorted_list = sorted(lst, reverse=True, key=lambda x: x[2])
        for x in sorted_list:
            x[2] = int(x[2])
        return sorted_list


def create_workbook(wbname):
    workbook = xlsxwriter.Workbook(wbname)
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 3, 10)
    format1 = workbook.add_format(({'bold': True, 'bg_color': '#FFFF00'}))

    worksheet.write('A1', 'Name', format1)
    worksheet.write('B1', 'Surname', format1)
    worksheet.write('C1', 'Age', format1)
    worksheet.write('D1', 'Profession', format1)
    return workbook, worksheet


def fill_data(workbook, worksheet, cont):
    format2 = workbook.add_format(({'bold': False, 'bg_color': '#008000'}))
    for i, (name, surname, age, profession) in enumerate(cont, start=2):
        worksheet.conditional_format(f'C{i}', {'type': 'cell', 'criteria': '<', 'value': 25, 'format': format2})
        worksheet.write(f'A{i}', name)
        worksheet.write(f'B{i}', surname)
        worksheet.write(f'C{i}', age, )
        worksheet.write(f'D{i}', profession)
    workbook.close()


def main():
    filename, xlsxname = get_arguments()
    mylst = get_content(filename)
    work_b, work_sh = create_workbook(xlsxname)
    fill_data(work_b, work_sh, mylst)


main()
