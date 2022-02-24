"""
GUNIN WASAN
XII-A
ROLL NO:10

PAYROLL MANAGEMENT

"""

#PAYROLL MANAGEMENT USING SQL CONNECTIVITY:


import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="")
curs=db.cursor()
from prettytable import PrettyTable


def createdatabase():
    sql="create database employee"
    curs.execute(sql)
    sql="use employee"
    curs.execute(sql)
    
def createtableempdetails():
    sql="use employee"
    curs.execute(sql)
    sq="create table EMPLOYEE_DETAILS (empname char(26), empcode numeric(10), empgender char(2),empdateofbirth date, empdateofjoining date, empdesig char(26),empbsal numeric(12,2), empmob numeric(8), empphone numeric(8), empaddress char(26))"
    curs.execute(sq)

def createtableemppayslip():
    sql="use employee"
    curs.execute(sql)
    sql="create table EMPLOYEE_PAYSLIP (empname char(26), empcode numeric(10),empbsal numeric(14,2) ,empda numeric(14,2), emphra numeric(14,2), empconveyance numeric(14,2), empgross numeric(14,2))"
    curs.execute(sql)
    
def monthDatetoName(birthmonth):

    if birthmonth==1:
        nameofmonth="JANUARY"
        return nameofmonth
    if birthmonth==2:
        nameofmonth="FEBRUARY"
        return nameofmonth
    if birthmonth==3:
        nameofmonth="MARCH"
        return nameofmonth
    if birthmonth==4:
        nameofmonth="APRIL"
        return nameofmonth
    if birthmonth==5:
        nameofmonth="MAY"
        return nameofmonth
    if birthmonth==6:
        nameofmonth="JUNE"
        return nameofmonth
    if birthmonth==7:
        nameofmonth="JULY"
        return nameofmonth
    if birthmonth==8:
        nameofmonth="AUGUST"
        return nameofmonth
    if birthmonth==9:
        nameofmonth="SEPTEMBER"
        return nameofmonth
    if birthmonth==10:
        nameofmonth="OCTOBER"
        return nameofmonth
    if birthmonth==11:
        nameofmonth="NOVEMBER"
        return nameofmonth
    if birthmonth==12:
        nameofmonth="DECEMBER"
        return nameofmonth

def makeDDMM(dateMonth):
    if dateMonth==1:
        dateMonth="01"
    if dateMonth==2:
        dateMonth="02"
    if dateMonth==3:
        dateMonth="03"
    if dateMonth==4:
        dateMonth="04"
    if dateMonth==5:
        dateMonth="05"
    if dateMonth==6:
        dateMonth="06"
    if dateMonth==7:
        dateMonth="07"
    if dateMonth==8:
        dateMonth="08"
    if dateMonth==9:
        dateMonth="09"
    
    return dateMonth

def inputtingemployeedata():

    global empno
    global month
    global nodaysworked
    
    sql="use employee"
    curs.execute(sql)
    #CHECKING FOR CORRECT VALUE OF NO. OF EMPLOYEES:
    k=0
    while k==0:
        try:
            n=int(input("Enter the number of employees="))
        except ValueError:
            print("Input the number of employees again")
            continue
        else:
            k+=1
            
    #ADDING EMPLOYEE DETAILS OF n NUMBER OF EMPLOYEES:       
    for k in range(n):
        empname=input("Enter Employee Name=")      

        #AUTO GENERATION OF EMPLOYEE NUMBER:
        empno=1001
        isempno=False
        while not isempno:
            try:
                empno+=k
                sql="select * from EMPLOYEE_DETAILS where empcode={}".format(empno)
                count=curs.execute(sql)
                while count!=0:
                    empno+=1
                    sql="select * from EMPLOYEE_DETAILS where empcode={}".format(empno)
                    count=curs.execute(sql)
                isempno=True
            except:
                print("INPUT EMPLOYEE CODE VALUE AGAIN.")

        print("YOUR AUTO-GENERATED EMPLOYEE NUMBER IS=",empno)
            
        #CHECKING FOR CORRECT INPUT OF EMPLOYEE GENDER:
        empgender=input("Employee Gender=")
        empgender=empgender.upper()

            
        #CHECKING FOR CORRECT INPUT OF EMPLOYEE DOB:
        isyear=False
        while not isyear:
            try:
                birthyear=int(input("Enter the Birth Year="))
                if birthyear>=1900 and birthyear<=2020:
                    isyear=True
            except:
                print("Input Birth Year Again.")

        ismonth=False
        while not ismonth:
            try:
                birthmonth=int(input("Enter the Birth Month="))
                if birthmonth>=1 and birthmonth<=12:
                    ismonth=True
                    nameofmonth=monthDatetoName(birthmonth)

            except:
                print("Input Birth Month Again")
                        
        isday=False
        while not isday:
            try:
                birthday=int(input("Enter the Day of Birth="))
                if birthday>=1 and birthday<=31:
                    if nameofmonth=="JANUARY" or  nameofmonth=="MARCH" or nameofmonth=="MAY" or nameofmonth=="JULY" or nameofmonth=="AUGUST" or nameofmonth=="OCTOBER" or nameofmonth=="DECEMBER":
                        isday=True
                
                if birthday>=1 and birthday<=30:
                    if nameofmonth=="APRIL" or nameofmonth=="JUNE" or  nameofmonth=="SEPTEMBER" or nameofmonth=="NOVEMBER":
                        isday=True
        ####
                if birthyear//100!=0 or birthyear//400==0 or birthyear//4==0:
                    if nameofmonth=="FEBRUARY" and birthday==29:
                        isday=True
                    
                if birthyear//100==0 or birthyear//400!=0 or birthyear//4!=0:
                    if nameofmonth=="FEBRUARY" and birthday==28:
                        isday=True
                                
                if birthday>=1 and birthday<=28:
                    isday=True

            except:
                print("Input Birth Day Again")
                
        #MAKING BIRTHDAY IN DD FORMAT:
        birthday=makeDDMM(birthday)
                    
        #MAKING BIRTH MONTH IN MM FORMAT:
        birthday=makeDDMM(birthmonth)
           
        empdob=str(birthyear)+"-"+str(birthmonth)+"-"+str(birthday)
      
        #CHECKING FOR CORRECT INPUT OF EMPLOYEE DOJ:
        isyear=False
        while not isyear:
            try:
                joinyear=int(input("Enter the join Year="))
                if joinyear>=1900 and joinyear<=2020:
                    isyear=True
            except:
                print("Input join Year Again.")

        ismonth=False
        while not ismonth:
            try:
                joinmonth=int(input("Enter the join Month="))
                if joinmonth>=1 and joinmonth<=12:
                    ismonth=True
                    nameofmonth=monthDatetoName(joinmonth)                      
            except:
                print("Input join Month Again")
                
        isday=False
        while not isday:
            try:
                joinday=int(input("Enter the day of joining="))
                if joinday>=1 and joinday<=31:
                    if nameofmonth=="JANUARY" or  nameofmonth=="MARCH" or nameofmonth=="MAY" or nameofmonth=="JULY" or nameofmonth=="AUGUST" or nameofmonth=="OCTOBER" or nameofmonth=="DECEMBER":
                        isday=True
                
                if joinday>=1 and joinday<=30:
                    if nameofmonth=="APRIL" or nameofmonth=="JUNE" or  nameofmonth=="SEPTEMBER" or nameofmonth=="NOVEMBER":
                        isday=True
        ####
                if joinyear//100!=0 or joinyear//400==0 or joinyear//4==0:
                    if nameofmonth=="FEBRUARY" and joinday==29:
                        isday=True
                    
                if joinyear//100==0 or joinyear//400!=0 or joinyear//4!=0:
                    if nameofmonth=="FEBRUARY" and joinday==28:
                        isday=True
                                
                if joinday>=1 and joinday<=28:
                    isday=True


            except:
                print("Input join Day Again")
        
        #MAKING JOINING DATE IN DD FORMAT:
        birthday=makeDDMM(joinday)
                    
        #MAKING BIRTH MONTH IN MM FORMAT:
        joinday=makeDDMM(birthmonth)
        #MAKING JOIN MONTH IN MM FORMAT:
        joinmonth=makeDDMM(birthmonth)           
        empdoj=str(joinyear)+"-"+str(joinmonth)+"-"+str(joinday)
        
        #EMPLOYEE DESIGNATION:    
        empdesig=input("Enter the designation of the Employee=")

        #CHECKING FOR CORRECT INPUR OF EMPBSAL:
        isbasic=False
        while not isbasic:
            try:
                empbsal= float(input("Enter the Basic Salary of the Employee="))
                isbasic=True
            except ValueError:
                print("INCORRECT INPUT. TRY AGAIN!")
            else:
                print(empbsal)
                
        #CHECKING FOR CORRECT INPUT OF HOME NUMBER:     
        isnumber=False
        while not isnumber:
            try:
                empmob= int(input("Enter the employee mobile number="))
                if len(str(empmob))==8:
                    isnumber=True
            except ValueError:
                print("Incorrect Value. Input Employee mobile number again and it should be an 8 digit number")
            
        #CHECKING FOR CORRECT INPUT OF HOME NUMBER:     
        number=False
        while not number:
            try:
                empphone=int(input("Enter the employee home number="))
                if len(str(empphone))==8:
                    number=True
            except ValueError:
                print("Incorrect Value. Input Employee home number again and it should be an 8 digit number")

            
        empaddr= input("Enter employee address=")
        
        sql="insert into EMPLOYEE_DETAILS values ('{}',{},'{}','{}','{}','{}',{},{},{},'{}')".format(empname,empno,empgender,empdob,empdoj,empdesig,empbsal,empmob,empphone,empaddr)
        curs.execute(sql)

    ###----------------------------------------------------------------------------------------------------------------------------------

    #ADDING DATA IN EMPLOYEE PAY SLIP:
    
    #CHECKING FOR CORRECT INPUT OF MONTH:
    ismonth=False
    while not ismonth:
        try:
            month=input("Name of the Month=")
            month=month.upper()
            if month=="JANUARY" or  month=="FEBRUARY" or month=="MARCH" or month=="APRIL" or month=="MAY" or month=="JUNE" or month=="JULY" or month=="AUGUST" or month=="SEPTEMBER" or month=="OCTOBER" or  month=="NOVEMBER" or month=="December":
                ismonth=True
        except ValueError:
            print("INCORRECT VALUE, Input the month again")
            
    #CHECKING FOR CORRECT YEAR:
    isyear=False
    while not isyear:
        try:        
            year=int(input("Which Year="))
            if year>=1960 and year<=2020:
                isyear=True
        except:
            print("INCORRECT VALUE OR RANGE EXCEEDS THE GIVEN RANGE")
            
    #CHECKING FOR CORRECT INPUT OF NO.OF DAYS WORKED:
    isdays=False
    try:
        nodaysworked=int(input("Enter the number of days worked="))
        if nodaysworked>=0 and nodaysworked<=31:
            isdays=True
    except ValueError:
        print("INCORRECT VALUE. PLEASE ENTER AGAIN")
        
    #CALCULATING BASIC SALARY:
        
    if month=="JANUARY" or  month=="MARCH" or month=="MAY" or month=="JULY" or month=="AUGUST" or month=="OCTOBER" or month=="DECEMBER":
        if nodaysworked==31: 
            actualbasic=float(empbsal)
        else:
            bsaldaily=empbsal/31
            actualbasic=nodaysworked*bsaldaily
            
    if month=="SEPTEMBER" or month=="APRIL" or month=="JUNE" or month=="NOVEMBER":
        if nodaysworked==30:
            actualbasic=float(empbsal)
        else:
            bsaldaily=empbsal/30
            actualbasic=nodaysworked*bsaldaily
            
    #CHECKING FOR LEAP YEAR:
            
    if year//100!=0 or year//400==0 or year//4==0:
        if month=="FEBRUARY" and nodaysworked==29:
            actualsal=empbsal
        else:
            bsaldaily=empbsal/29
            actualbasic=nodaysworked*bsaldaily
            
    if year//100==0 or year//400!=0 or year//4!=0:
        if month=="FERBUARY" and nodaysworked==28:
            actualbasic=float(empbsal)
        else:
            bsaldaily=empbsal/28
            actualbasic=nodaysworked*bsaldaily
    
        
        
    da=0.55*actualbasic
    hra=0.35*actualbasic
    conveyance=0.15*actualbasic
    gross=actualbasic+da+hra+conveyance
    
    if gross<=250000:
        itax=0
    if gross>=250000 and gross<=500000:
        itax=(gross-250000)*0.05
    if gross>=500000 and gross<=1000000:
        itax=12500+((gross-500000)*0.1)
    if gross>=1000000:
        itax=62500+((gross-1000000)*0.2)
        
    netsal=gross-itax

    #INPUTTING DATA IN EMPLOYEE_PAYSLIP:
    sql="insert into EMPLOYEE_PAYSLIP values ('{}',{},{},{},{},{},{})".format(empname,empno,actualbasic,da,hra,conveyance,gross)
    curs.execute(sql)

    


def showtables():
    from prettytable import PrettyTable
    x = PrettyTable()
    curs.execute("use employee")
    curs.execute("select * from EMPLOYEE_DETAILS")
    data=curs.fetchall()
    x.field_names = ["Employee Name", "Employee Number", "Basic Sal", "Dearness Allowance","HRA","Conveyance","Gross Salary"]
    for teacher in data:
        for col in teacher:
            print(col,end="\t||  ")
        print()
    #---------------------------------------#    
    print("-"*12)
    print("-"*11)
    print("-"*10)
    #---------------------------------------#
    curs.execute("select * from EMPLOYEE_PAYSLIP")
    data=curs.fetchall()
    for teacher in data:
        for col in teacher:
            print("DISPLAYING PAYSLIP FOR=",empno, "   MONTH=", month,   "     NO.OF DAYS WORKED=", nodaysworked)
            print(col,end="\t    ")
        print()
        
def deleterows():
    curs.execute("use employee")
    code=int(input("Enter Employee code you want to delete="))
    sql="delete from EMPLOYEE_DETAILS where empcode={}".format(code)
    count=curs.execute(sql)
    if count>0:
        print("RECORD DELETED")
        db.commit()
    else:
        print("Row with empcode={} was not found".format(code))

def searchemp():
    curs.execute("use employee")
    code=int(input("Enter Employee code you want to search="))
    sql=" SELECT * FROM EMPLOYEE_DETAILS where empcode={}".format(code)
    count=curs.execute(sql)
    if count>0:
        curs.fetchone()
    else:
        print("Row with empcode={} was not found".format(code))
    

while True:
    
    print("MENU OPTIONS:")
    print("1.Create a new database")
    print("2.Create Employee Details Table")
    print("3.Create Employee Pay Slip Table")
    print("4. Enter Employee details and salary information")
    print("5. Display Tables")
    print("6. Delete an Employee Record")
    print("7. Search for an Employee Record")
    print("0. Exit")
    
    ch=int(input("Enter Menu Option="))
    if ch==1:
        createdatabase()
        print("DATABASE CREATED")
        print("-"*18)
        
    if ch==2:
        createtableempdetails()
        print("Table EMPLOYEE_DETAILS CREATED")
        print("-"*18)
        
    if ch==3:
        createtableemppayslip()
        print("Table EMPLOYEE_PAYSLIP CREATED")
        print("-"*18)
        
    if ch==4:
        inputtingemployeedata()
        print("EMPLOYEE DATA HAS BEEN INPUTTED")
        print("-"*18)
        
    if ch==5:
        showtables()
        print("-"*18)
        
    if ch==6:
        deleterows()
        print("-"*18)
        
    if ch==7:
        searchemp()
        print("-"*18)

    if ch==0:
        break