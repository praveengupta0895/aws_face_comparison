from tkinter import *
from tkinter import filedialog
import boto3
from ctypes import *
from tkinter import messagebox

from tkinter import messagebox





def donothing():
    messagebox.showinfo("Info","Select second picture:")
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    c = root.filename
    return c






root = Tk()
def copyPath():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    a = root.filename
    return a
def hello():
    messagebox.showinfo("Hello")

def compare():
    sourceFile = copyPath()
    targetFile = donothing()
    messagebox.showinfo("compare","Click Ok to compare")
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})
    for record in response['FaceMatches']:
        face = record
        confidence = face['Face']


       # print("With {}""%"" Confidence".format(confidence['Confidence']))

        c = float(format(face['Similarity']))


        if (c > 95):
            messagebox.showinfo("Matched","Similarity "+format(face['Similarity'])+" With "+format(confidence['Confidence'])+" Confidence" )
        else:
            messagebox.showinfo("Not Matched",
                                "Similarity " + format(face['Similarity']) + " With " + format(confidence['Confidence'])+" Confidence")

    imageSource.close()
    imageTarget.close()







b3 = Button(root,text="Select two pictures and compare",command=compare,bg="thistle2")

b3.pack(side=LEFT,padx=90)

frame = Frame(root, width=10, height=100)
frame.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=hello)
helpmenu.add_command(label="About...", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.configure(background='sky blue')
root.mainloop()