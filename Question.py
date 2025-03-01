from tkinter import filedialog
file_path = filedialog.askopenfilename(title="Select File")
file=open(file_path,'r')
l=file.read().split('\n')
nl=[]
for i in l:
    nl.append(i.split(","))
print("{")
c=0
for i in nl:
    if float(i[2])>float(7.8):
        print(str(c)+':'+'{'+'\n'+"name:"+str(i[0])+'\n'+"age:"+str(i[1])+'\n'+"grade:"+str(i[2])+'\n'+'}')
    c=c+1
print("}")


"""
test.txt
chandu,21,9.9
kamal,22,7.9
yogi,24,8.9
sidhu,26,2.7

"""


#o/p
'''
{
0:{
name:chandu
age:21
grade:9.9
}
1:{
name:kamal
age:22
grade:7.9
}
2:{
name:yogi
age:24
grade:8.9
}
}
'''


