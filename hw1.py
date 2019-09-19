import sys
# import pandas as pd

allprices = {}
tks = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB']


def getDataIntoDict(file, dict):

    _data = open(file)
    data = []

    with _data as f:
        data = _data.readlines()

    for i in range(len(data)):
        data[i] = data[i].strip("\n")

    data.pop(0)
    data_array = []
    for i in range(len(data)):
        data_array.append(data[i].split(','))

    stock_price = []

    for i in range(len(data_array)):
        stock_price.append(data_array[i][5])

    allprices[file.split('.')[0]] = stock_price


def corellation(X, Y):
    mean_x = 0
    mean_y = 0

    for i in range(len(X)):
        mean_x = mean_x+float(X[i])
        mean_y = mean_y+float(Y[i])

    mean_x = (mean_x/len(X))
    mean_y = (mean_y/len(Y))
    # print("mean_x",mean_x)
    # print("mean_y",mean_y)
    sum_numer = 0
    s_x = 0
    s_y = 0

    for i in range(len(X)):
        sum_numer += ((float(X[i])-mean_x)*(float(Y[i])-mean_y))

    for i in range(len(X)):
        s_x += (float(X[i])-mean_x)**2
        s_y += (float(Y[i])-mean_y)**2

    return (sum_numer/(s_x*s_y)**0.5)


for i in range(len(tks)):
    getDataIntoDict(tks[i]+'.csv', allprices)


def returnCombs(item, list):
    for i in range(len(list)):
        if(item != list[i]):
            # print(item, ":" ,list[i])
            print(item+":"+list[i],corellation(allprices[item], allprices[list[i]]))
for i in range(len(tks)):
    returnCombs(tks[i], tks[i:])

