#Gets user inputted name, address and phone
#Saves info to txt file data is comma delimited
#reads saved comma delimited txt files for data validataion

#libraries
import os



#variables

path = '' #stores user inputed path
infolist = [] #stores information to be pushed to file or is freshly read from file
writemode = 'x' #set to 'x' as default for safety - set to 'w' to force run and overwrite files
fields = ["Name: ","Address: ","Phone Number: "] #expandable
menuloop = 9


#functions

def checkdir(): #verifies path exists and changes working dir to user input path
    ispath = False #initialize
    global path #get path var 
    
    while(ispath!=True): #loop until path is valid
        path=str(input("enter directory: "))
        ispath = os.path.isdir(path) #check path
        if(ispath!=True):
            print("'"+path+"' is not a valid directory")
    os.chdir(path) #change cwd to set path

def getinfo(): #sets user info to infolist
    global infolist #gets infolist
    global fields
    infolist.clear() #clears infolist for new data
    for x in fields: #iterates through all input fields 
        infolist.append(str(input("input " + x)))

def writetofile(): #writes data from infolist to file
    global infolist
    global writemode
    with open((infolist[0] + '.txt'), writemode) as f:
        f.write(",".join(infolist))
        f.close()
    infolist.clear() #clears infolist now that done with data

def readfile():
    filename = "" #initialize
    loopvar = 0
    global infolist
    global fields
    
    print("files in directory: ",os.listdir(path)) #lists files in cwd
    filename = str(input("input filename: "))
    
    if(os.path.exists(filename)!=True): #if file does not exist tell user
        print("file does not exist")
    else: #if file exists read file
        with open((filename), 'r') as f:
            for line in f:
                infolist = line.split(',') #dump data to infolist
        for x in fields:
            print(x+infolist[loopvar])
            loopvar = loopvar + 1
        infolist.clear() #clears infolist now that done with data



#body

checkdir() #immediately set directory

while(menuloop!=0):
    menuloop = int(input("Enter '1' to write a new file\nEnter '2' to read a file\nEnter '3' to change directories\n"))
    if(menuloop==1):
        getinfo() #getinfo leaves infolist populated for potential expansion / future use 
        writetofile() #call immediately after getinfo
    elif(menuloop==2):
        readfile()
    elif(menuloop==3):
        checkdir()
