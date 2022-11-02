from concurrent.futures import BrokenExecutor
from logging import root
from tkinter import *
from tkinter import messagebox

#root window setup
rootWindow = Tk()
rootWindow.title("Basic Subnetting Tool")
iconInmage = PhotoImage(file="HarryICON1.png")
rootWindow.iconphoto(False, iconInmage)

#functions
def calculateSubnet():
    print("Pushed")

#object creation
inputFrame = LabelFrame(rootWindow, text= "IP Address", labelanchor=N,padx=5,pady=5)
ipInputOne = Entry(inputFrame,width=5)
ipInputTwo = Entry(inputFrame, width=5)
ipInputThree = Entry(inputFrame,width=5)
dotLabelOne = Label(inputFrame,text=".")
dotLabelTwo = Label(inputFrame,text=".")
slashLabel = Label(inputFrame,text="/")
cidrInput = Entry(inputFrame, width=3)

subnetButton = Button(rootWindow,text="SUBNET", command= calculateSubnet)

networkFrame = LabelFrame(rootWindow, text= "Network ID", labelanchor=N)
networkLabel = Label(networkFrame,text="")

firstHostFrame = LabelFrame(rootWindow,text="First Host", labelanchor=N)
firstLabel = Label(firstHostFrame, text="")

lastHostFrame = LabelFrame(rootWindow, text="Last Host", labelanchor=N)
lastLabel = Label(lastHostFrame, text="")

broadcastFrame = LabelFrame(rootWindow, text="Broadcast ID", labelanchor=N)
broadcastLabel = Label(broadcastFrame, text="")

#object display
inputFrame.grid(row=0, column=0, padx=5, pady=5)
ipInputOne.grid(row=0,column=0)
dotLabelOne.grid(row=0,column=1)
ipInputTwo.grid(row=0,column=2)
dotLabelTwo.grid(row=0,column=3)
ipInputThree.grid(row=0,column=4)
slashLabel.grid(row=0,column=5)
cidrInput.grid(row=0,column=6)

subnetButton.grid(row=0, column=1, padx=5)

networkFrame.grid(row=1,column=0,padx=5,pady=5, columnspan=2)
networkLabel.pack()

firstHostFrame.grid(row=2,column=0,padx=5,pady=5, columnspan=2)
firstLabel.pack()

lastHostFrame.grid(row=3,column=0,padx=5,pady=5, columnspan=2)
lastLabel.pack()

broadcastFrame.grid(row=4,column=0,padx=5,pady=5, columnspan=2)
broadcastLabel.pack()

rootWindow.mainloop()
