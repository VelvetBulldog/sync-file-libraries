import win32file

def togglefileattribute(filename, fileattribute, value):
    #switches the file attribute to on or off based on the true or false value passed
    bitvector = win32file.GetFileAttributes(filename)
    if value:
        bitvector |= fileattribute
    else:
        bitvector &= ~fileattribute
    win32file.SetFileAttributes(filename, bitvector)

def fileattributecheck(filename, fileattr):
    #return the value of the file attribute
    attrvalue = win32file.GetFileAttributes(filename)
    is_archived = attrvalue & fileattr
    print(is_archived)
    return is_archived