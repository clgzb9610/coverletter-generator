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

        basicControlFrame = Frame(self, bd=5, padx=5, pady=5, relief="groove")
        basicControlFrame.grid(row=1, column=1)
        basicControlFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
        basicControlFrameTitle = Label(basicControlFrame, text="Creating the introduction", font="Arial 14 bold", padx=5,
                                      pady=5)
        basicControlFrameTitle.place(relx=0.5, rely=0.05, anchor=CENTER)

        self.position_input = StringVar()
        position_label = Label(basicControlFrame, text = "Position Applied: ", font="Arial 12 bold", padx = 5, pady=5)
        position_label.place(relx = 0.2, rely = 0.2, anchor = CENTER)
        position_entry = Entry(basicControlFrame, textvariable=self.position_input, font="Arial 12 bold")
        position_entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)

        self.resource_input = StringVar()
        resource_label = Label(basicControlFrame, text = "Resource of this opportunity: ", font="Arial 12 bold", padx = 5, pady=5)
        resource_label.place(relx = 0.2, rely = 0.3, anchor = CENTER)
        resource_entry = Entry(basicControlFrame, textvariable=self.resource_input, font="Arial 12 bold")
        resource_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)

        self.reason_input = StringVar()
        reason_label = Label(basicControlFrame, text = "Reasons of appling: ", font="Arial 12 bold", padx = 5, pady=5)
        reason_label.place(relx = 0.2, rely = 0.4, anchor = CENTER)
        reason_entry = Entry(basicControlFrame, textvariable=self.reason_input, font="Arial 12 bold")
        reason_entry.place(relx = 0.5, rely = 0.4, anchor = CENTER)


    def get_intro_paragraph(self):
        return "" #TODO: need to combine all information and generate a paragraph


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

        # Information
        self.finished_template = StringVar()


    def get_main_paragraph(self):
        return "" #TODO: need to combine all information and generate a paragraph

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
            #TODO: creating templates with the keywords given and assign that into self.finished_template


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

    def get_conclusion_paragraph(self):
        return "" #TODO: need to combine all information and generate a paragraph


class resultPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        basicControlFrame = Frame(self, bd=5, padx=5, pady=5, relief="groove")
        basicControlFrame.grid(row=1, column=1)
        basicControlFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
        basicControlFrameTitle = Label(basicControlFrame, text="Here's the result", font="Arial 14 bold", padx=5,
                                      pady=5)
        basicControlFrameTitle.place(relx=0.5, rely=0.05, anchor=CENTER)

        self.result_paragraph = StringVar()
        result_label = Label(basicControlFrame, textvariable=self.result_paragraph, font="Arial 12", padx=5, pady=5)
        result_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    def set_result_paragraph(self, intro, main, conclusion):
        self.result_paragraph.set(intro + "/n" + main + "/n" + conclusion)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.p1 = introPage(self)
        self.p2 = bodyPage(self)
        self.p3 = conclusionPage(self)
        self.p4 = resultPage(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Introduction", command=self.p1.lift)
        b2 = Button(buttonframe, text="Main Body", command=self.p2.lift)
        b3 = Button(buttonframe, text="Conclusion", command=self.p3.lift)
        b4 = Button(buttonframe, text="Result Cover Letter", command = self.get_all_info) #TODO: gather information method

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        self.p1.show()

    def get_all_info(self):
        self.p4.lift()
        intro = self.p1.get_intro_paragraph()
        main_body = self.p2.get_main_paragraph()
        conclusion = self.p3.get_conclusion_paragraph()
        self.p4.set_result_paragraph(intro, main_body, conclusion)


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
