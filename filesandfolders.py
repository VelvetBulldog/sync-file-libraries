import os, win32con, win32file, filecopy, attribs

#1. Go through a folder structure and identify the Archive folders                                                  Check
#2. Loop through the files in the archive folder, interrogate their archive bit and change it                       Check
#3. Copy the non-archived files one level up or into the Sales folder                                               Check
#4. Create variables for the top level source folder and top level destination                                      Check
#5. Determine how best to handle different files going to different folders Sales, Purchasing                       In Progress




# traverse root directory, and list directories as dirs and files as files
def folderwalk(toplevelsource, topleveldest):
    try:
        lz_directory = os.path.join(topleveldest, "LZ")
        os.mkdir(lz_directory)
    except FileExistsError:
        pass #if the directory already exists an exception will be raised but I'm happy for the program to continue
    for root, dirs, files in os.walk(toplevelsource):
        path = root.split(os.sep)
        if path[-1] == 'Archive':
            print(root)
            destination = str.replace(str.replace(str.replace(root,'\Archive',''),toplevelsource,topleveldest),'\\','\\\\') #remove Archive then add extra backslashes
            print(destination)
            for file in files:
                dirpath = os.path.join(root, file)
                print(dirpath) #print the file that is about to be worked on
                source = str.replace(dirpath,'\\','\\\\') #add the extra backslashes again
                if attribs.fileattributecheck(source, win32con.FILE_ATTRIBUTE_ARCHIVE):
                    filecopy.cpfile(source, destination, lz_directory, file) #copy file from source to destination
                    attribs.togglefileattribute(source, win32con.FILE_ATTRIBUTE_ARCHIVE, False) #turn the archive attribute off

folderwalk("C:\\Test","C:\\Test1")







