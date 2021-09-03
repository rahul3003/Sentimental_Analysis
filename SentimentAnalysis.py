from tkinter import *
import requests
import json

def featch(d):
    dic=d[0]
    newdic = {}
    act_resp = ''
    for i,j in dic.items():
        if i == 'classifications':
            newdic = j[0]
            for i1,j1 in newdic.items():
                if i1 == 'tag_name':
                    act_resp = j1
                    return act_resp

def onClick():
    url = "https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/"
    api_key= "50e6840a120636e9c447530584b9e8ac65328b30"

    header = {"Authorization" : f"Token {api_key}"}
    #input_val=["its good","its bad","the product is average"]
    #for i in range(len(input_val)):
       # a=input_val[i]
    a=e.get()
    s=a.split(",")
    for i in s:
        data={"data":[i] }

        resp=requests.post(url,headers=header,json=data)
        d=resp.json()
        res=featch(d)

        if res=="Positive":  
            resLabel.config(text=f"Thank You, {i} is {res}  feedback", fg="Green")
            imagel.config(image=im)
            
        elif res=="Negative":
            Label2.config( text=f"Thank You, {i} is {res} feedback", fg="red")

        else:
            Label3.config(text=f"Thank you, {i} is {res} feedback", fg="gold")


root = Tk()
root.title("Sentimental Analysis")
root.geometry("800x350")
img=PhotoImage(file="image/1.png")
labelimage=Label(root,image=img)

mylabel=Label(root, text="Sentimental Analysis" ,bg="#007ebb",font=("Helvetica", 30),bd=1)
inlabel=Label(root, text="Enter your Feedback: ",bg="#007ebb",font=("Helvetica", 20),bd=1)
e=Entry(root)
myButton=Button(root, text="Get Analysis",width=20,bg="lightblue", command=onClick)
resLabel=Label(root, text="",bg="#007ebb",font=("Helvetica", 30))
Label2=Label(root, text="" ,bg="#007ebb",font=("Helvetica", 30))
Label3=Label(root, text="",bg="#007ebb" ,font=("Helvetica", 30))
            
labelimage.place(x=1,y=0)
mylabel.grid(row=0,column=0,padx=40,pady=30)
inlabel.grid(row=1,column=0,padx=20)
e.grid(row=2,column=0,pady=30,ipadx=80,ipady=30)
myButton.grid(row=2,column=1,padx=10,pady=10)
resLabel.grid(row=3,column=0,padx=5,pady=10)
Label2.grid(row=4,column=0,padx=10,pady=10)
Label3.grid(row=5,column=0,padx=10,pady=10)

im=PhotoImage(file="image/2.png")
imagel=Label(root)
imagel.grid(row=3,column=1)
root.mainloop()

