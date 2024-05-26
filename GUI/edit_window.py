import tkinter as tk
from tkinter import Frame
from Process import EditWindow
from .content import edit_frame
from .imageviewer import EditViewApp
import data
import os

def render_edit():
    view:EditViewApp = data.EDIT_VIEW_APP
    edt:EditWindow = data.EDIT_WINDOW    
    edt.render()
    view.convert_img(edt.image)
    view.redraw_image()

def EditWindow_config(edt:EditWindow=None, width=720, height=560):
    if edt is None:
        edt = EditWindow(width=width, height=height)

    data.EDIT_WINDOW = edt
    render_edit()
