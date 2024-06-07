def calculate_bmi(height, weight): 
    print("height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height*height)
    print("BMI IS" ,BMI)
    if (BMI<18.5):
        print("you are underweight")
        return -1
    elif (BMI>=18.5 and BMI<=25.0):
        print("you are normal weight")
        return 0

    else:
        print("you are overwight")
        return 1

def main(): 
    calculate_bmi(weight = 57, height=1.73)

if __name__ == "__main__":    
    main() 
 


