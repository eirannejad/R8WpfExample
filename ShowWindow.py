#! python2
"""This script imports a XAML file and loads a UI"""

import clr
import os.path as op

import System
import Rhino
from Rhino.PlugIns import PlugIn

clr.AddReference("IronPython.Modules")
clr.AddReference("IronPython.Wpf")
import wpf


class MyWindow(System.Windows.Window):
    def __init__(self):
        # for testing
        xaml_file = r"C:\Users\ein\gits\rhino\src4\rhino4\Plug-ins\RhinoCodePlugins\tests_projects\wpf\Window.xaml"
        # get path of xaml file from plugin location
        plugin = op.dirname(PlugIn.PathFromName("WpfExample"))
        if plugin:
            xaml_file = op.join(plugin, "shared/Window.xaml")
        
        # load xaml
        wpf.LoadComponent(self, xaml_file)
        pass

    def do_something(self, sender, args):
        Rhino.RhinoApp.WriteLine("Did Something!")



MyWindow().Show()
