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

    def setupWidgets(self):
        self._initBasicControls()
        self._initKeywordSelections()


    def goPorgram(self):
        self.root.mainloop()

    #Loads the file
    def masterLoad(self):
        """Asks the user to select a filename of the appropriate type, then it creates the naive bayes
        network, and displays it."""
        fileOkay, filename = self._getFilename("Select your resume")
        if fileOkay: # TODO: Here we should parse the input file into readable contents
            print("Need to work on this part")


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

        # Quit Button
        masterQuitButton = Button(basicControlFrame, text="Quit", command=self.masterQuit)
        masterQuitButton.place(relx = 0.5, rely = 0.95, anchor=CENTER)

        # Load Button
        masterLoadButton = Button(basicControlFrame, text="Load", command=self.masterLoad)
        masterLoadButton.place(relx = 0.5, rely = 0.15, anchor = CENTER)

        # Error Output
        self.errorMessage = StringVar()
        loadErrorOutputLabel = Label(basicControlFrame, textvariable=self.errorMessage, font="Arial 12", padx=5, pady=0)
        loadErrorOutputLabel.grid(row=3, column=1)


    def _initKeywordSelections(self):
        #TODO: figure out what to do here
        return

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
