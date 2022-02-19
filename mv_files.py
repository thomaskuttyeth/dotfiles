import os
import shutil

def move_files(src,dest,n):
	count = 0
	try:
		for filename in os.listdir(src):
			if count >n-1:
				break
			else:
				shutil.move(f'src/{filename}',dest)
				count +=1
	except:
		print('Some error has occured! Check the directories')
		


