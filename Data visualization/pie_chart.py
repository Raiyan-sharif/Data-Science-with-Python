import matplotlib.pyplot as plt

labels='C#', 'C++', 'Java', 'C', 'Python'

# Portion for each label
size=[23,25,48,1,25]

# explode ration for each title
ex=(.02,0,0,0,0)

# Plotting the data
plt.pie(size,labels=labels,autopct='%1.1f%%',explode=ex)
plt.axis('equal')

plt.show()