import sys
import os
path = sys.argv[1]
print path
start = int(sys.argv[2])
for file in os.listdir(path):
	name = file[0:file.rindex('.')]
	extension = file[file.rindex('.'):]
	command = 'mv' + ' \'' + path + file + '\' ' + path + str(start) + extension
	print command
	os.system(command )
	start += 1


