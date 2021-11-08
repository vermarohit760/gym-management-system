from create_member import *
from MEMBER import * 
def view_my_regimen(mobile_number):
    Bm_index=super_user.member_dict[mobile_number]['BMI']
    for k in workout_regimen.regimen.keys():
        if Bm_index>k[0] and Bm_index<=k[1]:
            print('Monday    : ',workout_regimen.regimen[k]['monday'])
            print('Tuesday   : ',workout_regimen.regimen[k]['tuesday'])
            print('Wednesday : ',workout_regimen.regimen[k]['wednesday'])
            print('Thursday  : ',workout_regimen.regimen[k]['thursday'])
            print('Friday    : ',workout_regimen.regimen[k]['friday'])
            print('Saturday  : ',workout_regimen.regimen[k]['saturday'])
            print('Sunday    : ',workout_regimen.regimen[k]['sunday'])