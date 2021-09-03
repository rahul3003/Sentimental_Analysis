from tkinter import *
import requests
import json

#getting particular tag name
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
    data={"data":[e.get()] }
    #post request to monkey learn api
    resp=requests.post(url,headers=header,json=data)
    d=resp.json()
    res=featch(d)

    #classifying Sentimental and showing result
    if res=="Positive":  
        resLabel.config(text=f"Thank You, for {res}  feedback", fg="Green")
        imagel.config(image=im)
            
    elif res=="Negative":
        resLabel.config( text=f"Thank You,  {res} feedback", fg="red")

    else:
        resLabel.config(text=f"Thank you, for {res} feedback", fg="gold")

#using TKinter designed interface
root = Tk()
root.title("Sentimental Analysis")
root.geometry("800x350")
img=PhotoImage(file="image/1.png")
labelimage=Label(root,image=img)

mylabel=Label(root, text="Sentimental Analysis" ,bg="#007ebb",font=("Helvetica", 30),bd=1)
mylabel.grid(row=0,column=0,padx=40,pady=30)

inlabel=Label(root, text="Enter your Feedback: ",bg="#007ebb",font=("Helvetica", 20),bd=1)
inlabel.grid(row=1,column=0,padx=20)

e=Entry(root)
e.grid(row=2,column=0,pady=30,ipadx=80,ipady=30)

myButton=Button(root, text="Get Analysis",width=20,bg="lightblue", command=onClick)
myButton.grid(row=2,column=2,padx=10,pady=15,ipady=10)

resLabel=Label(root, text="",bg="#007ebb",font=("Helvetica", 30))
resLabel.grid(row=3,column=0,padx=5,pady=10)

labelimage.place(x=1,y=0)

im=PhotoImage(file="image/2.png")
imagel=Label(root)
imagel.grid(row=3,column=1)

root.mainloop()

