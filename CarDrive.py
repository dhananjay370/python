age = int(input("Enter Your Ege : "))
if (age >= 18):
    license = input("Do you have driving license? : ")
    if (license == "yes" or license == "Yes" or license == "Y" or license == "y" or license == 1 or license == "Ye" or license == "ye"):
        print("You can drive safely...")
    else:
        print("You cannot drive a car becouse you don't have driving license!")
else:
    print("Sorry you cannot drive a car!!!")