import statistics

def calc_average(values_list): 
    print("calc_average")
    average = sum(values_list)/len(values_list)
    print(average)
    return average

def get_user_input():
    print("get user input")
    values = input("Enter values")
    splitText = values.split(",")
    values_list = []
    for x in splitText:
        values_list.append(float(x))
    print(values_list)
    return values_list

def find_min_max(values_list):
    print("find min and max")
    max_value = max (values_list)
    min_value  = min (values_list)
    print("minimum is " ,max_value)
    print("maximum is ",min_value)
    return max_value, min_value
    
    
def sort_temperature(values_list): 
    print("sort temperature")
    value_sorted = sorted(values_list)
    print(value_sorted)
    return value_sorted



def calc_median_temperature(value_sorted):
    print("calculate median temp")
    median_value = statistics.median(value_sorted)
    print(median_value)
    return median_value



def main():
    y=get_user_input() 
    find_min_max(y)
    calc_average(y)
    s=sort_temperature(y)
    calc_median_temperature(s)

 


if __name__ == "__main__":
    main()