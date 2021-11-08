from create_member import *
def view_regimen():
    print('Enter the Body Mass Index (BMI): ')
    while True:
          try:
              Bmi=float(input())
              break
          except:
              print('Please Enter correct BMI')
    if Bmi<=max(workout_regimen.range_list) and Bmi>=min(workout_regimen.range_list):
        for k in workout_regimen.regimen.keys():
              if Bmi>k[0] and Bmi<=k[1]:
                  print('Monday    : ',workout_regimen.regimen[k]['monday'])
                  print('Tuesday   : ',workout_regimen.regimen[k]['tuesday'])
                  print('Wednesday : ',workout_regimen.regimen[k]['wednesday'])
                  print('Thursday  : ',workout_regimen.regimen[k]['thursday'])
                  print('Friday    : ',workout_regimen.regimen[k]['friday'])
                  print('Saturday  : ',workout_regimen.regimen[k]['saturday'])
                  print('Sunday    : ',workout_regimen.regimen[k]['sunday'])