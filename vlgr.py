import demo
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
root = Tk()
root.title('车牌识别')
root.geometry('1088x685')

f1 = Frame(root)
f1.place(x=0,y=0)
f2 = Frame(root)
f2.place(y=340)
#changesize
def re_size(w,h):
    ratio = 300/h
    w_re = int(w * ratio)
    h_re = int(h * ratio)
    return (w_re,h_re)
#choice img
def file_select():
    global img_path,photo
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    s = img.size
    re_s = img.resize(re_size(s[0], s[1]))  # set size 
    photo = ImageTk.PhotoImage(re_s)
    t1.configure(image=photo)


b1 = Button(f1,text='选择文件',font=14,background='lightblue',fg='white',command=file_select)
b1.pack(anchor='nw')
t1 = Label(f1)
t1.pack(side='left')


#working

def recognition():
    n = demo.vlgr_res(img_path)
    print(n)
    t2.delete(1.0, 'end')
    for pstr,confidence,rest in n:
        t2.insert(1.0,pstr+'         准确度：'+'%.2f%%' %(confidence*100)+'\n','tag_1')
    demo.Vlgr(img_path)

b2 = Button(f2,text='车牌识别',font=14,background='lightblue',fg='white',command=recognition)
b2.pack(anchor='nw')
l1 = Label(f2,text='识别的车牌为：',font=14,width=90,height=2,background='lightgreen')
l1.pack()
t2 = Text(f2,width=90,height=10,font=14,background='lightblue',borderwidth=2,relief='flat')
t2.pack()

t2.tag_config("tag_1",justify='center')

root.mainloop()
