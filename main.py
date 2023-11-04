

import read_csv


import days


import charts

def run():
    data=read_csv.read_csv('./road.csv')
    labels, values = days.days(data)
    charts.generate_bar_char(labels, values)

if __name__ == '__main__' :
    run()




