import matplotlib.pyplot as plt
import pandas as pd

# Data to be used
data={
        'Name': ['Nick','Reyes','Hamono','Julia','Hussain'],
        'Salary': [80000,56000,100000,60000,25000],
        'Jobs_done_jan': [2,4,1,4,5],
        'Jobs_done_feb': [1,2,3,4,1],
        'Jobs_done_mar': [3,2,1,4,2]
     }

# Formatting the data properly
df=pd.DataFrame(data,columns=['Name','Salary','Jobs_done_jan','Jobs_done_feb','Jobs_done_mar'])

# Creating a column called Total
df['Total']=df['Jobs_done_jan']+df['Jobs_done_feb']+df['Jobs_done_mar']
print(df)

# Plot the data
plt.pie(df['Total'],labels=df['Name'],autopct='%1.1f%%')
plt.axis('equal')
plt.show()