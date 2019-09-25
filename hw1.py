allprices = {}
tks = ['IBM', 'MSFT', 'GOOG', 'AAPL', 'AMZN', 'FB']
results = {}

def getDataIntoDict(file, dict):

    _data = open(file)
    data = data_array = stock_price = []
    with _data as f:
        data = _data.readlines()

    data = [data[i].strip("\n") for i in range(len(data))]
    data.pop(0)
    data_array = [data[i].split(',') for i in range(len(data))]
    stock_price = [float(data_array[i][5]) for i in range(len(data_array))]
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

[getDataIntoDict(tks[i]+'.csv', allprices) for i in range(len(tks))]

def returnCombs(item, list, results):
    
    for i in range(len(list)):
        if(item != list[i]):
            results.update({item+":"+list[i] : corellation(allprices[item], allprices[list[i]])})
    
for i in range(len(tks)):
    returnCombs(tks[i], tks[i:], results)

final_result = sorted(results.items(), key=lambda x: x[1], reverse=True)
for key, value in final_result:
    print(key, value)