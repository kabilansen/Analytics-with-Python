allprices = {}
tks = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB']

def getDataIntoDict(file, dict):

    _data = open(file)
    data = data_array = []

    with _data as f:
        data = _data.readlines()

    for i in range(len(data)):
        data[i] = data[i].strip("\n")

    data.pop(0)
    
    for i in range(len(data)):
        data_array.append(data[i].split(','))

    stock_price = []

    for i in range(len(data_array)):
        stock_price.append(float(data_array[i][5]))

    allprices[file.split('.')[0]] = stock_price


def corellation(X, Y):
    mean_x = mean_y = sum_numer = s_x = s_y = 0

    mean_x = sum(X,0)/len(X)
    mean_y = sum(Y,0)/len(Y)

    for i in range(len(X)):
        sum_numer += ((X[i])-mean_x)*((Y[i])-mean_y)
        s_x += ((X[i])-mean_x)**2
        s_y += ((Y[i])-mean_y)**2
        
    return round((sum_numer/(s_x*s_y)**0.5),2)

for i in range(len(tks)):
    getDataIntoDict(tks[i]+'.csv', allprices)

def returnCombs(item, list):
    for i in range(len(list)):
        if(item != list[i]):
            print(item+":"+list[i]+" = ",corellation(allprices[item], allprices[list[i]]))
for i in range(len(tks)):
    returnCombs(tks[i], tks[i:])