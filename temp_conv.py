# temp_Val = "Celsius"
  
# getting drop down value 
# def store_temp(set_temp): 
#     global temp_Val 
#     temp_Val = set_temp 
  
# Conversion of  temperature 



def call_convert(from_unit, to_unit, temp):
        if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    f = float((float(temp) * 9 / 5) + 32)         
                    # print(f)
                    f=round(f,3)
                    return f
                elif to_unit == "Kelvin":
                    k = temp + 273.15
                    k = round(k,3)
                    return k


        elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    c = float((float(temp) - 32) * 5 / 9)         
                    # print(f)
                    c = round(f,3)
                    return c
                elif to_unit == "Kelvin":
                    c = float((float(temp) - 32) * 5 / 9)
                    k = c + 273.15
                    k = round(f,3)
                    return k

        elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    k = temp - 273.15
                    k = round(k,3)
                    return k
                elif to_unit == "Fahrenheit":
                    c = float((float(temp) - 32) * 5 / 9) 
                    k = c - 273.15
                    k = round(k,3)
                    return k


#test run
# print(call_convert("Fahrenheit",95))