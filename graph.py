from matplotlib import pyplot as plt

def graph(x,y,n):

    gen = [i+1 for i in range(n//25)]

    plt.plot(gen, x, label = "Deterministic")
    plt.plot(gen, y, label = "Non-Deterministic")
    
    plt.xlabel('Generations')
    plt.ylabel('Varaince')
    plt.title('Variance VS Generation')
    
    plt.legend()
    plt.show()
