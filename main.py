import os

from config import INPUT_DIR, OUTPUT_DIR
from my_excel import read_excel_file, read_xls, save_excel_file
from parser import parsing

if __name__ == '__main__':
    data_sheets = []
    for f in os.listdir(INPUT_DIR):
        f = os.path.join(INPUT_DIR, f)
        if f.endswith('xls'):
            data_sheets.append(read_xls(f))
        if f.endswith('xlsx'):
            data_sheets.append(read_excel_file(f))

    data_list_export = []
    for i, d in enumerate(data_sheets):
        if i == 0:
            data_list_export.extend(parsing(d['TDSheet'],header=True))
        else:
            data_list_export.extend(parsing(d['TDSheet']))
    print(data_list_export)

    save_excel_file(os.path.join(OUTPUT_DIR, 'out.xlsx'), data_list_export)
