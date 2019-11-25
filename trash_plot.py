labels=["Grim","Pride and Prejudice", "Copyright Law", "Paper Collection"]
x=[-0.155,-0.0799,-0.0196,0.0157]
y=[0.693276463299,0.6514742725,0.48534938222,0.339096470318]


#x=[-0.155,-0.0799,-0.06,-0.0196,0.0157]
#y=[0.693276463299,0.6514742725,0.842,0.48534938222,0.339096470318]



import matplotlib.pyplot as plt

plt.plot(x,y,"o-")

for i in range(len(labels)):
    plt.annotate(labels[i], (x[i],y[i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                  xytext=(0,3),
                 ha='center')

plt.xlabel("EH Index")
plt.ylabel("Percent of Common Words")
plt.show()
