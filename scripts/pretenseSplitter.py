#! /bin/python
import os, os.path
import errno

# parse the pretense compiled file.
allLines = []
with open("pretense_compiled.lua","r") as file:
	allLines = file.readlines()

	

# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')
    
writtenFilesInOrder = []
isStart = False
isEnd = False
linesForFile = []
fileName = ""	

# Go through all the lines we read, and split them up by file.
for line in allLines:

	# This is the start of a section, let's pull it out.
	if line.startswith("-----------------[[") and "]]-----------------" in line and "END" not in line:
		print(line)
		isStart = True;
		isEnd = False;
		line = line.replace("-----------------[[","")
		line = line.replace("]]-----------------","")
		fileName = "src/"+line.lstrip();
		print("FileName: ",fileName)
	elif line.startswith("-----------------[[") and "]]-----------------" in line and "END" in line:
		print(line, fileName)
		isEnd = True;
		isStart = False;
		if "/" in fileName:
			with safe_open_w(fileName.strip()) as outFile:
				outFile.writelines(linesForFile)
		else:
			with open(fileName.strip(),"w") as outFile:
				outFile.writelines(linesForFile)
		linesForFile = []
		writtenFilesInOrder.append(fileName)
		fileName = ""
		isStart = False		
	elif isStart and not isEnd:
		linesForFile.append(line)

print("writing order file")
with open("ORDER","w") as outFile:
	outFile.writelines(writtenFilesInOrder)
