"""
This file generates the GUI interface for the main program
"""


from tkinter import *
import tkinter.filedialog
from getTemplate import *
from resumeProcessor import *

class getCoverLetterGUI:


    def __init__(self):
        self.root = Tk()
        self.root.title("Get Cover Letter")
        self.root.geometry("500x500")
        self.root.resizable(0, 0)
        self.keywords = StringVar()

    def setupWidgets(self):
        self._initBasicControls()

    def goPorgram(self):
        self.root.mainloop()

    #Loads the file
    def masterLoad(self):
        """Asks the user to select a filename of the appropriate type, then it creates the naive bayes
        network, and displays it."""
        fileOkay, filename = self._getFilename("Select your resume")
        if fileOkay:
            self.keywords.set(extract_keywords(filename))
            self.root.update()

    # def masterSelection(self):
    #     self.root.update()

    """Quits the program"""
    def masterQuit(self):
        self.root.destroy()



    #####################################
    #private methods
    def _initBasicControls(self):
        basicControlFrame = Frame(self.root, bd=5, padx=5, pady=5, relief="groove")
        basicControlFrame.grid(row=1, column=1)
        basicControlFrame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
        basicControlFrameTitle = Label(basicControlFrame, text="Generate Your Cover Letter", font="Arial 14 bold", padx=5,
                                       pady=5)
        basicControlFrameTitle.place(relx=0.5, rely=0.05, anchor=CENTER)

        # Load Button
        masterLoadButton = Button(basicControlFrame, text="Load", command=self.masterLoad)
        masterLoadButton.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        # Keywords list box
        list_box_label = Label(basicControlFrame, text = "Keywords", font = "Arial 12 bold", padx=5, pady=5)
        list_box_label.place(relx = 0.5, rely = 0.15, anchor = CENTER)
        list_box = Listbox(basicControlFrame, listvariable=self.keywords, selectmode=MULTIPLE, width=20, height=10)
        list_box.place(relx = 0.5, rely = 0.35, anchor = CENTER)

        # Quit Button
        masterQuitButton = Button(basicControlFrame, text="Quit", command=self.masterQuit)
        masterQuitButton.place(relx = 0.5, rely = 0.95, anchor=CENTER)

        # Error Output
        self.errorMessage = StringVar()
        loadErrorOutputLabel = Label(basicControlFrame, textvariable=self.errorMessage, font="Arial 12", padx=5, pady=0)
        loadErrorOutputLabel.grid(row=3, column=1)


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



###########################################################################################
# Run the program

def runProgram():
    gui = getCoverLetterGUI()
    gui.setupWidgets()
    gui.goPorgram()


if __name__ == "__main__":
    runProgram()
