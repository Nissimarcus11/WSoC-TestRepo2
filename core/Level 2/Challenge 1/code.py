import pickle
import matplotlib.pyplot as plt
file = open('Data.pkl','rb')
data=pickle.load(file)
key_list=[]
value_list=[]
for i in data:
    key_list.append(i)
    value_list.append(data[i])
plt.bar(key_list,value_list)
plt.show()
plt.pie(value_list,labels=key_list,autopct='%1.2f%%')
plt.show()