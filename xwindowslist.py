#!/usr/bin/python3
# x window list
import sys
import subprocess
import re

def main(args):
	data=idofwindows()
	nofw=len(data)
	for i in data:
		names=nameofid(i)
		print(names)
	#print("# of windows: {}".format(nofw))
	return nofw

def idofwindows():
	command = "xprop -root | grep '_NET_CLIENT_LIST_STACKING(WINDOW)'"
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print(out)
	print("gozdr")
	base, basedata = str(out).split("window id # ")
	print(base)
	print("elma")
	print(basedata)
	print("durmaz")
	basedata=basedata.split("\\n")
	data=basedata[0].split(", ")
	print(data)
	return(data)

def nameofid(id):
	global line1
	global line2
	command="xprop -id {} | grep '^WM_CLASS\|^WM_NAME'".format(id) #sdf
	
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	lines=str(out).split("\\n")
	print(lines)
	print("armut123")
	windows=[]

	if "WM_CLASS" in lines[0]:
		line2=re.findall('"([^"]*)"', lines[1] )
		line1=re.findall('"([^"]*)"', lines[0] )
	elif "WM_NAME" in lines[0]:
		line1=re.findall('"([^"]*)"', lines[1] )
		line2=re.findall('"([^"]*)"', lines[0] )
	windows.append(line1[1])
	windows.append(line2[0])
	return(windows)

if __name__ == '__main__':
    import sys, subprocess, re
    sys.exit(main(sys.argv))
