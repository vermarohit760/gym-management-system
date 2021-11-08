from create_member import *
from view_my_regimen import *
from view_my_profile import *
def MEMBER():
    print('Please enter LOGIN credential')
    print('Enter your mobile number')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Enter correct mobile number')
    if mobile_number in super_user.member_dict.keys():
        print('Enter your Password:')
        user_password=input()
        if super_user.member_dict[mobile_number]['Password']==user_password:
            print('HELLOOOOOO Member.... Please select one option from given list:---')
            while True:
                try:
                    print('1. View My Regimen')
                    print('2. View My Profile')
                    print('3. Update Profile')
                    print('4. Logout')
                    m=int(input())
                    if m==1:
                        view_my_regimen(mobile_number)
                    elif m==2:
                        view_my_profile(mobile_number)
                    elif m==3:
                        update_profile(mobile_number)
                    elif m==4:
                        print('Logging OUT')
                        break
                    assert m>=1 and m<=4
                except:
                    print('Something went wrong, please select correct option')
                    
        else:     
            print('Login Credential did not match')
    else:
        print('This mobile number is not registered')