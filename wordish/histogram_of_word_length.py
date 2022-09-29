import matplotlib.pyplot as plt

lista=["hej", "då", "elak", "snäll", "varför", \
                              "bibliotek", "åsna", "penna"]
ny_lista=[]
def count_word_length(lista):
    for ord in lista:
        length=len(ord)
        ny_lista.append(length)
    return ny_lista




def draw_histogram(värden):
    x = värden

    plt.hist(x)

    plt.xlabel("age")
    plt.ylabel("count")
    plt.title("Population Age Count")

    plt.show()

#draw_histogram(count_word_length(lista))




