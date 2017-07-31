#!/usr/bin/python2.7
# -*-coding:Latin-1

#L2 FDV - Projet Ingénierie 2016/2017 - ECG wireless
#Nina Guérin - Julien Pichon - Simon Fradet 

#Ce programme en python fonctionne avec la bibliothèque matplotlib. Il permet de tracer un électrocardiogramme en direct avec les données acquise en wifi grâce à l'ECG wireless et de stockés ces données dans un fichier nommé data.csv.

#Importation des librairies nécéssaires à l'éxécution du programme
import sys
from socket import *
import random
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker #module permettant de modifier les axes



data = open("data.csv", "w")

#Tant qu'on n'arrête pas le programme, les valeurs renvoyés par le port série sont 1) enregistrées dans  un fichier nommé data.csv, et une ligne est sauté entre chaque valeur et 2) 
plt.ion()
i = 0
x=list()
y=list()
fig, ax = plt.subplots()

def main(threadname,q):
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2390))

    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        data.write("b'")
        data.write(str(message))
        data.write("'\n")
        print(message)
        p = message
        print(i)
        print(p)
        global i
        i += 0.01
        x.append(i)
        y.append(p)
        #plt.scatter(i, p)
        plt.plot(x, y)
        # Be sure to only pick integer tick locations.
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_locator(ticker.MaxNLocator(integer=True))
        ax.margins(0.05)
        ax.axis('tight')
        fig.tight_layout()
        plt.pause(0.0001)
        plt.show()
      
if __name__ == '__main__':
    sys.exit(main(0,0))
