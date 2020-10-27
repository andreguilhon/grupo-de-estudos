from xlrd import open_workbook
from os import path, mkdir
from datetime import datetime
from glob import glob
from decimal import Decimal
from csv import writer, reader as csv_reader
from xlsxwriter.workbook import Workbook


class InfoSummarizer:
    
    
    def sum_values(self, planilha):
        name = path.basename(planilha).split('_')
        cnpj = name[1]
        periodo_mes = name[2]
        periodo_ano = name[3].replace('.xlsx', '')
        
        wb = open_workbook(planilha)
        sheet = wb.sheet_by_index(0)
        total = 0
        for line in range(10, sheet.nrows - 1):
            try:
                total += Decimal(str(sheet.cell_value(line, 29)))
            except Exception as e:
                pass
                # print(planilha, cnpj, periodo_mes, periodo_ano, total, i, e)
                # print('ERRO -----> ', cnpj, periodo_mes, periodo_ano, sheet.cell_value(line, 29))
                # raise
        return [str(cnpj), periodo_mes.zfill(2), periodo_ano, total]


    def get_files(self):
        all_files = sorted(glob("./**/FICHA3*.xlsx", recursive=True))
        return all_files

    def __init__(self):
        self.__files = self.get_files()
        with open('result.csv', 'w', newline='') as stream:
            csv_file = writer(stream)
            for _file in self.__files:
                csv_file.writerow(self.sum_values(_file))
        with open('result.csv', 'r', newline='') as stream:
            workbook = Workbook('result.xlsx')
            worksheet = workbook.add_worksheet()
            reader = csv_reader(stream)
            for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()



if __name__ == '__main__':
    InfoSummarizer()
