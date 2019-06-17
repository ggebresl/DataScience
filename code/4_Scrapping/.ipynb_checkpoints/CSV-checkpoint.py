import csv

with open('iris.csv') as csvfile:
    readcsv = csv.reader(csvfile,delimiter=',')

    Sepal_l = []
    Sepal_w = []
    Petal_l = []
    Petal_w = []
    Species = []

    for row in readcsv:
        Sepal_l.append(row[0])
        Sepal_w.append(row[1])

    print(Sepal_l)
    print(Sepal_w)
