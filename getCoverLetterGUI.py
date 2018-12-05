"""
This file generates the GUI interface for the main program
"""


from tkinter import *
import tkinter.filedialog
from getTemplate import *
from resumeProcessor import *

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class introPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

class bodyPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       self.keywords = StringVar()
       self.keywords_list = list()

       basicControlFrame = Frame(self, bd=5, padx=5, pady=5, relief="groove")
       basicControlFrame.grid(row=1, column=1)
       basicControlFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
       basicControlFrameTitle = Label(basicControlFrame, text="Creating the body part", font="Arial 14 bold", padx=5,
                                      pady=5)
       basicControlFrameTitle.place(relx=0.5, rely=0.05, anchor=CENTER)

       # Load Button
       masterLoadButton = Button(basicControlFrame, text="Load", command=self.masterLoad)
       masterLoadButton.place(relx = 0.5, rely = 0.1, anchor = CENTER)

       # Keywords list box
       list_box_label = Label(basicControlFrame, text = "Keywords", font = "Arial 12 bold", padx=5, pady=5)
       list_box_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
       self.list_box = Listbox(basicControlFrame, listvariable=self.keywords, selectmode=MULTIPLE, width=30, height=15)
       self.list_box.place(relx = 0.5, rely = 0.5, anchor = CENTER)
       select_btn = Button(basicControlFrame, text="Choose", command=self.masterSelection)
       select_btn.place(relx=0.5, rely=0.85, anchor = CENTER)

       # Error Output
       self.errorMessage = StringVar()
       loadErrorOutputLabel = Label(basicControlFrame, textvariable=self.errorMessage, font="Arial 12", padx=5, pady=0)
       loadErrorOutputLabel.place(relx=0.5, rely = 0.9, anchor = CENTER)



   #Loads the file
   def masterLoad(self):
       """Asks the user to select a filename of the appropriate type, then it creates the naive bayes
       network, and displays it."""
       fileOkay, filename = self._getFilename("Select your resume")
       if fileOkay:
           self.keywords.set(extract_keywords(filename))
           Page.update(self)

   def masterSelection(self):
       selection = self.list_box.curselection()
       for i in selection:
           entry = self.list_box.get(i)
           self.keywords_list.append(entry)
           #TODO: creating templates with the keywords given


   #####################################
   #private methods

   def _getFilename(self, promptString):
       """Pops up a dialog box to ask the user for a filename, returns a boolean if the file was chosen well,
       and the name/path of the file. Otherwise, returns an empty string and a boolean False."""
       try:
           filename = tkinter.filedialog.askopenfilename(title=promptString)
           self.errorMessage.set("")
       except:
           self.errorMessage.set("incorrect filename")
           return False, ""
       if filename == "":
           return False, ""
       return True, filename


class conclusionPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="Creating the conclusion")
       label.pack(side="top", fill="both", expand=True)

class resultPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="I don't know how to do this part yet")
        label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = introPage(self)
        p2 = bodyPage(self)
        p3 = conclusionPage(self)
        p4 = resultPage(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Introduction", command=p1.lift)
        b2 = Button(buttonframe, text="Main Body", command=p2.lift)
        b3 = Button(buttonframe, text="Conclusion", command=p3.lift)
        b4 = Button(buttonframe, text="Result Cover Letter", command = p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

class getCoverLetterGUI:

    def __init__(self, *args, **kwargs):
        self.root = Tk()
        self.root.title("Get Cover Letter")
        self.root.geometry("500x500")
        self.root.resizable(0, 0)
        main = MainView(self.root)
        main.pack(side="top", fill="both", expand=True)


    def setupWidgets(self):
        # Quit Button
        masterQuitButton = Button(self.root, text="Quit", command=self.masterQuit)
        masterQuitButton.place(relx=0.5, rely=0.95, anchor=CENTER)

    def goPorgram(self):
        self.root.mainloop()


    """Quits the program"""
    def masterQuit(self):
        self.root.destroy()

###########################################################################################
# Run the program

def runProgram():
    gui = getCoverLetterGUI()
    gui.setupWidgets()
    gui.goPorgram()


if __name__ == "__main__":
    runProgram()
