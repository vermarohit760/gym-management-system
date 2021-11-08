from create_member import *
from view_member import *
from delete_member import *
from update_member import *
from create_regimen import *
from view_regimen import *
from delete_regimen import *
from update_regimen import *
def SUPER_USER():
    print('HELLOOOOOO Super User.... Please select one option from given list:---')
    while True:
        try:
            print('1. Create Member')
            print('2. View Member')
            print('3. Delete Member')
            print('4. Update Member')
            print('5. Create Regimen')
            print('6. View Regimen')
            print('7. Delete Regimen')
            print('8. Update Regimen')
            print('9. Logout')
            n=int(input())
            if n==1:
                create_member()
            elif n==2:
                view_member()
            elif n==3:
                delete_member()
            elif n==4:
                update_member()
            elif n==5:
                create_regimen()
            elif n==6:
                view_regimen()
            elif n==7:
                delete_regimen()
            elif n==8:
                update_regimen()
            elif n==9:
                print('Logging Out')
                break
            assert n>=1 and n<=9
        except:
            print('Something went wrong, please select correct option')