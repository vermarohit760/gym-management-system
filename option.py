from SUPER_USER import *
from MEMBER import *
def option():
    while True:
        try:
            print('Select User Type')
            print('1. Super User')
            print('2. Member')
            print('3. Exit')
            user= int(input())
            if user==1:
                SUPER_USER()
            elif user==2:
                MEMBER()
            elif user==3:
                print('Happy Gyming.... VISIT SOON')
                break
            assert user>=1 and user<=3
        except:
            print('Something went wrong . Please select CORRECT option')