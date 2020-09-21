import pickle
list_dict = {
    'RCB':['Virat Kohli',31],
    'CSK':['MS Dhoni',39],
    'MI':['Rohit Sharma',33],
    'SRH':['David Warner',33],
    'DC':['Shreyas Iyer',25],
    'RR':['Steven Smith',31],
    'KXIP':['KL Rahul',28],
    'KKR':['Dinesh Karthik',35]  
}

file_name="captains.pkl"

outfile = open(file_name,'wb')
pickle.dump(list_dict,outfile)
outfile.close()

infile = open(file_name,'rb')
loaded_list=pickle.load(infile)
loaded_list['sponsors'] = ['Dream 11','Tata Motors', 'PAYTM']
infile.close()

newfile = open(file_name,'wb')
pickle.dump(loaded_list,newfile)
newfile.close()

readfile = open(file_name,'rb')
newlist = pickle.load(readfile)
print(newlist)
