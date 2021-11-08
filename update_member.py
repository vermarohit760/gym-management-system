from create_member import *
import re
def update_member():
    print('Enter the Member Mobile Number to update details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
    if mobile_number in super_user.member_dict.keys():
        print('Enter Membership duration to extend in months (1,3,6,12) , 0 to revoke membership :- ')
        while True:
            try:
                duration=int(input())
                duration_list=[0,1,3,6,12]
                if duration in duration_list:
                    break
            except:
                print('Please enter the correct Membership Duration :')
        super_user.member_dict[mobile_number]['Duration']=super_user.member_dict[mobile_number]['Duration']+duration
        while True:
            if duration==0:
                super_user.member_dict.pop(mobile_number)
                break
            else:
                print('Enter the name:- ')
                name=input()
                super_user.member_dict[mobile_number]['Name']=name
                print('Enter the Age:- ')
                while True:
                    try:
                        age=int(input())
                        break
                    except:
                        print('Please enter the correct age :')
                super_user.member_dict[mobile_number]['Age']=age
                print('Enter the Gender (M,F,T):- ')
                while True:
                    gender=input()
                    gender_list=['M','F','T']
                    if gender in gender_list:
                        break
                    else:
                        print('Please enter the correct Gender :')
                super_user.member_dict[mobile_number]['Gender']=gender
                print('Enter the email:- ')
                while True:
                    try:
                        email=input()
                        pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                        if(re.search(pattern, email)):
                            break
                        else:
                            raise error
                    except error:
                            print('Enter the Valid Email id ')
                super_user.member_dict[mobile_number]['Email']=email
                print('Enter the BMI 0 to ',max(workout_regimen.range_list),':-')
                while True:
                    try:
                        bmi=float(input())
                        assert bmi>0 and bmi<=max(workout_regimen.range_list)
                        break
                    except:
                        print('Please enter the correct Body Mass Index (BMI) :')
                super_user.member_dict[mobile_number]['BMI']=bmi
                print('Create password for the member:- ')
                password=input()
                super_user.member_dict[mobile_number]['Password']=password
                print('Member details updated successfully')
                break
    else:
        print('Entered Mobile Number Is not Registered')