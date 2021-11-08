from create_member import *
def delete_regimen():
    print('Choose workout regimen to be deleted',list(workout_regimen.regimen.keys()))
    print('Lower limit of range :')
    while True:
        try:
            lower=float(input())
            break
        except:
            print('Enter input in numbers')
    print('Upper limit of range :')
    while True:
        try:
            upper=float(input())
            break
        except:
            print('Enter input in numbers')
    if lower in workout_regimen.range_list and upper in workout_regimen.range_list:
        for i in list(workout_regimen.regimen.keys()):
            if lower==i[0] and upper==i[1]:
                workout_regimen.regimen.pop(i)
                workout_regimen.range_list.remove(lower)
                workout_regimen.range_list.remove(upper)
                print('Workout Regimen deleted successfully')
    else:
        print('This Range is NOT DEFINED for this work regimen')