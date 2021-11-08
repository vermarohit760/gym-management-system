from create_member import *
def delete_member():
    print('Enter the Member Mobile Number to delete details of member: -')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
            
    if mobile_number in super_user.member_dict.keys():
        super_user.member_dict.pop(mobile_number)
        print('Member deleted successfully')
    else:
        print('Entered Mobile Number is not registered--')