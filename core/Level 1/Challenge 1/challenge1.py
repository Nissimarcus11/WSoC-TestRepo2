import pickle
file=open('data.pkl','rb')
data=pickle.load(file)

for index in data:
    print(index)