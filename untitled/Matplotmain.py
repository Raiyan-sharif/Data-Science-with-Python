import matplotlib.pyplot as plt
years = [1, 1000, 1500,1600,1700, 1750, 1800, 1850, 1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [200, 400, 450, 580, 682, 791, 1000, 1262, 1650, 2525, 2758, 3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735, 6127, 6520, 6930, 7349]
plt.plot(years,pops,color=(1.0,0.39,0.39))
plt.ylabel("Population in billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()