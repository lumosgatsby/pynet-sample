from pythonnet import load
load("coreclr", runtime_config="./runtimeconfig.json")
import clr

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *

clr.AddReference("WinFormsLibrary")
from WinFormsLibrary import *

form = Form1()
form.Text = "Hello World"
form.textBox1.Text="Hello World"
Application.Run(form)
