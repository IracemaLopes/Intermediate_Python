#we are trying to get an insight evolution of the world poluplation
import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
#number of population is in expressed in billions of how many people lived on earth
population=[2.519,3.692,5.263,6.972]
#we are printing the plot
plt.plot(year,population)
plt.show()

#we are printing scatter plot
plt.scatter(year,population)
plt.show()