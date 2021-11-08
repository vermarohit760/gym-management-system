from create_member import *
from MEMBER import *
def view_my_profile(mobile_number):
    print('Name                           : ',super_user.member_dict[mobile_number]['Name'])
    print('Age                            : ',super_user.member_dict[mobile_number]['Age'])
    print('Gender                         : ',super_user.member_dict[mobile_number]['Gender'])
    print('Mobile Number                  : ',super_user.member_dict[mobile_number]['Mobile number'])
    print('Email                          : ',super_user.member_dict[mobile_number]['Email'])
    print('Body Mass Index(BMI)           : ',super_user.member_dict[mobile_number]['BMI'])
    print('Membership duration in Months  : ',super_user.member_dict[mobile_number]['Duration'])
    print('Password                       : ',super_user.member_dict[mobile_number]['Password'])