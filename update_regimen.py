from create_member import *
def update_regimen():
    print('Choose workout regimen to be updated',list(workout_regimen.regimen.keys()))
    print('Lower limit of range :')
    while True:
        try:
            lower=float(input())
            break
        except:
            print('Enter input in numbers')
    print('Upper limit of range')
    while True:
        try:
            upper=float(input())
            break
        except:
            print('Enter input in numbers')
    if lower in workout_regimen.range_list and upper in workout_regimen.range_list:
        print('Enter workout for monday :')
        mon=input()
        workout_regimen.regimen[(lower,upper)]['monday']=mon
        print('Enter workout for tuesday :')
        tue=input()
        workout_regimen.regimen[(lower,upper)]['tuesday']=tue
        print('Enter workout for wednesday :')
        wed=input()
        workout_regimen.regimen[(lower,upper)]['wednesday']=wed
        print('Enter workout for thursday :')
        thur=input()
        workout_regimen.regimen[(lower,upper)]['thursday']=thur
        print('Enter workout for friday :')
        fri=input()
        workout_regimen.regimen[(lower,upper)]['friday']=fri
        print('Enter workout for saturday :')
        sat=input()
        workout_regimen.regimen[(lower,upper)]['saturday']=sat
        print('Enter workout for sunday :')
        sun=input()
        workout_regimen.regimen[(lower,upper)]['sunday']=sun
          
        workout=workout_regimen(lower,upper,mon,tue,wed,thur,fri,sat,sun)
        print('workout regimen updated successfully')
    
    else:
        print('This Range is NOT DEFINED for this workout regimen')