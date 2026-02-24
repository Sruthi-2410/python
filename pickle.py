import pickle
f=open("pickledemo.txt","wb")
data={1:"one",2:"two"}
pickle.dump(data,f)
f.close()