import math
from prettytable import PrettyTable
import re

karyawan = [{'EmployeeID':'001',
             'Name':'Bima',
             'Department':'Operation',
             'Position':'Foreman',
             'HireDate':'03-10-2016',
             'Salary':5000000,
             'Status':'Active'},
             {'EmployeeID':'002',
             'Name':'Rangga',
             'Department':'HR',
             'Position':'Staff',
             'HireDate':'25-12-2016',
             'Salary':4500000,
             'Status':'Active'},
             {'EmployeeID':'003',
             'Name':'Bima',
             'Department':'Operation',
             'Position':'Staff',
             'HireDate':'25-12-2017',
             'Salary':4500000,
             'Status':'Resign'}
            ]

newKaryawan = []
x = ['']

def clear():
    newKaryawan.clear()

def cek():
    if len(newKaryawan) > 0:
        for i in range(len(newKaryawan)):
            tabelKaryawan.add_row([newKaryawan[i]['EmployeeID'],newKaryawan[i]['Name'],newKaryawan[i]['HireDate'],
                               newKaryawan[i]['Department'],newKaryawan[i]['Position'],newKaryawan[i]['Salary'],newKaryawan[i]['Status']])
        print('*************** List of Employee Data ***************\n')
        print(tabelKaryawan)
        x[0] = 'lanjut'
    else:
        print('***************** The data you are looking for does not exist *****************')  

def mainMenu():
    print('''
    ********** Welcome **********
    1. Employee data
    2. Create new employee data
    3. Update employee data
    4. Delete employee data
    5. Exit
    ''')

def menuRead():
    print('''
    ********** Employee Data **********
    1. List of all employee data
    2. List of department/position
    3. Looking for a specific employee
    4. Back to main menu
    ''')

def read():
    print('*************** List of All Employee Data ***************\n')
    for i in range(len(karyawan)):
        tabelKaryawan.add_row([karyawan[i]['EmployeeID'],karyawan[i]['Name'],karyawan[i]['HireDate'],
                               karyawan[i]['Department'],karyawan[i]['Position'],karyawan[i]['Salary'],
                               karyawan[i]['Status']])
    print(tabelKaryawan)

def department():
    print('*************** List of {} ***************\n'.format(inputDepartment))
    tabelDepartment = PrettyTable()
    dept =[karyawan[0][inputDepartment]]  
    for i in range(len(karyawan)-1):
        dept.append(karyawan[i+1][inputDepartment])  
    dept = list(set(dept))
    tabelDepartment.add_column(inputDepartment,dept)  
    print(tabelDepartment)
        
def spesifik():
    TabelColumn = PrettyTable()
    TabelColumn.add_column('Column',['EmployeeID', 'Name','Department', 'Position', 'Salary', 'HireDate', 'Status'])
    print(TabelColumn)
   
def readSpesifikString():
    enterData1 = input('Input data [{}]: '.format(selectColumn))
    for i in range(len(karyawan)):
        search = enterData1 in karyawan[i][selectColumn]
        if search == True:
            newKaryawan.append({'EmployeeID':karyawan[i]['EmployeeID'],
             'Name':karyawan[i]['Name'],
             'Department':karyawan[i]['Department'],
             'Position':karyawan[i]['Position'],
             'HireDate':karyawan[i]['HireDate'],
             'Salary':karyawan[i]['Salary'],
             'Status':karyawan[i]['Status']})

def menuSorting():
    print('''
    ********** Sorting Employee Data by {} **********
    1. Sorting by range
    2. Sorting by minimum
    3. Sorting by maximum
    '''.format(selectColumn))

def readSpesifikInt():
    print('Enter the salary range')
    enterData1 = int(input('Input min salary: '))
    enterData2 = int(input('Input max salary: '))
    for i in range(len(karyawan)):
        if enterData1 <= karyawan[i][selectColumn] <= enterData2:
            newKaryawan.append({'EmployeeID':karyawan[i]['EmployeeID'],
             'Name':karyawan[i]['Name'],
             'Department':karyawan[i]['Department'],
             'Position':karyawan[i]['Position'],
             'HireDate':karyawan[i]['HireDate'],
             'Salary':karyawan[i]['Salary'],
             'Status':karyawan[i]['Status']})

def spesifikTanggal():
    print('Enter the year range')
    year1 = int(input('Input min year: '))
    year2 = int(input('Input max year: '))
    for i in range(len(karyawan)):
        karyawanYear = (re.findall('\d{4}',karyawan[i]['HireDate']))
        karyawanYear = int(karyawanYear[0])
        if year1 <= karyawanYear <= year2:
            newKaryawan.append({'EmployeeID':karyawan[i]['EmployeeID'],
             'Name':karyawan[i]['Name'],
             'Department':karyawan[i]['Department'],
             'Position':karyawan[i]['Position'],
             'HireDate':karyawan[i]['HireDate'],
             'Salary':karyawan[i]['Salary'],
             'Status':karyawan[i]['Status']})

def sorting():
    if selectColumn == 'HireDate':
        for i in range(len(karyawan)):
            karyawanYear = (re.findall('\d{4}',karyawan[i]['HireDate']))
            karyawanYear = int(karyawanYear[0])
            newKaryawan.append(karyawanYear)
    elif selectColumn == 'Salary': 
        for i in range(len(karyawan)):
            newKaryawan.append(karyawan[i][selectColumn])
    newKaryawan.sort() 

def minimumSort():
    sort = 'minimum'
    sortData = int(input('Input {} {}: '.format(sort,selectColumn)))
    for a in range (len(newKaryawan)):
        for b in newKaryawan:
            if b < sortData:
                newKaryawan.remove(b)

def maximumSort():
    sort = 'maximum'
    sortData = int(input('Input {} {}: '.format(sort,selectColumn)))
    for a in range (len(newKaryawan)):
        for b in newKaryawan:
            if b > sortData:
                newKaryawan.remove(b)

def sortSalary():
    for j in newKaryawan:
        for i in range(len(karyawan)):
            if j == karyawan[i][selectColumn]:
                newKaryawan[newKaryawan.index(j)]= {'EmployeeID':karyawan[i]['EmployeeID'],
                                                    'Name':karyawan[i]['Name'],
                                                    'Department':karyawan[i]['Department'],
                                                    'Position':karyawan[i]['Position'],
                                                    'HireDate':karyawan[i]['HireDate'],
                                                    'Salary':karyawan[i]['Salary'],
                                                    'Status':karyawan[i]['Status']}

def sortHireDate():
    for x in range(len(newKaryawan)):
        newKaryawan[x]=str(newKaryawan[x])
    for j in newKaryawan:
        for i in range(len(karyawan)):
            dateHire = (re.findall('\d{4}',karyawan[i]['HireDate']))
            if j == dateHire[0]:
                newKaryawan[newKaryawan.index(j)]= {'EmployeeID':karyawan[i]['EmployeeID'],
                                                        'Name':karyawan[i]['Name'],
                                                        'Department':karyawan[i]['Department'],
                                                        'Position':karyawan[i]['Position'],
                                                        'HireDate':karyawan[i]['HireDate'],
                                                        'Salary':karyawan[i]['Salary'],
                                                        'Status':karyawan[i]['Status']}

def menuCreate():
    print('''
    ********** Create New Employee Data **********
    1. Create new data
    2. Back to main menu
    ''')

def create():
    createID = input('Input employeeID: ')
    createName = input('Input name: ')
    createHireDate = input('Input hire date[DD-MM-YYYY]: ')
    createDepartment = input('Input department: ')
    createPosition = input('Input position: ')
    createSalary = int(input('Input salary: '))
    newKaryawan.append({'EmployeeID':createID,
             'Name':createName,
             'Department':createDepartment,
             'Position':createPosition,
             'HireDate':createHireDate,
             'Salary':createSalary,
             'Status':'Active'})
    for i in range(len(karyawan)):
        if karyawan[i]['EmployeeID'] == newKaryawan[0]['EmployeeID']:
            newKaryawan.clear()
            break

def createConfimr():
    print('********** Create New Employee Data **********')
    tabelNewKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary","Status"])
    tabelNewKaryawan.add_row([newKaryawan[0]['EmployeeID'],newKaryawan[0]['Name'],newKaryawan[0]['HireDate'],
                               newKaryawan[0]['Department'],newKaryawan[0]['Position'],newKaryawan[0]['Salary'],
                               newKaryawan[0]['Status']])
    print(tabelNewKaryawan)
    while True:
        createKonf = input('Saving data [Y/N]: ')
        if createKonf == 'Y':
            karyawan.extend(newKaryawan)
            print('************ Data Successfully Saved ************')
            newKaryawan.clear()
            break
        elif createKonf == 'N':
            print('************ Data Successfully Not Saved ************')
            newKaryawan.clear()
            break
        else: 
            print('***************** The option you entered is not valid *****************')

def menuUpdate():
    print('''
    ********** Update Employee Data **********
    1. Update employees data
    2. Back to main menu
    ''')

def update():
    selectColumn = input('Input column that want to update(separate with commas): ').split(',')
    for i in selectColumn:
        if selectColumn == 'Salary':
            updateData = int(input('Input new data: '))
        updateData = input('Input new data in {}: '.format(i))
        newKaryawan[0][i] = updateData
        for j in range(len(karyawan)):
            if karyawan[j]['EmployeeID'] == newKaryawan[0]['EmployeeID']:
                karyawan[j][i] = updateData
    print('***************** Data successfully update *****************')

def menuDelete():
    print('''
    ********** Delete Employee Data **********
    1. Delete employees data
    2. Delete all employee data that resigned
    3. Back to main menu
    ''')

def delete():
    deleteEmpID = input('Input EmployeeID that want to delete(separate with commas): ').split(',')
    for i in deleteEmpID:
        for j in range(len(karyawan)-1):
            if karyawan[j]['EmployeeID'] == i:
                del karyawan[j]
            elif karyawan[j-1]['EmployeeID'] == i:
                del karyawan[j-1]
    print('***************** Data successfully deleted *****************')

def deleteResign():
    deleteEmpID = ['Resign']
    for i in deleteEmpID:
        for j in range(len(karyawan)-1):
            if karyawan[j]['Status'] == i:
                del karyawan[j]
            elif karyawan[j-1]['Status'] == i:
                del karyawan[j-1]
    print('***************** Data successfully deleted *****************')

while True:
    mainMenu()
    menu = input('Please select menu [1-5]: ')
    if menu == '1':
        while True:
            tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
            menuRead()
            clear()
            x[0]=''
            readMenu = input('Please select menu [1-4]: ')
            if readMenu == '1':
                read()
            elif readMenu == '2':
                TabelColumn = PrettyTable()
                TabelColumn.add_column('Column',['Department', 'Position'])
                print(TabelColumn)
                inputDepartment = input('Type [Department/Position] to see the list: ').capitalize()
                department()
            elif readMenu == '3':
                spesifik()
                selectColumn = input('Select search by column: ')
                if (selectColumn == 'EmployeeID') or (selectColumn  == 'Name') or (selectColumn == 'Department') or (selectColumn == 'Position') or (selectColumn == 'Status'):
                    readSpesifikString()
                    cek()
                elif (selectColumn == 'Salary') or (selectColumn == 'HireDate'):
                    while True:
                        menuSorting()
                        sortingMenu = input('Please select menu [1-3]: ')
                        if sortingMenu == '1': 
                            if selectColumn == 'Salary': 
                                readSpesifikInt()
                            else:
                                spesifikTanggal()
                            cek()
                            break
                        elif sortingMenu == '2':
                            sorting()
                            minimumSort()
                            if selectColumn == 'Salary':
                                sortSalary()
                                cek()
                            else:
                                sortHireDate()
                                cek()
                            break
                        elif sortingMenu == '3':
                            sorting()
                            maximumSort()
                            if selectColumn == 'Salary':
                                sortSalary()
                                cek()
                            else:
                                sortHireDate()
                                cek()
                            break 
                        else:
                            print('***************** The option you entered is not valid *****************') 
                else:
                    print('***************** The option you entered is not valid *****************')
            elif readMenu == '4':
                break
            else:
                print('***************** The option you entered is not valid *****************')
                continue
    elif menu == '2':
        while True:
            menuCreate()
            createMenu = input('Please select menu [1-2]: ')
            if createMenu == '1':
                create()
                if len(newKaryawan) == 0:
                    print('\n********* Data already exists *********')
                else:
                    createConfimr()
            elif createMenu == '2':
                break
            else:
                print('***************** The option you entered is not valid *****************')
    elif menu == '3':
        while True:
            menuUpdate()
            x[0] = ''
            clear()
            tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
            updateMenu = input('Please select menu [1-2]: ')
            if updateMenu == '1':
                selectColumn = input('Search by [EmployeeID/Name/Status]: ')
                if selectColumn == 'EmployeeID':
                    print('Input EmployeeID')
                    readSpesifikString()
                    cek()
                    if x[0] == 'lanjut':
                        pilihanUpd = input('Continue update[Y/N]: ')
                        if pilihanUpd == 'Y':
                            update()
                        elif pilihanUpd == 'N':
                            continue
                        else:
                            print('***************** The option you entered is not valid *****************')
                elif selectColumn == 'Status':
                    print('Input Status[Active/Resign]')
                    readSpesifikString()
                    cek()
                    clear()
                    tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
                    if x[0] == 'lanjut':
                        x[0] =''
                        selectColumn = 'EmployeeID'
                        print('Input EmployeeID')
                        readSpesifikString()
                        cek()
                        if x[0] == 'lanjut':
                            pilihanUpd = input('Continue update[Y/N]: ')
                            if pilihanUpd == 'Y':
                                update()
                            elif pilihanUpd == 'N':
                                continue
                            else:
                                print('***************** The option you entered is not valid *****************')
                elif selectColumn == 'Name':
                    print('Input Name')
                    readSpesifikString()
                    cek()
                    clear()
                    tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
                    if x[0] == 'lanjut':
                        x[0] =''
                        selectColumn = 'EmployeeID'
                        print('Input EmployeeID')
                        readSpesifikString()
                        cek()
                        if x[0] == 'lanjut':
                            pilihanUpd = input('Continue update[Y/N]: ')
                            if pilihanUpd == 'Y':
                                update()
                            elif pilihanUpd == 'N':
                                continue
                            else:
                                print('***************** The option you entered is not valid *****************')
                else:
                    print('***************** The option you entered is not valid *****************')
            elif updateMenu == '2':
                break
            else:
                print('***************** The option you entered is not valid *****************')
                continue 
    elif menu == '4':
        while True:
            menuDelete()
            clear()
            tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
            x[0] = ''
            deleteMenu = input('Please select menu [1-2]: ')
            if deleteMenu == '1':
                selectColumn = input('Search by [EmployeeID/Name]: ')
                if selectColumn == 'EmployeeID':
                    print('Input EmployeeID')
                    readSpesifikString()
                    cek()
                    if x[0] == 'lanjut':
                        pilihanUpd = input('Continue delete[Y/N]: ')
                        if pilihanUpd == 'Y':
                            delete()
                        elif pilihanUpd == 'N':
                            continue
                        else:
                            print('***************** The option you entered is not valid *****************')
                elif selectColumn == 'Name':
                    print('Input Name')
                    readSpesifikString()
                    cek()
                    clear()
                    tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
                    if x[0] == 'lanjut':
                        pilihanUpd = input('Continue delete[Y/N]: ')
                        if pilihanUpd == 'Y':
                            delete()
                        elif pilihanUpd == 'N':
                            continue
                        else:
                            print('***************** The option you entered is not valid *****************')
            elif deleteMenu == '2':
                print('please input [Resign]')
                selectColumn = 'Status'
                readSpesifikString()
                cek()
                clear()
                tabelKaryawan = PrettyTable(["EmployeeID", "Name", "HireDate", "Department", "Position", "Salary", "Status"])
                if x[0] == 'lanjut':
                    pilihanUpd = input('Continue delete[Y/N]: ')
                    if pilihanUpd == 'Y':
                        deleteResign()
                    elif pilihanUpd == 'N':
                        continue
                    else:
                        print('***************** The option you entered is not valid *****************')
            elif deleteMenu == '3':
                break
            else:
                print('***************** The option you entered is not valid *****************')
    elif menu == '5':
        print('''
        ************** Thank You *************
        ************** Good Bye! *************
        ''')
        break
    else:
        print('***************** The option you entered is not valid *****************') 