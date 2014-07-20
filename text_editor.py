#a simple text editor

import wx
import os

class texteditor(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        self.Centre()
        filemenu= wx.Menu()
        self.aboutmenu = wx.Menu()
        self.exitmenu = wx.Menu()
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(self.aboutmenu, "About")
        menuBar.Append(self.exitmenu, "Exit")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        filemenu.AppendSeparator()
        new = filemenu.Append(-1, "New", "Create a new document.")
        openfile = filemenu.Append(-1, "Open", "Open an existing document.")
        save = filemenu.Append(-1, "Save", "Save your document.")
        saveas = filemenu.Append(-1, "Save As...", "Save your document under a new name.")
        
        #Event Binding
        self.Bind(wx.EVT_MENU_OPEN, self.menuclicks)
        self.Bind(wx.EVT_MENU, self.openfile, openfile)
        self.Bind(wx.EVT_MENU, self.savefile, save)
        self.Bind(wx.EVT_MENU, self.newfile, new)

    def menuclicks(self, e):
        #creates popup
        if e.GetMenu() == self.aboutmenu:
            popup = wx.MessageDialog(self, "A small, simple text editor created as a tool to help \
                                    William Archer learn programming. \n V1.0", "About", wx.OK)
            popup.ShowModal()
            popup.Destroy()
        #checks to see if its Exit
        elif e.GetMenu() == self.exitmenu:
            self.Destroy()
        else:
            e.Skip()

    def openfile(self, e):
        #Function to open files
        if self.control != '':
            dlg = wx.MessageDialog(self, "Are you sure you wish to open a new document with text on the screen?", \
                                   "Warning!", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.dirname = ''
                popup = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
                if popup.ShowModal() == wx.ID_OK:
                    self.filename = popup.GetFilename()
                    self.dirname = popup.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'r')
                    self.control.SetValue(f.read())
                    f.close()

                    self.SetTitle("Will's Simple Text Editor - " + self.filename)
                popup.Destroy()

    def savefile(self,e):
        #saving files
        self.dirname = ''
        popup = wx.FileDialog(self, "Save As...", self.dirname, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
        if popup.ShowModal() == wx.ID_OK:
            contents = self.control.GetValue()
            self.filename = popup.GetFilename()
            self.dirname = popup.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(contents)
            f.close()
            self.SetTitle("Will's Simple Text Editor - " + self.filename)
        popup.Destroy()

    def newfile(self, e):
        #creating a new file
        if self.control.GetValue() != "":
            popup = wx.MessageDialog(self, "Are you sure you want to create a new document?", "Warning!", wx.OK | wx.CANCEL)
            if popup.ShowModal() == wx.ID_OK:
                self.control.SetValue("")
                self.SetTitle("Will's Simple Text Editor")
                
app = wx.App(False)
frame = texteditor(None, "Will's Simple Text Editor")
app.MainLoop()
