import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"  # 160 currencies
# url='https://api.exchangeratesapi.io/latest?base=USD' #33 currencies
data = requests.get(url).json()
# print(s)

rates = data["rates"]
currency = rates
# print(rates)

# i=0
# for key in rates.items():
#     i+=1
# print(i)


def send():
    return list(currency.keys())


def conv_curr(fr, t, fv):
    val = 0
    tempfr = 0
    if fr == 'USD':
        for key, value in currency.items():
            if key == t:
                val = fv*value
                val = round(val, 3)
                # print("Converted value: ",val, t)
                return val
    else:
        for key, value in currency.items():
            if key == fr:
                tempfr = fv/value
        for key, value in currency.items():
            if key == t:
                val = tempfr*value
                val = round(val, 3)
                # print("Converted value: ",val,t)
                return val


# test run
# c=conv_curr('USD','INR',1)
# print(send())
# print(c)
