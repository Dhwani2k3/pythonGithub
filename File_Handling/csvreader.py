data="test.csv"
rows=[]
list1=[]
def read_csv(data):
    f=open(data,"r")
    data=f.read()
    rows=data.split('\n')
    
    for i in range(0,len(rows)):
        list1=rows[i]
        rows[i]=list1.split(",")
    print(rows,"\n")
    f.close()
    dr=rows
    return rows

receivedata=read_csv(data)
#print(receivedata,"\n")
