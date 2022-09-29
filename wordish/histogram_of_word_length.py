import matplotlib.pyplot as plt

x=[1,5,12,22,21,33,32,47,96,8,8,4,66,8,90,100]

plt.hist(x, 2)

plt.xlabel ("age")
plt.ylabel("count")
plt.title("Population Age Count")

#plt.show()

lista=["hej", "då", "elak", "snäll", "varför", "bibliotek", "åsna", "penna", "hypernervokustiskadiafragmakontravibrationer", "bil", "volvo", "jag", "heter", "Lucas", "och", "jobbar", "med", "Samuel", "som", "jobbar", "med", "Lucas" ]
ny_lista=[]
def count_word_length():
    for ord in lista:
        length=len(ord)
        ny_lista.append(length)
    print (ny_lista)
    return ny_lista
