import matplotlib.pyplot as plt
import numpy as np

col_count=4

Navi=(15,24,17,25)
Cloud9=(5,29,16,15)
Alliance=(5,2,1,1)
Team_Empire=(15,9,6,5)

index=np.arange(col_count)

N=plt.bar(index,Navi,.2,alpha=.5,label='Navi')
C=plt.bar(index+.2,Cloud9,.2,alpha=.5,label='Cloud9')
A=plt.bar(index+.4,Alliance,.2,alpha=.5,label='Alliance')
TE=plt.bar(index+.6,Team_Empire,.2,alpha=.5,label='Team empire')

def createlabels(data):
    for item in data:
        height=item.get_height()
        plt.text(item.get_x() + item.get_width()/2,height+.02,"{}".format(height),ha='center',va='bottom')

createlabels(N)
createlabels(C)
createlabels(A)
createlabels(TE)

plt.xticks(index+.8/3,('2013','2014','2015','2016'))

plt.xlabel("Team Name",fontsize=12)
plt.ylabel("Money earned(Millions)",fontsize=12)
plt.title("Money earned throughout the years",fontsize=23)

plt.grid(True)

plt.legend()

plt.show()