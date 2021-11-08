import re
class super_user:
    member_dict={}
    def __init__(self,name,age,gender,mobile_number,email,bmi,duration,password):
        self.name=name
        self.gender=gender
        self.age=age
        self.email=email
        self.mobile_number=mobile_number
        self.bmi=bmi
        self.duration=duration
        self.password=password
        super_user.member_dict[mobile_number]={}
        super_user.member_dict[mobile_number]['Name']=name
        super_user.member_dict[mobile_number]['Gender']=gender
        super_user.member_dict[mobile_number]['Age']=age
        super_user.member_dict[mobile_number]['Email']=email
        super_user.member_dict[mobile_number]['Mobile number']=mobile_number
        super_user.member_dict[mobile_number]['BMI']=bmi
        super_user.member_dict[mobile_number]['Duration']=duration
        super_user.member_dict[mobile_number]['Password']=password
        
class workout_regimen:
    regimen={}
    range_list=[]
    def __init__(self,bmi_lower,bmi_upper,mon,tue,wed,thur,fri,sat,sun):
        self.mon=mon
        self.tue=tue
        self.wed=wed
        self.thur=thur
        self.fri=fri
        self.sat=sat
        self.sun=sun
        workout_regimen.range_list.append(bmi_lower)
        workout_regimen.range_list.append(bmi_upper)
        workout_regimen.regimen[(bmi_lower,bmi_upper)]={}
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['monday']=mon
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['tuesday']=tue
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['wednesday']=wed
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['thursday']=thur
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['friday']=fri
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['saturday']=sat
        workout_regimen.regimen[(bmi_lower,bmi_upper)]['sunday']=sun
def create_member():
    print('Enter the name:- ')
    name=input()
    print('Enter the Age:- ')
    while True:
        try:
            age=int(input())
            break
        except:
            print('Please enter the correct age :')
    print('Enter the Gender (M,F,T):- ')
    while True:
        gender=input()
        gender_list=['M','F','T']
        if gender in gender_list:
            break
        else:
            print('Please enter the correct Gender :')
    print('Enter the Mobile Number:- ')
    while True:
        try:
            mobile_number=int(input())
            break
        except:
            print('Please enter the correct Mobile Number :')
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
    print('Enter the BMI 0 to ',max(workout_regimen.range_list),':-')
    while True:
        try:
            bmi=float(input())
            assert bmi>0 and bmi<=max(workout_regimen.range_list)
            break
        except:
            print('Please enter the correct Body Mass Index (BMI) :')
    print('Enter Membership duration in months (1,3,6,12) :- ')
    while True:
        try:
            duration=int(input())
            duration_list=[1,3,6,12]
            if duration in duration_list:
                break
        except:
            print('Please enter the correct Membership Duration :')
    print('Create password for the member:- ')
    password=input()
    print('New Member Registered')
    
    member=super_user(name,age,gender,mobile_number,email,bmi,duration,password)