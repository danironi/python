#B00350882
import datetime
import json
import pickle
import os
import glob
import re


now = datetime.datetime.now()


class Batch:

    def __init__(self, batch_id, comp_num, location):
        self.batch_id = batch_id

        self.comp_num = comp_num

        self.location = location

    def display(self):
        print(self.batch_id)


class Component:

    def __init__(self, ty_pe, size_fitment, serial_num, status):
        self.ty_pe = ty_pe

        self.size_fitment = size_fitment

        self.serial_num = serial_num

        self.status = status

    def displayComp(self):
        print(self.serial_num)


q = 0

x = 0

p = 0


choices = ('1','2','3')
choices2 = ('1','2','3')
choices3 = ('1','2')
answers = ('y','Y','n','N')

#Global variables
ty_pes = ['Winglet Struts', 'Door Handle', 'Rudder Pin']
size_fitments = ['A320', 'A380', '10mm x 75mm', '12mm x 100mm', '16mm x 150mm', 'Universal fit']
size_fitment = 'A320'
comp_status = ""
serial_num = ""
statuses = ["Manufactured - Unfinished"]
finish = ["Unfinished", "Polished"]
manufacturetime = str(now.strftime("%Y")) + str(now.strftime("%m")) + str(now.strftime("%d"))
location = ['Factory Floor - Warehouse Not Allocated', 'Paisley', 'Dubai']
data = {}
data["batch"] = []


# function to check if a file exists, this file is BatchIndex.json in our case
def where_json(filename):
    return os.path.exists(filename)


# function to check if the value of input is an integer otherwise handling errors
def isNumber(value):

        try:

            var = int(value)
            if 0 < var < 10000:
                return True

        except (TypeError, ValueError):
            return False


#function to print the menu out
def menu():
    print("Please select an option :")
    print("1 \t Create a new batch")
    print("2 \t List all batches")
    print("3 \t View details of a batch")
    print("4 \t View details of a component")
    print("5 \t Allocate manufactured stock")
    print("6 \t Search by product type")
    print("7 \t Finish a component")
    print("8 \t Quit")

#function to allocate manufactures stock
def stocklocation():
    print("Select Warehouse :")
    print("1 Paisley")
    print("2 Dubai")

# function to print component type choices
def comptype():
    print("Select component type:")
    print("1 Winglet Struts")
    print("2 Door Handle")
    print("3 Rudder Pin")


# function to print fitment type choices
def size_fit1():
    print("Select size/fitment type:")
    print("1 A320 Series")
    print("2 A380 Series")


# function to print size choices
def size_fit2():
    print("Select size/fitment type:")
    print("1 10mm x 75mm")
    print("2 12mm x 100mm")
    print("3 16mm x 150mm")

# function to select a finish type such as polished or painted with a color code
def selectfinish():
    print("Select finish:")
    print("1 Polished")
    print("2 Painted")

# this is the function to create batches. This function is called when you press menupoint 1
def createBatch():
    size_fitment = ''
    ty_pe = ''
    comp = Component(ty_pe='', size_fitment='', serial_num='', status='')

    #built-in function to save data into json and pickle files
    def savedata(batch, batchdata, comp_num, data):
        picklefiles = batch.batch_id
        with open("..\B00350882\Data\ " + picklefiles + '.' + 'pck', 'wb') as f:
            pickle.dump(batchdata, f)

        for q in range(int(comp_num)):
            q = q + 1

            p = "000" + str(q)

            if q > 9:
                p = "00" + str(q)
            if q > 99:
                p = "0" + str(q)
            if q > 999:
                p = str(q)
            serial_num = batch.batch_id + '-' + p
            serial_num_pickle = batch.batch_id + "_" + p
            compdata = [serial_num, comp.ty_pe, comp.size_fitment, manufacturetime, status]
            with open("..\B00350882\Data\ " + serial_num_pickle + '.pck', 'wb') as f:
                pickle.dump(compdata, f)

        # here the BatchIndex.json file opens up and the previously created data dictionary is dumped into it
        with open("..\B00350882\Data\BatchIndex.json", "w") as outfile:
            json.dump(data, outfile, indent=2)

    # built-in function which append each batch into a dictionary as a list. I just call this after answering the "this contains..." question with yes
    def pushbatch():
        data['batch'].append({
            "Batchnumber": batch.batch_id,
            "Location": location[0],
            "Manufacture date": manufacturetime,
            "Component type": comp.ty_pe,
            "Component size/fitment type": comp.size_fitment,
            "Number of comps in batch": batch.comp_num,
            "Serial numbers": seriallist,
            "Component status": statuslist
        })

    # built-in function to print the actual batch out after answering the "Would you print the batch details?" question with yes
    def printoutbatch():
        print("Batch Number : " + batch.batch_id)
        print("Location : " + location[0])
        print("Manufacture Date : " + manufacturetime)
        print("Component Type : " + comp.ty_pe)
        print("Component Size/Fitment Type : " + comp.size_fitment)
        print("Number of Components in Batch : " + batch.comp_num)
        print("Serial Numbers : " + str(seriallist))
        print("Component Status : " + str(statuslist))
        print("-------------------------------------")


    z = input("Enter a number between 1 and 9999:")
    c = isNumber(z)
    # loop to check the input is integer, keep looping until inputting an integer
    while c is not True:
        print("Wrong input")
        z = input("Enter a number between 1 and 9999:")
        c = isNumber(z)
        continue
    # here is the last 4 digits of batch id number created
    x = "000" + str(z)

    if int(z) < 10:
        x = "000" + str(z)
    if 10 <= int(z) < 100:
        x = "00" + str(z)
    if 100 <= int(z) < 1000:
        x = "0" + str(z)
    if int(z) >= 1000:
        x = str(z)

    batch_id = manufacturetime + x
    while batch_id in s:
        z = int(input("Enter a number between 1 and 9999:"))

        x = "000" + str(z)

        if z < 10:
            x = "000" + str(z)
        if 10 <= z < 100:
            x = "00" + str(z)
        if 100 <= z < 1000:
            x = "0" + str(z)
        if z >= 1000:
            x = str(z)

        batch_id = manufacturetime + x

    else:
        while True:
            comp_num = input("Enter number of components: ")
            batch = Batch(batch_id, comp_num, location)
            # checking if the input is an integer, if not then it continues asking to enter number of components
            while isNumber(comp_num) is not True:
                print("Wrong input")
                comp_num = input("Enter number of components: ")
            # if the input is number then the program continues to execute
            if isNumber(comp_num):
                seriallist = []
                statuslist = []
                batchdata = [batch.batch_id, batch.comp_num, location[0]]

                # I use 'for' loop to create the last 4 digits of sequential serial number
                for q in range(int(comp_num)):
                    q = q + 1
                    global p
                    p = "000" + str(q)

                    if q > 9:
                        p = "00" + str(q)
                    if q > 99:
                        p = "0" + str(q)
                    if q > 999:
                        p = str(q)

                    global status
                    global serial_num

                    serial_num = batch.batch_id + "-" + p
                    status = statuses[0]
                    comp = Component(ty_pe, size_fitment, serial_num, status)
                    comp_status = comp.serial_num + " " + comp.status  # this will create the serial number with its status
                    seriallist.append(comp.serial_num)
                    statuslist.append(comp_status)


                comptype()
                seltype = input(">")
                while seltype not in choices:
                    comptype()
                    seltype = input(">")
                else:
                    if seltype == '1':
                        ty_pe = ty_pes[0]
                        size_fit1()
                        seltype2 = input(">")
                        while seltype2 not in choices3:
                            size_fit1()

                            seltype2 = input(">")
                        else:
                            if seltype2 == '1':
                                size_fitment = size_fitments[0]
                                comp = Component(ty_pe, size_fitment, serial_num = '', status='')
                                print(
                                    "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                ans = input(">")
                                while ans not in answers:
                                    print(
                                        "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + ty_pe + " " + " is this correct, Y/N?")

                                    ans = input(">")
                                else:
                                    if ans == 'y' or ans == 'Y':
                                        pushbatch()

                                        savedata(batch, batchdata, comp_num, data)
                                        print("Batch and component records created at " + str(now.strftime("%H"))+":"+str(now.strftime("%M"))+" on "+manufacturetime)
                                        print("Would you print the batch details? Y/N")
                                        ans2 = input(">")
                                        while ans2 not in answers:
                                            print("Would you print the batch details? Y/N")
                                            ans2 = input(">")
                                        else:

                                            if ans2 == 'y' or ans2 == 'Y':

                                                printoutbatch()
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                            if ans2 == 'n' or ans2 == 'N':
                                                print("ok")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                    if ans == 'n' or ans == 'N':

                                        continue
                            if seltype2 == '2':
                                size_fitment = size_fitments[1]
                                comp = Component(ty_pe, size_fitment, serial_num='', status='')
                                print(
                                    "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                ans = input(">")
                                while ans not in answers:
                                    print(
                                        "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                    ans = input(">")
                                else:
                                    if ans == 'y' or ans == 'Y':
                                        pushbatch()

                                        savedata(batch, batchdata, comp_num, data)
                                        print("Batch and component records created at " + str(now.strftime("%H"))+":"+str(now.strftime("%M"))+" on "+manufacturetime)
                                        print("Would you print the batch details? Y/N")
                                        ans2 = input(">")
                                        while ans2 not in answers:
                                            print("Would you print the batch details? Y/N")
                                            ans2 = input(">")
                                        else:

                                            if ans2 == 'y' or ans2 == 'Y':

                                                printoutbatch()
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                            if ans2 == 'n' or ans2 == 'N':
                                                print(" ")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                    if ans == 'n' or ans == 'N':

                                        continue
                    if seltype == '2':
                        ty_pe = ty_pes[1]
                        size_fitment = size_fitments[5]
                        comp = Component(ty_pe, size_fitment, serial_num='', status='')
                        print("This is an " + size_fitment + " for all aircraft.")
                        print(
                            "This batch contains " + str(
                                batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                        ans = input(">")
                        while ans not in answers:
                            print(
                                "This batch contains " + str(
                                    batch.comp_num)+ " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                            ans = input(">")
                        else:
                            if ans == 'y' or ans == 'Y':
                                pushbatch()

                                savedata(batch, batchdata, comp_num, data)
                                print("Batch and component records created at " + str(
                                    now.strftime("%H")) + ":" + str(
                                    now.strftime("%M")) + " on " + manufacturetime)
                                print("Would you print the batch details? Y/N")
                                ans2 = input(">")
                                while ans2 not in answers:
                                    print("Would you print the batch details? Y/N")
                                    ans2 = input(">")
                                else:

                                    if ans2 == 'y' or ans2 == 'Y':
                                        printoutbatch()
                                        anyb = input("Press any button to get the menu: ")
                                        if anyb:
                                            break

                                    if ans2 == 'n' or ans2 == 'N':
                                        print("ok")
                                        anyb = input("Press any button to get the menu: ")
                                        if anyb:
                                            break

                            if ans == 'n' or ans == 'N':
                                continue
                    if seltype == '3':
                        ty_pe = ty_pes[2]
                        size_fit2()

                        seltype2 = input(">")
                        while seltype2 not in choices2:
                            size_fit2()

                            seltype2 = input(">")
                        else:
                            if seltype2 == '1':
                                size_fitment = size_fitments[2]
                                comp = Component(ty_pe, size_fitment, serial_num='', status='')
                                print(
                                    "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                ans = input(">")
                                while ans not in answers:
                                    print(
                                        "This batch contains " + str(
                                            batch.comp_num)+ " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                    ans = input(">")
                                else:
                                    if ans == 'y' or ans == 'Y':
                                        pushbatch()

                                        savedata(batch, batchdata, comp_num, data)
                                        print("Batch and component records created at " + str(
                                            now.strftime("%H")) + ":" + str(
                                            now.strftime("%M")) + " on " + manufacturetime)
                                        print("Would you print the batch details? Y/N")
                                        ans2 = input(">")
                                        while ans2 not in answers:
                                            print("Would you print the batch details? Y/N")
                                            ans2 = input(">")
                                        else:

                                            if ans2 == 'y' or ans2 == 'Y':
                                                printoutbatch()
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                            if ans2 == 'n' or ans2 == 'N':
                                                print("ok")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                    if ans == 'n' or ans == 'N':
                                        continue
                            if seltype2 == '2':
                                size_fitment = size_fitments[3]
                                comp = Component(ty_pe, size_fitment, serial_num='', status='')
                                print(
                                    "This batch contains " + str(
                                        batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                ans = input(">")
                                while ans not in answers:
                                    print(
                                        "This batch contains " + str(
                                            batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                    ans = input(">")
                                else:
                                    if ans == 'y' or ans == 'Y':
                                        pushbatch()

                                        savedata(batch, batchdata, comp_num, data)
                                        print("Batch and component records created at " + str(
                                            now.strftime("%H")) + ":" + str(
                                            now.strftime("%M")) + " on " + manufacturetime)
                                        print("Would you print the batch details? Y/N")
                                        ans2 = input(">")
                                        while ans2 not in answers:
                                            print("Would you print the batch details? Y/N")
                                            ans2 = input(">")
                                        else:

                                            if ans2 == 'y' or ans2 == 'Y':
                                                printoutbatch()
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                            if ans2 == 'n' or ans2 == 'N':
                                                print("ok")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                    if ans == 'n' or ans == 'N':

                                        continue

                            if seltype2 == '3':
                                size_fitment = size_fitments[4]
                                comp = Component(ty_pe, size_fitment, serial_num='', status='')
                                print("This batch contains " + str(batch.comp_num) + " " + size_fitment +
                                      " " + ty_pe + " is this correct, Y/N?")

                                ans = input(">")
                                while ans not in answers:
                                    print("This batch contains " + str(batch.comp_num) + " " + size_fitment + " " + ty_pe + " is this correct, Y/N?")

                                    ans = input(">")
                                else:
                                    if ans == 'y' or ans == 'Y':
                                        pushbatch()

                                        savedata(batch, batchdata, comp_num, data)
                                        print("Batch and component records created at " + str(
                                            now.strftime("%H")) + ":" + str(
                                            now.strftime("%M")) + " on " + manufacturetime)
                                        print("Would you print the batch details? Y/N")
                                        ans2 = input(">")
                                        while ans2 not in answers:
                                            print("Would you print the batch details? Y/N")
                                            ans2 = input(">")
                                        else:

                                            if ans2 == 'y' or ans2 == 'Y':
                                                printoutbatch()
                                                print(" ")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                            if ans2 == 'n' or ans2 == 'N':
                                                print(" ")
                                                anyb = input("Press any button to get the menu: ")
                                                if anyb:
                                                    break

                                    if ans == 'n' or ans == 'N':

                                            continue

            break


#this a function to allocate location status to 'Factory Floor - Warehouse Not Allocated' for those batches which have not been allocated yet from previous step
def locationstatus():

    t = []
    path = '..\B00350882\Data\ '

    for filename in glob.glob(path + '*.pck'):
        # here im getting the pickle files from Data directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x

        if len(y) < 18:
            with open(path + y2, 'rb') as f:
                h = pickle.load(f)
            t.append(h)

    for batch in t:
        if len(batch) == 2:
            batch.append(location[0])

            with open('..\B00350882\Data\ '+batch[0] +'.pck', 'wb') as f:
                pickle.dump(batch, f)


#this is the function to list all previously created batches
def list_all_batches():
    print("List of all batches recorded in system:")
    print("Batch# \t \t \t \t Type  \t \t \t \t Size/fitment \t \t \t Quantity Made \t \t \t Location")
    t = []
    l = []
    ind = '0001'
    path = '..\B00350882\Data\ '

    for filename in glob.glob(path + '*.pck'):
        # here im getting the pickle files from Data directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x

        if len(y) < 18:
            with open(path + y2, 'rb') as f:
                h = pickle.load(f)
            t.append(h)
        if len(y) > 18 and ind in y.split("_")[1]:
            with open(path + y2, 'rb') as g:
                i = pickle.load(g)
            l.append(i)

    k = [x+y for x, y in zip(t, l)]

    for lista in k:

        if len(lista) == 8:
            if lista[4] == 'Winglet Struts' or lista[5] == '10mm x 75mm':
                print(lista[0] + '\t \t' + lista[4] + '\t \t \t' + lista[5] + '\t \t \t \t \t' + lista[1] + '\t \t \t \t \t' + lista[2])
            else:
                print(lista[0] + '\t \t' + lista[4] + '\t \t \t' + lista[5] + '\t \t \t \t' + lista[1] + '\t \t \t \t \t' + lista[2])
        if len(lista) == 7:
            lista.insert(2, location[0])
            if lista[4] == 'Winglet Struts' or lista[5] == '10mm x 75mm':
                print(lista[0] + '\t \t' + lista[4] + '\t \t \t' + lista[5] + '\t \t \t \t \t' + lista[1] + '\t \t \t \t \t' + lista[2])
            else:
                print(lista[0] + '\t \t' + lista[4] + '\t \t \t' + lista[5] + '\t \t \t \t' + lista[1] + '\t \t \t \t \t' + lista[2])

    print("End of list")
    print(" ")
    anyb = input("Press any button to get the menu")
    if anyb:
        return True

# function to view batch details
def viewbatchdetails():
    t = []
    batchlst = []
    batchlst2 = []
    numb = input("Enter batch number:")
    path = '..\B00350882\Data\ '
    for filename in glob.glob(path + '*.pck'):  # listing the pickle files in the directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x
        with open(path + y2, 'rb') as f:  # open the pickle files and put its content into the list "t"
            h = pickle.load(f)
        t.append(h)

    t2 = [item[0] for item in t] #"t2" is a list with all of the first element of the "t" list

    if numb in t2:#checking if numb input value is in the list

        g = [x for x in t2 if numb in x] #output all the elements which contains our batch number

        for i in g:
            k = i.replace("-","_") #i have replaced the characters otherwise the component number's files are not found and the "k"s are the batch and component numbers which contain our input number
            if len(k) < 13: # if length of it is less then 13 characters then that is batch pickled file
                with open("..\B00350882\Data\ "+ k +'.pck', 'rb') as f:
                    c = pickle.load(f)
                batchlst.append(c) #I put the content into a list called batchlst
            if len(k) > 13: # if length of it is higher then 13 characters then that is component pickled file
                with open("..\B00350882\Data\ "+ k +'.pck', 'rb') as f:
                    d = pickle.load(f)
                batchlst2.append(d) #I put the content into a list called batchlst2

        if len(batchlst[0]) == 2:
            print(len(batchlst[0]))

        snumbers = [item[0] for item in batchlst2]
        componentstatus = [item[0]+ ' ' + item[4] for item in batchlst2]
        # printing the details of a batch
        print("Batch Number: \t" + str(batchlst[0][0]))
        print("Location: \t" + str(batchlst[0][2]))
        print("Manufacture Date: \t" + str(batchlst2[0][3]))
        print("Component Type: \t" + str(batchlst2[0][1]))
        print("Component size/fitment type: \t" + str(batchlst2[0][2]))
        print("Number of components in batch: \t" + str(batchlst[0][1]))
        print("Serial numbers: \t" + str(snumbers))
        print("Component Status: \t" + '\n\t\t\t\t\t\t' + str("\n\t\t\t\t\t\t".join(componentstatus)))
        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True

    else:
        print("Batch not found")
        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True


#funtiont to view component details
def viewcomponentdetails():
    t = []
    batchlst = []
    numb = input("Enter component number:")

    path = '..\B00350882\Data\ '
    for filename in glob.glob(path + '*.pck'):  # listing the pickle files in the directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x
        with open(path + y2, 'rb') as f:  # open the pickle files and put its content into the list "t"
            h = pickle.load(f)
        t.append(h)

    t2 = [item[0] for item in t]  # "t2" is a list with all of the first element of the "t" list

    if numb in t2 and len(numb)==17:
        k = numb.replace("-", "_")
        with open("..\B00350882\Data\ " + k + '.pck', 'rb') as f:
            c = pickle.load(f)
        batchlst.append(c)

        batchnum = batchlst[0][0].split('-', 1)[0] #taking the part of the component number before the sign "-"
        #printing the details of a component
        print("Component details for: \t" + batchlst[0][0])
        print("Type: \t" + batchlst[0][1])
        print("Size/fitment type: \t" + batchlst[0][2])
        print("Date of manufacture: \t" + batchlst[0][3])
        print("Current status: \t" + batchlst[0][4])
        print("Part of batch: \t" + batchnum)
        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True
    else:
        print("Component not found")
        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True


#function to allocate manufactured stock
def allocatestock():
    t = []
    batchlst = []
    numb = input("Enter batch number:")
    path = '..\B00350882\Data\ '
    for filename in glob.glob(path + '*.pck'):  # listing the pickle files in the directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x
        with open(path + y2, 'rb') as f:  # open the pickle files and put its content into the list "t"
            h = pickle.load(f)
        t.append(h)

    t2 = [item[0] for item in t]  # "t2" is a list with all of the first element of the "t" list

    if numb in t2 and len(numb)<13:

        with open("..\B00350882\Data\ " + numb + '.pck', 'rb') as f:
            c = pickle.load(f)
        batchlst.append(c)

        if len(batchlst[0]) == 3:
            if batchlst[0][2] == location[0]:
                del batchlst[0][2]

                stocklocation()
                chooselocation = input("Enter the location's index: ")
                while chooselocation not in choices3:
                    print("Wrong choice.")
                    chooselocation = input("Enter the location's index: ")
                else:
                    k = numb.replace("-", "_")
                    if chooselocation == "1":

                        batchlst[0].append("Paisley")
                        print("This batch is now allocated to the " + batchlst[0][2] + " location")
                        with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                            pickle.dump(batchlst[0], f)
                    if chooselocation == "2":

                        batchlst[0].append("Dubai")
                        print("This batch is now allocated to the " + batchlst[0][2] + " location")
                        with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                            pickle.dump(batchlst[0], f)

            else:
                print("Batch already allocated")
                print(" ")
                anyb = input("Press any button to get the menu")
                if anyb:
                    return True
        if len(batchlst[0]) == 2:
            stocklocation()
            chooselocation = input("Enter the location's index: ")
            while chooselocation not in choices3:
                print("Wrong choice.")
                chooselocation = input("Enter the location's index: ")
            else:
                k = numb.replace("-", "_")
                if chooselocation == "1":
                    print("Paisley")
                    batchlst[0].append("Paisley")
                    with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                        pickle.dump(batchlst[0], f)
                if chooselocation == "2":
                    print("Dubai")
                    batchlst[0].append("Dubai")
                    with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                        pickle.dump(batchlst[0], f)

    else:
        print("Batch not found")
        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True



def long(size_fitment, ty_pe):
    print(
        "This batch contains " + size_fitment + " " + ty_pe + " is this correct, Y/N?")
    ans = input(">")
    while ans not in answers:
        print(
            "This batch contains " + size_fitment + ty_pe + " " + " is this correct, Y/N?")

        ans = input(">")
    else:
        if ans == 'y' or ans == 'Y':
            t = []
            t2 = []
            t3 = []
            unfinished = []
            finished = []
            path = '..\B00350882\Data\ '
            for filename in glob.glob(path + '*.pck'):  # listing the pickle files in the directory
                x = filename.split('Data\ ', 1)[1]
                y = ' ' + x
                y2 = x
                with open(path + y2, 'rb') as f:  # open the pickle files and put its content into the list "t"
                    h = pickle.load(f)
                t.append(h)
                t2.extend(h)
            if ty_pe not in t2 and size_fitment not in t2:

                print("No stock available!")
            else:
                for x in t:

                    with open(path + x[0].split('-')[0] + '.pck', 'rb') as f:
                        w = pickle.load(f)
                        v = x + w

                    if len(v) == 8:

                        t3.append(v)
                        if ty_pe in v and size_fitment in v and v[7] != "Factory Floor - Warehouse Not Allocated":

                            if x[4].split('-')[1] == " Unfinished":
                                unfinished.append(x)

                            if x[4].split('-')[1] != " Unfinished":
                                finished.append(x)

                if len(unfinished) == 0 and len(finished) == 0:
                    print("No stock available!")
                # print(t3)
                else:
                    print("Finished Products:")
                    print(
                        "Compponent serial number " + "\t\t\t\t" + "Location" + "\t\t\t\t" + "Finish" + "\t\t\t\t" + "Manufacture date")
                    for e in finished:
                        with open(path + e[0].split('-')[0] + '.pck', 'rb') as f:
                            h = pickle.load(f)
                        if h[2] != "Factory Floor - Warehouse Not Allocated":
                            print(e[0] + "\t\t\t\t\t\t" + h[2] + "\t\t\t\t\t" + e[4].split('- ')[1] + "\t\t\t" + e[3])
                    print(" ")
                    print("Unfinished Products:")
                    print(
                        "Compponent serial number " + "\t\t\t\t" + "Location" + "\t\t\t\t" + "Finish" + "\t\t\t\t" + "Manufacture date")

                    for r in unfinished:
                        with open(path + r[0].split('-')[0] + '.pck', 'rb') as f:
                            h = pickle.load(f)
                        if h[2] != "Factory Floor - Warehouse Not Allocated":
                            print(r[0] + "\t\t\t\t\t\t" + h[2] + "\t\t\t\t\t" + "Unfinished" + "\t\t\t" + r[3])

        print(" ")
        anyb = input("Press any button to get the menu")
        if anyb:
            return True


#function to search by product type
def searchbyproducttype():
    comptype()
    seltype = input(">")
    while seltype not in choices:
        comptype()
        seltype = input(">")
    else:
        if seltype == '1':
            ty_pe = ty_pes[0]
            size_fit1()
            seltype2 = input(">")
            while seltype2 not in choices3:
                size_fit1()

                seltype2 = input(">")
            else:
                if seltype2 == '1':
                    size_fitment = size_fitments[0]
                    long(size_fitment, ty_pe)

                if seltype2 == '2':
                    size_fitment = size_fitments[1]
                    long(size_fitment, ty_pe)

        if seltype == '2':
            ty_pe = ty_pes[1]
            size_fitment = size_fitments[5]
            long(size_fitment, ty_pe)

        if seltype == '3':
            ty_pe = ty_pes[2]
            size_fit2()

            seltype2 = input(">")
            while seltype2 not in choices2:

                size_fit2()
                seltype2 = input(">")

            else:
                if seltype2 == '1':
                    size_fitment = size_fitments[2]
                    long(size_fitment, ty_pe)

                if seltype2 == '2':
                    size_fitment = size_fitments[3]
                    long(size_fitment, ty_pe)

                if seltype2 == '3':
                    size_fitment = size_fitments[4]
                    long(size_fitment, ty_pe)


#function to allow letters and numbers in the string
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


#function to get a component finished
def finishcomponent():

    t = []
    batchlst = []
    batchlst2 = []
    numb = input("Enter serial number of the component to finish: ")

    path = '..\B00350882\Data\ '
    for filename in glob.glob(path + '*.pck'):  # listing the pickle files in the directory
        x = filename.split('Data\ ', 1)[1]
        y = ' ' + x
        y2 = x
        with open(path + y2, 'rb') as f:  # open the pickle files and put its content into the list "t"
            h = pickle.load(f)
        t.append(h)

    t2 = [item[0] for item in t]  # "t2" is a list with all of the first element of the "t" list

    if numb in t2 and len(numb) == 17:
        k = numb.replace("-", "_")
        with open("..\B00350882\Data\ " + k + '.pck', 'rb') as f:
            c = pickle.load(f)
        batchlst.append(c)
        m = batchlst[0][0].split('-')[0]

        with open(path + m + '.pck', 'rb') as f:
            g = pickle.load(f)
        batchlst2.append(g)

        if len(batchlst2[0]) == 3 and batchlst2[0][2] != "Factory Floor - Warehouse Not Allocated":
            print("You selected " + batchlst[0][2] + " " + batchlst[0][1] + " " + batchlst2[0][2] + " is this correct Y/N?")
            ans = input(">")
            while ans not in answers:
                print(
                    "You selected " + batchlst[0][2] + " " + batchlst[0][1] + " " + batchlst2[0][2] + " is this correct Y/N?")
                ans = input(">")
            if ans == 'Y' or ans == 'y':
                if batchlst[0][4] == "Manufactured - Unfinished":
                    del batchlst[0][4]
                    selectfinish()
                    ans = input(">")
                    while ans not in choices3:
                        print("Wrong choice")
                        selectfinish()
                        ans = input(">")
                    if ans == '1':
                        batchlst[0].append("Manufactured - Polished")

                        with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                            pickle.dump(batchlst[0], f)
                        print("Component number " + numb + " will be finished as polished")
                    if ans == '2':
                        paintcode = input("Enter 4 digits paint code: ")

                        while is_allowed_specific_char(paintcode) is False or len(paintcode) != 4:
                            print("Invalid paintcode")
                            paintcode = input("Please, enter a valid paint code: ")
                        else:
                            batchlst[0].append("Manufactured - Paint:" + paintcode.upper())
                            with open("..\B00350882\Data\ " + k + '.pck', 'wb') as f:
                                pickle.dump(batchlst[0], f)
                            print("Component number " + numb + " will be finished using Paint Code " + paintcode.upper())

                else:
                    print("Component is already finished")
                    return False
        else:
            print("Not in stock")
            return False
    else:
        print("Not a valid serial number")

    print(" ")
    anyb = input("Press any button to get the menu")
    if anyb:
        return True

print("Welcome to the PPEC inventory system")
print("---------------------------------")
print()
while True:
    # if BatchIndex.json file exists then read it otherwise create it
    if where_json("..\B00350882\Data\BatchIndex.json"):
        with open('..\B00350882\Data\BatchIndex.json', encoding='utf-8') as readfile:
            data = json.loads(readfile.read())

            t = data.get("batch")

            s = []

            for w in t:
                y = w.get("Batchnumber")
                s.append(y)

    else:
        with open("..\Data\BatchIndex.json", "w") as outfile:
            json.dump(data, outfile, indent=2)
            t = data.get("batch")

            s = []

            for w in t:
                y = w.get("Batchnumber")
                s.append(y)

    locationstatus()
    # Print out the menu:
    print(" ")
    menu()
    choice = input("Select a menu-point > ")
    #calling the right functions
    if choice == '1':
        createBatch()

    elif choice == '2':
        list_all_batches()

    elif choice == '3':
        viewbatchdetails()

    elif choice == '4':
        viewcomponentdetails()

    elif choice == '5':
        allocatestock()

    elif choice == '6':
        searchbyproducttype()

    elif choice == '7':
        finishcomponent()

    elif choice == '8':
        print("The program is finished.")
        print("Good Bye")
        break


