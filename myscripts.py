
# getting the parent directory 
import os
def get_parent_path():
	cwd = os.getcwd()
	parent_dir = os.path.abspath(os.path.join(cwd,os.pardir))
	return parent_dir


