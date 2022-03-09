def my_func(x1, x2, x3):
    try:
        if (type(x1) == float and type(x2) == float and type(x3) == float):
            counter = (x1 + x2 + x3) * (x2 + x3) * x3
            denominator = x1 + x2 + x3
            if (denominator == 0):
                print("Not a number – denominator equals zero")
            else:
                return (counter / denominator)
        else:
            print("Error: parameters should be float")

    except:
        return "None"

#my_func(1.0,2.0,1.2)



def convert(hours, minutes):
    if hours>0 and minutes>0:
        seconds = (hours)*3600 + (minutes)*60
        return seconds
    else:
        print("Input error!")

#print(convert(1.75,-3))

