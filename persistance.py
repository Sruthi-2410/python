''' persistance storage on harddrive
-its means storing permenantly

'''
import marshal
f=open("marshaldb","rb")
'''data={1:"mahenr",2:"udutala"}
marshal.dump(data,f)'''
print(marshal.load(f))
f.close()