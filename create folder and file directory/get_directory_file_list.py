import xlsxwriter,os

output = []

root_Path = r'D:\BIM Addin\Dynamo'

for root, dirs, files in os.walk(root_Path):
    for file in files:
        if '.dyn' in file.split('//')[-1] and '.backup' not in file.split('//')[-1] and 'Package' not in root and 'EMSD' not in root and 'Aussie BIM Guru' not in root:
            output.append(root)

content = list(set(output))

workbook = xlsxwriter.Workbook(root_Path + os.sep + 'Dynamo List.xlsx')
worksheet = workbook.add_worksheet()

col = 0
row = 0
for data in content:
    worksheet.write(row, col, data)
    row = row + 1

workbook.close()