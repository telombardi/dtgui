import wx
import operator
from dtree import DecisionTree

class Window(wx.Frame):
    def __init__(self, parent, title):
        """Constructor for Window class."""
        super(Window, self).__init__(parent, title=title, size=(400,220))
        self.widgets()
        self.Show()

    def widgets(self):
        """Function creates the GUI components (widgets) in the Window frame."""
        my_box = wx.GridSizer(3,2,1,1) #Create a grid with 3 rows and 2 columns

        font = wx.Font(16, wx.ROMAN, wx.ITALIC, wx.NORMAL) #Define font style
        color = (180,180,240) #Define light blue color
        
        self.SetBackgroundColour(color) #Set background color for Window

        #Credit Score label
        self.label = wx.StaticText(self, -1, "Credit Score ", style=wx.ALIGN_RIGHT)
        self.label.SetFont(font)
        my_box.Add(self.label, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)

        #Textbox for Credit Score
        self.textbox = wx.TextCtrl(self, style=wx.TE_RIGHT)
        my_box.Add(self.textbox, flag=wx.TOP | wx.BOTTOM, border=10)

        #Assess Loan Application Button
        self.btn1 = wx.Button(self,-1,"Assess Loan Application") 
        my_box.Add(self.btn1,0,wx.ALIGN_CENTER) 
        self.btn1.Bind(wx.EVT_BUTTON,self.assessLoan) #Bind event handler method to button

        #Clear Values Button
        self.btn2 = wx.Button(self, -1, "Clear Values")
        my_box.Add(self.btn2,0,wx.ALIGN_CENTER) 
        self.btn2.Bind(wx.EVT_BUTTON,self.clearForm) #Bind event handler method to button

        #Assessment Label
        self.label2 = wx.StaticText(self, -1, "Assessment ", style=wx.ALIGN_RIGHT)
        self.label2.SetFont(font)
        my_box.Add(self.label2, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        #Assessment Textbox
        self.textbox2 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        my_box.Add(self.textbox2, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        self.SetSizer(my_box)

    def assessLoan(self, event):
        """Event handler for Assess Loan Application button."""
        click = event.GetEventObject().GetLabel() 
        text_entered = self.textbox.GetValue()
        print(text_entered)
        dt = DecisionTree()
        dt.setCreditScore(float(text_entered))
        dt.executeTree()
        self.textbox2.SetValue(dt.printState())

    def clearForm(self, event):
        """Event handler for Clear Values button."""
        click = event.GetEventObject().GetLabel() 
        self.textbox.SetValue("")
        self.textbox2.SetValue("")

def main():
    myapp = wx.App()
    Window(None, title='Loan Processing Application')
    myapp.MainLoop()

main()

