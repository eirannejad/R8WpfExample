#! python2
"""This script imports a XAML file and loads a UI"""

# the usual suspects
import os.path as op

import System
import Rhino

# import IronPython's WPF helper module
import clr
clr.AddReference("IronPython.Wpf")
import wpf


class MyWindow(System.Windows.Window):
    def __init__(self):
        # for testing
        xaml_file = op.join(op.dirname(__file__), "Window.xaml")
        # get path of xaml file from plugin location
        plugin = Rhino.PlugIns.PlugIn.PathFromName("WpfExample")
        if plugin:
            xaml_file = op.join(op.dirname(plugin), "shared/Window.xaml")
        
        # load xaml
        wpf.LoadComponent(self, xaml_file)

        # make rhino window the owner of this window
        helper = System.Windows.Interop.WindowInteropHelper(self)
        helper.Owner = Rhino.RhinoApp.MainWindowHandle()

        # set some properties
        self.Title = "Custom Window"

    def do_something(self, sender, args):
        Rhino.RhinoApp.WriteLine("Did Something!")


# create and instance of window and show
MyWindow().Show()
