import os
def get_parent_path():
    # getting the parent directory 
	cwd = os.getcwd()
	parent_dir = os.path.abspath(os.path.join(cwd,os.pardir))
	return parent_dir

def is_monotonic(ar):
    # whether an array is monotonic_increasing or not 
    for j in range(len(ar)-1):
        if ar[j]>ar[j+1]:
            return False
    else:
        return True
def unordered_counter(ar1):
    # how many elements are unorderd in an array
    counter = 0
    order = is_monotonic(ar1)
    while not order:
        for i in range(len(ar1)):
            if i<len(ar1)-1 and ar1[i]>ar1[i+1]:
                counter+=1
                ar1[i+1],ar1[i] = ar1[i],ar1[i+1]
                print(ar1)
                break
            order = is_monotonic(ar1)
    else:
        return counter
        