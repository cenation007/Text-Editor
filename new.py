import tkinter as tk
from tkinter import filedialog
class Menubar:
    
    def __init__(self,parent):
        font_specs = ("ubuntu",14)
        
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)#used to display the menu
        
        #creating a pulldown menu, and add it to menu bar
        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File",command=parent.new_file,accelerator="Ctrl+N")
        file_dropdown.add_command(label="Open File",command=parent.open_file,accelerator="Ctrl+O")
        file_dropdown.add_command(label="Save",command=parent.save,accelerator="Ctrl+S")
        file_dropdown.add_command(label="Save As",command=parent.save_as,accelerator="Ctrl+Shift+N")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",command=parent.master.destroy)
        menubar.add_cascade(label="File",menu=file_dropdown)
      
class StatusBar:
    def __init__(self,parent):
        font_specs=("ubuntu",12)
        self.status = tk.StringVar()
        self.status.set("TextEditor- cenation1.0")
        label=tk.Label(parent.textarea,textvariable=self.status,fg="black"
                       ,bg="lightgrey",anchor="sw",font=font_specs)
        label.pack(side=tk.BOTTOM,fill=tk.BOTH)
        
    def updateStatusBar(self,*args):
        if isinstance(args[0],bool):
            self.status.set("Your file has been saved")
        else:
            self.status.set("TextEditor- cenation1.0")
        
class textEditor:
    
    def __init__(self,master):
        master.title("Untitled - Editor")
        master.geometry("1200x800")
        font_specs=("ubuntu",18)
        self.master=master
        self.dlg=None
        self.textarea=tk.Text(master,font=font_specs)#define the text area
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)#define the scroll bar
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)#making the text-area using textarea defined variable
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)#making the scroll to the right
        self.menubar=Menubar(self)
        self.statusbar=StatusBar(self)
        self.ftypes = [('Text Files','*.txt'),('Python files', '*.py'), ('All files', '*'),
                  ('HTML Documents','*.html'),('JavaScipt Files','*.js')]
        self.bind_shortcuts()
        
    def set_window_title(self,name=None):
        if name:
            self.master.title(name+"-textEditor")
        else:
            self.master.title("Untitled-textEditor")
    
    def new_file(self,*args):
        self.textarea.delete(1.0,tk.END)
        self.dlg=None
        self.set_window_title()
    
    def open_file(self,*args):
        self.dlg = filedialog.askopenfilename(defaultextension=".txt", filetypes = self.ftypes)
        if self.dlg != '':
            self.textarea.delete(1.0,tk.END)
            f=open(self.dlg, "r")
            if f.mode=='r':
                self.textarea.insert(1.0,f.read())
            self.set_window_title(self.dlg)
    
    def save(self,*args):
        if self.dlg:
            contents=self.textarea.get(1.0,tk.END)
            with open(self.filename,'w') as f:
                f.write(contents)
            self.statusbar.updateStatusBar(True)
        else:
            try:
                self.save_as()
            except Exception as e:
                print(e)
    
    def save_as(self,*args):
        try:
            f = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=self.ftypes)
            contents = self.textarea.get(1.0, tk.END)
            with open(f,'w') as f1:
                f1.write(contents)
            self.filename=f
            print(self.filename)
            self.set_window_title(self.filename)
            self.statusbar.updateStatusBar(True)
        except Exception as e:
            print(e)
            
    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>',self.new_file)
        self.textarea.bind('<Control-o>',self.open_file)
        self.textarea.bind('<Control-s>',self.save)
        self.textarea.bind('<Control-S>',self.save_as)
        self.textarea.bind('<Key>',self.statusbar.updateStatusBar)
        
if __name__=="__main__":
     master = tk.Tk()
     et=textEditor(master)
     master.mainloop()