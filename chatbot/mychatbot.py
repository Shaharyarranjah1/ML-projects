from tkinter import *
import tkinter as ttk
import random
from tkinter import Tk

# lets make a chatbot
class chatbot:
   def __init__(self, root):
      self.root= root
      self.root.geometry('700x600+250+10')
      self.root.title('My ChatGPT')
      self.root.bind('<Return>',self.entfun)

      # =====Title ====== ##
      lbl_title = Label(self.root, text='ChatGPT develop SHAHARYAR',font=('times new roman',20, 'bold'))
      lbl_title.place(x=130,y=10)

      #####---- Main frame scroll bar and text area  green
      main_frame = Frame(self.root, bd=4,relief=RAISED, bg='black')
      main_frame.place(x=0,y=60, width=700 ,height=400)

      ### ---> Text area with scroll bar <---- ###
      self.scroll_y = ttk.Scrollbar(main_frame,orient='vertical')
      
      self.text = Text(main_frame, width=65,height=20, font=('arial',14), relief=RAISED,yscrollcommand= self.scroll_y.set)
      self.scroll_y.pack(side=RIGHT,fill=Y)
      self.text.pack()

      ### Search Label #####
      lbl_search= Label(self.root,text='Search Here',font=('times new roman ',20,'bold'))
      lbl_search.place(x=20,y=470)

      ### -----> Entry area <---- ###
      self.ent = StringVar()
      self.entry= ttk.Entry(self.root ,textvariable= self.ent ,font=('times new roman',15,'bold'))
      self.entry.place(x=200,y=470, width=400,height=35)

      ###  Send button and clear button ####
      ## btn save
      self.btn= ttk.Button(self.root,command=self.send ,width=20,text='Send', font=('times new roman',14,'bold'), bg='black',fg='white')
      self.btn.place(x=200,y=520,width=200,height=30)

      ## clear btn
      self.btn_clr= ttk.Button(self.root,command=self.clear, width=20,text='Clear',font=('times new roman',14,'bold'), bg='black',fg='white')
      self.btn_clr.place(x=410,y=520,width=200,height=30)



## Backend functions ###
   def entfun(self,syr):
      self.btn.invoke()
      self.ent.set("")

   def clear(self):
      self.text.delete("1.0",END)
      self.ent.set("")

   def send(self):
     user_input = "\t\t\t"+"You :"+self.entry.get()
     self.text.insert(END,"\n\n"+user_input)
     input_list =['Hi','Hey','Helo','How are you?','Whats up?']
     output_list = ['Helo','Good to see you!','Nice to meet you!','Hi']
     for mess in input_list:
        if self.entry.get() == mess:
           ans = random.choice(output_list)
           self.text.insert(END,'\n\n','chatbot :', ans)

     rechest_persons = "Top 3 Richest persons in the world are , \n 1 Elon Musk \n 2 Jeff Bezoz \n 3 Bill Gates"
     if self.entry.get() == "richest person" or self.entry.get() == "top rechest person":
        self.text.insert(END, '\n\n'+'Bot :' + rechest_persons)





# ====================
if __name__ == "__main__":
   root= Tk()
   obj= chatbot(root)
   root.mainloop()
