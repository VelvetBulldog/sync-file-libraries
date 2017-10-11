#copy files from source directory to destination directory and trim X characters from the front

#C:\Test\Z1\Archive\2017-09-13 01.01.58.0190_sales_Z1_sales_d.txt
import shutil, os, attribs, win32con

def renamefile(originalfilename):
    firstunderline = originalfilename.find('_') + 1
    positionsecondunderline = originalfilename.find('_',firstunderline) + 1

    finalfilename = originalfilename[positionsecondunderline:]
    return finalfilename


def cpfile(source, destination, lz_directory, filename):

    shutil.copy(source, lz_directory) #copy to LZ for renaming

    lz_file = os.path.join(lz_directory, filename)
    new_filename = renamefile(filename)
    new_lz_file_name = os.path.join(lz_directory, new_filename)
    new_dst_file_name = os.path.join(destination, new_filename)
    os.rename(lz_file, new_lz_file_name)



    try:
        shutil.copy(new_lz_file_name, destination)#copy from LZ to destination hopefully will overwrite if file already exists
    except PermissionError:
        #if file already exists turn off the Readonly file attribute and try again
        attribs.togglefileattribute(new_dst_file_name, win32con.FILE_ATTRIBUTE_READONLY, False)
        shutil.copy(new_lz_file_name, destination)
    attribs.togglefileattribute(new_lz_file_name, win32con.FILE_ATTRIBUTE_READONLY, False)
    os.remove(new_lz_file_name)#delete file from the LZ once it has successfully been copied across


#filecopy('C:\\Test\\Z1\\Archive\\2017-09-13 01.01.58.0190_sales_Z1_sales_d.txt', 'C:\\Test\\Z1\\Sales')