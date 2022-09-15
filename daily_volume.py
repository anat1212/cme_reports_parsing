import json
import glob
import re
import camelot
from camelot import read_pdf
import pandas as pd

# choose directory on your PC and put 'DailyBulletin_20220914177' file there.
# Put the address of the directory in the line below and wait until 'INST.xlsx' will appear in the same folder.

wait and untill document will be processed and 
files = glob.glob("C:/Users/Anatoliy/PycharmProjects/pythonProject/cme/*.pdf")
for file in files:
    tables = camelot.read_pdf(file, flavor='stream', pages='1-20')
    tables.export('memo.json', f='json', compress=False)
    final_list90 = []
    final_list88 = []
    final_list89 = []

    def scrap(i):
        q222 = []
        for key, value in i.items():
            b222 = re.findall(r'\w+', value)
            for t in b222:
                q222.append(t)
        # print(q222[-5:-3])
        a999 = (q222[-5:-3])
        if int(a999[1]) < 9000:
            final_list88.append(q222[-3:-2][0])
            final_list89.append(row)
        else:
            final_list88.append(q222[-5:-4][0])
            final_list89.append(row)


    final_list = []
    names = glob.glob("*.json")
    for name in names:
        with open(name) as json_file:
            data = json.load(json_file)
            for i in data:
                for n in (i.values()):
                    b111 = re.findall(r'\w+', str(n))

                    if 'NYMEX' in b111:
                        if 'CRUDE' in b111:
                            if 'OIL' in b111:
                                row = '19_CL'
                                scrap(i)


                    if 'NYMEX' in b111:
                        if 'HEATING' in b111:
                            if 'OIL' in b111:
                                if 'FUTURES' not in b111:
                                    row = '20_HEATOIL'
                                    scrap(i)

                    if 'NATURAL' in b111:
                        if 'GAS' in b111:
                            if 'HENRY' in b111:
                                if 'HUB' in b111:
                                    row = '21_GAS'
                                    scrap(i)

                    if 'MINI' in b111:
                        if 'FUTURES' in b111:
                            if '500' in b111:
                                if 'MICRO' not in b111:
                                    if 'ESG' not in b111:
                                        row = '22_SP'
                                        scrap(i)

                    if 'MINI' in b111:
                        if 'FUTURES' in b111:
                            if '100' in b111:
                                if 'MICRO' not in b111:
                                    if 'NASDAQ' in b111:
                                        row = '23_NQ'
                                        scrap(i)

                    if 'CORN' in b111:
                        if 'FUTURES' in b111:
                            if 'MINI' not in b111:
                                row = '27_CORN'
                                scrap(i)

                    if 'SOYBEAN' in b111:
                        if 'FUTURES' in b111:
                            if 'MINI' not in b111:
                                if 'MEAL' not in b111:
                                    if 'OIL' not in b111:
                                        row = '28_SOYBEAN'
                                        scrap(i)

                    if 'WHEAT' in b111:
                        if 'FUTURES' in b111:
                            if 'MINI' not in b111:
                                if 'AUSTRALIAN' not in b111:
                                    if 'KC' not in b111:
                                        row = '29_WHEAT'
                                        scrap(i)

                    if 'COMEX' in b111:
                        if 'FUTURES' in b111:
                            if 'GOLD' in b111:
                                if 'MICRO' not in b111:
                                    row = '24_GOLD'
                                    scrap(i)

                    if 'COMEX' in b111:
                        if 'FUTURES' in b111:
                            if 'SILVER' in b111:
                                if 'MICRO' not in b111:
                                    row = '25_SILVER'
                                    scrap(i)

                    if 'COMEX' in b111:
                        if 'FUTURES' in b111:
                            if 'COPPER' in b111:
                                if 'MINI' not in b111:
                                    if 'SWAP' not in b111:
                                        row = '26_COPPER'
                                        scrap(i)


                    if 'EURODOLLAR' in b111:
                        if 'FUTURES' in b111:
                                if 'MONTH' not in b111:
                                    row = '30_ERDOLL'
                                    scrap(i)

                    if '10' in b111:
                        if 'NOTE' in b111:
                            if 'YR' in b111:
                                if 'FUTURES' in b111:
                                    row = '31_10_YEAR'
                                    scrap(i)

                    if '5' in b111:
                        if 'NOTE' in b111:
                            if 'YR' in b111:
                                if 'FUTURES' in b111:
                                    row = '32_5_YEAR'
                                    scrap(i)

                    if '2' in b111:
                        if 'NOTE' in b111:
                            if 'YR' in b111:
                                if 'FUTURES' in b111:
                                    row = '33_2_YEAR'
                                    scrap(i)



    df = pd.DataFrame({'name': final_list89})
    df['volume'] = final_list88
    df = df.sort_values(by='name')
    print(df)
    df = df.drop_duplicates()
    df.to_excel('INST.xlsx', index=False)
