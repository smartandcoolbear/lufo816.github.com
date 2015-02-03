import os

i = 1
path = '.'
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path,file))==True:
		if file.find('jpg')>=0:
			os.rename(os.path.join(path,file),os.path.join(path,"{:0>2d}".format(i)+'.jpg'))
			i+=1