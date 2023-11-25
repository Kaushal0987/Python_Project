def bmi_calc(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ", bmi)
    if bmi > 25:
        print(name, "is overweight")
    else:
        print(name, "is not overweight")


nm = input("Enter the name of the user: ")
ht = float(input("Enter the height of the user in meter : "))
wt = float(input("Enter the weight of the user in kilogram: "))
bmi_calc(nm, ht, wt)
