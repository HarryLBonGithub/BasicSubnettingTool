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

    #check if the input is good
    if entryIsInvalid():
        messagebox.showerror(title="BAD INPUT", message="Input valid IP Address")
        ipInputOne.delete(0,END)
        ipInputTwo.delete(0,END)
        ipInputThree.delete(0,END)
        ipInputFour.delete(0,END)
        cidrInput.delete(0,END)
        return

    #grabbing user input and converting it to binary strings
    octOneBinaryString = generateOctet(ipInputOne.get())
    octTwoBinaryString = generateOctet(ipInputTwo.get())
    octThreeBinaryString = generateOctet(ipInputThree.get())
    octFourBinaryString = generateOctet(ipInputFour.get())

    addressBinaryString = octOneBinaryString + octTwoBinaryString + octThreeBinaryString + octFourBinaryString

    #creating the network mask as a binary string. this is only used in testing
    netMaskBinaryString = ""
    for _ in range(int(cidrInput.get())):
        netMaskBinaryString = netMaskBinaryString + "1"
    
    netMaskBinaryString = fillZeros(netMaskBinaryString)
    
    #creating the network ID first as a binary string then as a dot notation string
    networkIDBinary = fillZeros(addressBinaryString[0:int(cidrInput.get())])
    networkIDDotNote = binaryToDotNote(networkIDBinary)

    networkLabel.config(text = networkIDDotNote)

    #creating the broadcast ID first as a binary string then as a dot notation string
    broadcastBinaryString = fillOnes(addressBinaryString[0:int(cidrInput.get())])
    broadcastDotNote = binaryToDotNote(broadcastBinaryString)

    broadcastLabel.config(text = broadcastDotNote)

    #creating the first host in binary then as dot notation
    firstHostBinary = fillLeadingZeros(str(bin(int(networkIDBinary, 2) + 1))[2:])
    firstHostDotNote = binaryToDotNote(firstHostBinary)

    firstLabel.config(text=firstHostDotNote)

    #creating the last host in binary then as dot notation
    lastHostBinary = fillLeadingZeros(str(bin(int(broadcastBinaryString, 2) - 1))[2:])
    lastHostDotNote = binaryToDotNote(lastHostBinary)

    lastLabel.config(text=lastHostDotNote)

def generateOctet(segment):
    octet = str(bin(int(segment))[2:])
    while len(octet) < 8:
        octet = "0"+ octet
    return octet

def fillZeros(segment):

    addressString = segment

    while len(addressString) <32:
        addressString = addressString + "0"
    return addressString

def fillLeadingZeros(segment):

    addressString = segment

    while len(addressString) <32:
        addressString = "0" + addressString
    return addressString

def fillOnes(segment):

    addressString = segment

    while len(addressString) <32:
        addressString = addressString + "1"
    return addressString

def binaryToDotNote(segment):
    address = str(int(segment[0:8],2)) + "." + str(int(segment[8:16],2)) + "." + str(int(segment[16:24],2)) + "." + str(int(segment[24:32],2))
    return address

def entryIsInvalid():
    if ipInputOne.get().isnumeric() == False or int(ipInputOne.get()) < 0 or int(ipInputOne.get()) > 255:
        return True
    if ipInputTwo.get().isnumeric() == False or int(ipInputTwo.get()) < 0 or int(ipInputTwo.get()) > 255:
        return True
    if ipInputThree.get().isnumeric() == False or int(ipInputThree.get()) < 0 or int(ipInputThree.get()) > 255:
        return True
    if ipInputFour.get().isnumeric() == False or int(ipInputFour.get()) < 0 or int(ipInputFour.get()) > 255:
        return True
    if cidrInput.get().isnumeric() == False or int(cidrInput.get()) < 0 or int(cidrInput.get()) > 32:
        return True

#object creation
inputFrame = LabelFrame(rootWindow, text= "IP Address", labelanchor=N,padx=5,pady=5)
ipInputOne = Entry(inputFrame,width=5)
ipInputTwo = Entry(inputFrame, width=5)
ipInputThree = Entry(inputFrame,width=5)
ipInputFour = Entry(inputFrame,width=5)
dotLabelOne = Label(inputFrame,text=".")
dotLabelTwo = Label(inputFrame,text=".")
dotLabelThree = Label(inputFrame,text=".")
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
dotLabelThree.grid(row=0,column=5)
ipInputFour.grid(row=0, column=6)
slashLabel.grid(row=0,column=7)
cidrInput.grid(row=0,column=8)

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
