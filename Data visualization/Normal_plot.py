import matplotlib.pyplot as plt

years=[1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015]
population=[2.5,2.7,3.0,3.3,3.7,4.0,4.4,4.8,5.3,5.7,6.1,6.5,6.9,7.3]
Death=[1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8]

#plt.plot(years,population,'go-',label='Line 1',linewidth=2,color=(1,.1,.1))


lines=plt.plot(years,population,'--',label='Population')
plt.plot(years,Death,'go-',label="Death")
plt.grid(True)
plt.xlabel("Year",fontsize=23)
plt.ylabel("Population growth",fontsize=23)
plt.title("Population growth over years")
plt.legend()
plt.show()