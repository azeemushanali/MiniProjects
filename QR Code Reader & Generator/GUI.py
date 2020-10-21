# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:29:38 2020

@author: Azeemushan
"""

import tkinter as tk
from tkinter import Button, Entry, Label, Radiobutton,  StringVar , messagebox
import pyqrcode
from PIL import ImageTk,Image 
from barcode import Code128
from barcode.writer import ImageWriter



def createWidget():
    label = Label(text="CODE TEXT : ",bg="steelblue")
    label.grid(row=0,column=1,padx=5,pady=5)
    
    root.entry = Entry(width=30,textvariable=QrBarcodeInput)
    root.entry.grid(row=0,column=2,padx=5,pady=5,columnspan=2)

    button =Button(width=10,text="GENERATE",command=QrBarcodeGenerate)
    button.grid(row=0,column=4,padx=5,pady=5)

    label = Label(text="CODE TYPE : ",bg="steelblue")
    label.grid(row=1,column=1,padx=5,pady=5)
    
    qrRadio = Radiobutton(root,text="QRCode",variable=radioVaribale,value="qrcode",bg="steelblue")
    qrRadio.grid(row=1,column=2,padx=5,pady=5)

    bRadio = Radiobutton(root,text="BarCode",variable=radioVaribale,value="barcode",bg="steelblue")
    bRadio.grid(row=1,column=3,padx=5,pady=5)

    label = Label(text="CODE : ",bg="steelblue")
    label.grid(row=2,column=1,padx=5,pady=5) 

    root.imageLabel = Label(root,background="steelblue")
    root.imageLabel.grid(row=3,column=1,columnspan=4,padx=5,pady=5)

def QrBarcodeGenerate():
    #Storing user input text in a variable
    QrBarcodeString = QrBarcodeInput.get()
    # Storing the radio button selection 
    QrBarcodeSelection = radioVaribale.get()

    ##checking the radio button selectiion and generating the code as per the selection
    if QrBarcodeSelection == "qrcode" :
        if QrBarcodeString != "":
            QRCodePath = "OutputFiles/"
            QRCodeName = QRCodePath + QrBarcodeString + ".png"
            QrGenerate = pyqrcode.create(QrBarcodeString)
            QrGenerate.png(QRCodeName,scale= 10)
            image = Image.open(QRCodeName)
            image = image.resize((400,400),Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            root.imageLabel.config(image=image)
            root.imageLabel.photo = image
        else:
            messagebox.showerror("ERROR","Enter a Text first!")
    elif QrBarcodeSelection == "barcode" :
        if QrBarcodeString != '':
            BarcodePath = "OutputFiles/"
            BarcodeName = BarcodePath + QrBarcodeString + "-barcode"
            barcodeOutput = Code128(QrBarcodeString,writer=ImageWriter())
            barcodeOutput.save(BarcodeName)

            image = Image.open(BarcodeName+".png")
            image = image.resize((450,300),Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

            root.imageLabel.config(image=image)
            root.imageLabel.photo = image
        else:
            messagebox.showerror("ERROR","Enter a text first !!")

    print("Clicked")
    



#setting up the GUI UI
root = tk.Tk()
root.title("QRCode Generator")
root.geometry("510x530")
root.resizable(False,False)
root.config(background="steelblue")
#creating tkinter variable
QrBarcodeInput = StringVar()
radioVaribale = StringVar()
radioVaribale.set("qrcode")
createWidget()
root.mainloop()