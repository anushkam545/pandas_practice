import pandas as pd
df= pd.read_csv(r"C:\Users\This PC\Downloads\Ecommerce Purchases")

# 1. check first 10 rows
print(df.head(10))

# 2. check last 10 rows
print(df.tail(10))

# 3. check datatype of each column
print(df.dtypes)

# 4. check null values
print(df.isnull().sum())

# 5. how many rows and columns
print(df.columns)
print(len(df.columns))
print(len(df))

# 6. highest and lowest purchase price
print(df['Purchase Price'].max())
print(df['Purchase Price'].min())

# 7. average purchase price
print(df['Purchase Price'].mean())

# 8. how many people have french 'fr' as their language?
data=df[df['Language']=='fr']
print(len(data))

# 9. job tile contains engineer
title=df[df['Job'].str.contains('engineer',case=False)]
print(len(title))

# 10. find the email of the person with the following IP address : 132.207.160.22
IP_address=df[df['IP Address']=='132.207.160.22']['Email']
print(IP_address)

# 11. how many people have mastercard as their credit card provider and made a purchase above 50
people=df[(df['CC Provider']=='Mastercard') & (df['Purchase Price']>50)]
print(len(people))

# 12. find the email of the person with the following credit card no.: 4664825258997302
email=df[df['Credit Card']==4664825258997302] ['Email']
print(email)

# 13. how many people purchase during the AM and PM.
print(df['AM or PM'].value_counts())

# 14. how many people have CC that expires in 2020
print(df['CC Exp Date'])
def fun():
    count=0
    for date in df['CC Exp Date']:
        if date[3:]=='20':
            count+=1
    print(count)
print(fun())   

# 15. top 5 most popular email providers
list1=[]
for email in df['Email']:
    list1.append(email.split('@')[1])
df['temp1']=list1
print(df['temp1'].value_counts().head())