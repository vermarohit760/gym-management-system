from create_member import *
def create_regimen():
    print('Enter the lower limit of BMI range:-')
    while True:
        try:
            bmi_lower=int(input())
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) lower limit :') 
    print('Enter the upper limit of BMI range:-')
    while True:
        try:
            bmi_upper=int(input())
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) upper limit :')
    if bmi_lower>35:
        print('Enter workout for monday :')
        mon=input()
        print('Enter workout for tuesday :')
        tue=input()
        print('Enter workout for wednesday :')
        wed=input()
        print('Enter workout for thursday :')
        thur=input()
        print('Enter workout for friday :')
        fri=input()
        print('Enter workout for saturday :')
        sat=input()
        print('Enter workout for sunday :')
        sun=input()
        workout=workout_regimen(bmi_lower,bmi_upper,mon,tue,wed,thur,fri,sat,sun)
        print('Workout Regimen created successfully')
    else:
        print('The work regimen is already created')