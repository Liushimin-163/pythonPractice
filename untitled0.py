import pandas as pd
import numpy as np
from copy import deepcopy
df=pd.read_json('Contacts.json')

df=df.join(df[df['Email']!=''].groupby('Email')['Id'].apply(list),on='Email',rsuffix='EmailRelated')
#print(df[['Email','IdEmailRelated']].head(50))
df=df.join(df[df['OrderId']!=''].groupby('OrderId')['Id'].apply(list),on='OrderId',rsuffix='OrderIdRelated')
df=df.join(df[df['Phone']!=''].groupby('Phone')['Id'].apply(list),on='Phone',rsuffix='PhoneRelated')
df['IdEmailRelated'] = df['IdEmailRelated'].apply(lambda d: d if isinstance(d, list) else [])
df['IdPhoneRelated'] = df['IdPhoneRelated'].apply(lambda d: d if isinstance(d, list) else [])
df['IdOrderIdRelated'] = df['IdOrderIdRelated'].apply(lambda d: d if isinstance(d, list) else [])
df['Related'] = (df['IdEmailRelated'] + df['IdPhoneRelated'] + df['IdOrderIdRelated']).apply(set).apply(list)
def spilt_col(data, columns):
    for c in columns:
        new_col=data.pop(c)
        max_len=max(list(map(lambda x:len(x)if isinstance(x, list) else 1,new_col.values)))
        new_col=new_col.apply(lambda x:x+[None]*(max_len-len(x)) if isinstance(x, list)else[x]+[None]*(max_len-1))
        new_col=np.array(new_col.tolist()).T 
        for i,j in enumerate(new_col):
            data[c + str(i)]=j
      
spilt_col(df, columns=['Related'])
print(df[['Related0', 'Related1', 'Related2']].info())
        

df = df.set_index('Id')
id_ids_dict=df.to_dict()['Related']

id_contact_dict=df.to_dict()['Contacts']
id_ids_tmp_dict={}
while True:
    for key, value in id_ids_dict.items():
        for v in value:
            id_ids_dict[key]=sorted(list(set(id_ids_dict[key]+id_ids_dict[v])))
    if id_ids_tmp_dict== id_ids_dict:
        break
    else:
       id_ids_tem_dict=id_ids_dict.copy()
id_answer_dict={}
for key , value in id_ids_dict.items(): 
    contacts=0
    for k in values:
        contacts += id_contact_dict[k]
    id_answer_dict[key]='_'.join(list(map(str, value)))+ ','+str(contacts)   
df['ticket_trace/contact'] = df.index.map(id_answer_dict)
df = df.reset_index()
df = df.rename(columns={'Id': 'ticket_id'})
df.head()    
type 
#df['Related']=df['Related'].astype(str)
#print(df.head())
#data1=df.drop_duplicates(subset='Related', keep='first', inplace=False).astype(str)
#print(data1.info())
#data1['Related1']=[i for i in range(len(data1['Id']))]
#data1.drop(['Id','Email', 'Phone', 'Contacts', 'OrderId', 'IdEmailRelated', 'IdOrderIdRelated', 'IdPhoneRelated'],axis=1,inplace=True)
#print(data1.info())
#df=pd.merge(df, data1, how='left', on='Related').astype(str)
#df11=df.groupby('Related1')['Id'].apply(lambda x: x.astype(str).str.cat(sep='_')).reset_index()
#print(df.head(50))
#df12=df.groupby('Related1')['Contacts'].sum()
#df['ticket_Id']='_'.join(df['Related'])
#print(df.head(50))
#df.drop(['ticket_Id'],axis=1)
#df['ticket_Id']=df['Related'].apply(lambda _:str(_))
#df['ticket_Id']=df['Related'].str.get（'Related'[1：-1]）
#print(df.head(50))
#df.drop(['ticket_Id'],axis=1)
#df['ticket_Id'].str.replace(', ','_',case=False)
#df['ticket_Id']=pd.Series(df['ticket_Id'])
#print(df.head(50))
#df['ticket_Id'].str.replace(', ','_',case=False)
#print(df.head(50))

str1='   This is string example/   '
str2=str1.rstrip()
print(str2)

x=input('nihao:')
strs=x.split(' ')
s=list(map(int,strs))
if 1<=s[0] and s[0]<=2000 and 1<=s[1] and s[1]<=20:
    z=s[0]*s[1]
print(z)

z=(s[0]-s[1]*s[0]/100)*(1-s[2]/100)
print(round(z,2))

def countm(x,y):
x=input('stint: ')
a=' '.join(x.split())
print(a)
strs= a.rstrip().split(' ')
print(strs)
s=list(map(int,strs))
point=0
l=s[0]
for i in (s[2:]):
    if l < i and i > point*3:
        break
    elif i <= point*3:
         point-= s[s.index(i)-1]//3
         print(l,point)

    else:
        l-=i
        point += i//10
        print(l,point)
        
n=int(input('stint: '))
while 2<=n and n<=31:
     t=n-1
print(t)   
T=False
s=input()
strs={'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O':'0', 'S':'5', 'Z':'2'}
if 1<=len(s) and len(s)<=100:
    T= True
while T: 
    for i in range(len(s)):
        if s[i] in strs.keys():
           a=s.replace(s[i],strs[s[i]])
print(a)  


s=input('tt: ')
strs={'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O':'0', 'S':'5', 'Z':'2'}

a=s
if 1<=len(s) and len(s)<=100: 
    for i in range(len(s)):
        if a[i] in strs.keys():
           a=a.replace(a[i],strs[a[i]])
print(a)           
        
        
   
        
