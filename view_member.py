from create_member import *
def view_member():
    print('Enter the Member Mobile Number to view details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
    if mobile_number in super_user.member_dict.keys():
        print('Name                           : ',super_user.member_dict[mobile_number]['Name'])
        print('Age                            : ',super_user.member_dict[mobile_number]['Age'])
        print('Gender                         : ',super_user.member_dict[mobile_number]['Gender'])
        print('Mobile Number                  : ',super_user.member_dict[mobile_number]['Mobile number'])
        print('Email                          : ',super_user.member_dict[mobile_number]['Email'])
        print('Body Mass Index(BMI)           : ',super_user.member_dict[mobile_number]['BMI'])
        print('Membership duration in Months  : ',super_user.member_dict[mobile_number]['Duration'])
        print('Password                       : ',super_user.member_dict[mobile_number]['Password'])
    else:
        print('Entered Mobile Number is not registered--')