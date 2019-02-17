import csv
import math



def return_average():
    with open('MERGED2016_17_PP.csv', errors = 'replace') as csvfile:
        reader = csv.reader(csvfile, dialect = 'excel')
        all_prices = []
        reader = list(reader)
        for row in reader[1:]:
            if row[0] != '':
                all_prices.append(int(row[0]))

        return (sum(all_prices)/len(all_prices))
