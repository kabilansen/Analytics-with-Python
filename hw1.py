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


print("IBM:MSFT = ",corellation(allprices['IBM'], allprices['MSFT']))
print("IBM:GOOG = ",corellation(allprices['IBM'], allprices['GOOG']))
print("IBM:AAPL = ",corellation(allprices['IBM'], allprices['AAPL']))
print("IBM:AAPL = ",corellation(allprices['IBM'], allprices['AAPL']))
print("IBM:AMZN = ",corellation(allprices['IBM'], allprices['AMZN']))
print("IBM:FB = ",corellation(allprices['IBM'], allprices['FB']))
print("MSFT:GOOG = ",corellation(allprices['MSFT'], allprices['GOOG']))
print("MSFT:AAPL = ",corellation(allprices['MSFT'], allprices['AAPL']))
print("MSFT:AMZN = ",corellation(allprices['MSFT'], allprices['AMZN']))
print("MSFT:FB = ",corellation(allprices['MSFT'], allprices['FB']))
print("GOOG:AAPL = ",corellation(allprices['GOOG'], allprices['AAPL']))
print("GOOG:AMZN = ",corellation(allprices['GOOG'], allprices['AMZN']))
print("GOOG:FB = ",corellation(allprices['GOOG'], allprices['FB']))
print("AAPL:AMZN = ",corellation(allprices['AAPL'], allprices['AMZN']))
print("AAPL:AMZN = ",corellation(allprices['AAPL'], allprices['FB']))
print("AMZN:FB = ",corellation(allprices['AMZN'], allprices['FB']))
