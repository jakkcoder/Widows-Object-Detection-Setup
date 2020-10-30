
classnames_file = "images/class-names.txt"
protobuf_file = "images/labelmap.pbtxt"

file  = open(classnames_file,'r')
output_dict ={}
classname = file.readline().strip()
count=1
while len(classname) >0 :
    output_dict[classname] = count
    classname = file.readline().strip()
    count+=1
file.close()

outfile = open(protobuf_file,'w+')
outfile.truncate(0)
for i in output_dict.keys():   
    outfile.write("item {\n"+"  id:"+ str(output_dict[i]) + '\n'+'  name:'+"'" +str(i)+"'" +'\n'+ "}\n")
outfile.close() 
