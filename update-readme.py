import os
import urllib.parse

FOLDER_ICON = ':file_folder:'
PAGE_ICON = ':page_with_curl:'
TAB_CHAR = '&emsp;'

ignoreDirs = ['.git','diagrams', 'images', '.github']


def processSubFolders(path,depth):
    tabstr = ''
    for i in range(0,depth):
        tabstr += TAB_CHAR

    (_,dirs,files) = os.walk(path).__next__()
    dirs.sort(reverse=False)
    files.sort(reverse=False)
    for dir in dirs:
        childPath = path + '/' + dir
        line = '{s0} {s1} [{s2}]({s3})'.format(
            s0= tabstr,
            s1 = FOLDER_ICON,
            s2 = dir,
            s3= childPath
        )
        writeInMdFile(line=line)
        processSubFolders(path= childPath,depth=depth+1)

    for file in files:
        childPath = path + '/' + file
        line = '{s0} {s1} [{s2}]({s3})'.format(
            s0= tabstr,
            s1 = PAGE_ICON,
            s2 = file,
            s3= childPath
        )
        writeInMdFile(line=line)
       
def writeMdHeading():
    with open('README.md', 'w') as f:
        f.write('# Folder Structure' + '  \n')
        f.close()

def writeInMdFile(line):
    with open('README.md', 'a') as f:
        f.write(line + '  \n')
        f.close()

def main():
    ## add heading to readme files 
    writeMdHeading()

    (root, dirs, files) = os.walk('./',).__next__()
    dirs.sort(reverse=False)
    files.sort(reverse=False)

    # recursively add folders 
    for dir in dirs:
        if dir in ignoreDirs:
            continue
        childPath = './' + dir    
        line = '{s1} [{s2}]({s3})'.format(s1=FOLDER_ICON, s2= dir, s3 = childPath)
        writeInMdFile(line)
        processSubFolders(path=childPath,depth=1)

    # add files 
    for file in files:
        childPath = './' + file
        line = '{s1} [{s2}]({s3})'.format(
            s1 = PAGE_ICON,
            s2 = file,
            s3= childPath
        )
        writeInMdFile(line=line)

if __name__=="__main__":
    main()

