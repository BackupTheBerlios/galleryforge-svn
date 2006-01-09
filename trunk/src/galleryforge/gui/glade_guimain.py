#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4 on Mon Jan  9 18:24:07 2006

import wx

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.templates = wx.Panel(self.notebook_1, -1)
        self.panel_1 = wx.Panel(self.templates, -1)
        self.image_sizes = wx.Panel(self.notebook_1, -1)
        self.album_layout = wx.Panel(self.notebook_1, -1)
        self.basics = wx.Panel(self.notebook_1, -1)
        self.launch = wx.Panel(self.notebook_1, -1)
        self.button_1 = wx.Button(self.launch, -1, "Start!")
        self.button_3 = wx.Button(self.launch, -1, "Save settings")
        self.exitBtn = wx.Button(self.launch, -1, "Exit")
        self.static_line_3 = wx.StaticLine(self.launch, -1, style=wx.LI_VERTICAL)
        self.text_ctrl_2 = wx.TextCtrl(self.launch, -1, u"galleryforge version 1.0.1\n© 2005-6 Martin Matusiak\n\nLicenced under the General Public License (GPL), which roughly means you can do whatever the hell you want with this code.", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.NO_BORDER)
        self.bitmap_3 = wx.StaticBitmap(self.launch, -1, wx.Bitmap("galleryforge_logo.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_1 = wx.StaticBitmap(self.basics, -1, wx.Bitmap("gf_gallery_path.png", wx.BITMAP_TYPE_ANY))
        self.label_4 = wx.StaticText(self.basics, -1, "gallery path:")
        self.gallery_path = wx.TextCtrl(self.basics, -1, "")
        self.button_2 = wx.Button(self.basics, -1, "...\n")
        self.static_line_1 = wx.StaticLine(self.basics, -1)
        self.label_2 = wx.StaticText(self.basics, -1, "image file extensions:")
        self.image_extensions = wx.TextCtrl(self.basics, -1, "jpg,png")
        self.label_3 = wx.StaticText(self.basics, -1, "thumbnail file suffix:")
        self.thumbnail_suffix = wx.TextCtrl(self.basics, -1, "_thumb")
        self.bitmap_2 = wx.StaticBitmap(self.album_layout, -1, wx.Bitmap("gf_album_layout.png", wx.BITMAP_TYPE_ANY))
        self.label_5 = wx.StaticText(self.album_layout, -1, "number of columns (nx):")
        self.album_cols = wx.SpinCtrl(self.album_layout, -1, "2", min=1, max=10)
        self.label_6 = wx.StaticText(self.album_layout, -1, "number of rows (yx):")
        self.album_rows = wx.SpinCtrl(self.album_layout, -1, "3", min=1, max=10)
        self.bitmap_1_copy_1_copy = wx.StaticBitmap(self.image_sizes, -1, wx.Bitmap("gf_img.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_2_copy_1_copy = wx.StaticBitmap(self.image_sizes, -1, wx.Bitmap("gf_thumb.png", wx.BITMAP_TYPE_ANY))
        self.label_5_copy_2_copy = wx.StaticText(self.image_sizes, -1, "image size (X):")
        self.image_size_x = wx.SpinCtrl(self.image_sizes, -1, "740", min=1, max=4000)
        self.label_5_copy_copy_1_copy = wx.StaticText(self.image_sizes, -1, "image size (Y):")
        self.image_size_y = wx.SpinCtrl(self.image_sizes, -1, "740", min=1, max=4000)
        self.label_7_copy_1_copy = wx.StaticText(self.image_sizes, -1, "thumbnail size (x):")
        self.thumbnail_size_x = wx.SpinCtrl(self.image_sizes, -1, "200", min=1, max=4000)
        self.label_8_copy_1_copy = wx.StaticText(self.image_sizes, -1, "thumbnail size (y):")
        self.thumbnail_size_y = wx.SpinCtrl(self.image_sizes, -1, "200", min=1, max=4000)
        self.text_ctrl_11 = wx.TextCtrl(self.templates, -1, "Using special characters directly in HTML breaks XHTML standards. It is recommended to use HTML codes instead.", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.NO_BORDER)
        self.label_7 = wx.StaticText(self.panel_1, -1, "'First':")
        self.tmp_first = wx.TextCtrl(self.panel_1, -1, "[&lt;&lt; First]")
        self.label_7_copy = wx.StaticText(self.panel_1, -1, "'Previous':")
        self.tmp_prev = wx.TextCtrl(self.panel_1, -1, "[&lt; Previous]")
        self.label_7_copy_1 = wx.StaticText(self.panel_1, -1, "'Index':")
        self.tmp_index = wx.TextCtrl(self.panel_1, -1, "[Index]")
        self.label_7_copy_1_copy_1 = wx.StaticText(self.panel_1, -1, "'Next':")
        self.tmp_next = wx.TextCtrl(self.panel_1, -1, "[Next &gt;]")
        self.label_7_copy_3 = wx.StaticText(self.panel_1, -1, "'Last':")
        self.tmp_last = wx.TextCtrl(self.panel_1, -1, "[Last &gt;&gt;]")
        self.static_line_2 = wx.StaticLine(self.panel_1, -1, style=wx.LI_VERTICAL)
        self.label_1 = wx.StaticText(self.panel_1, -1, "Char")
        self.label_8 = wx.StaticText(self.panel_1, -1, "HTML code")
        self.label_9 = wx.StaticText(self.panel_1, -1, "<")
        self.text_ctrl_4 = wx.TextCtrl(self.panel_1, -1, "&lt;", style=wx.TE_READONLY)
        self.label_10 = wx.StaticText(self.panel_1, -1, ">")
        self.text_ctrl_5 = wx.TextCtrl(self.panel_1, -1, "&gt;", style=wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onStartBtn, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.onSaveSettingsBtn, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.onExitBtn, self.exitBtn)
        self.Bind(wx.EVT_BUTTON, self.onFileSelectorBtn, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("galleryforge")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("galleryforge_logo.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(239, 239, 239))
        self.text_ctrl_2.SetMinSize((146,220))
        self.text_ctrl_2.SetBackgroundColour(wx.Colour(239, 239, 239))
        self.text_ctrl_2.SetForegroundColour(wx.Colour(0, 0, 0))
        self.gallery_path.SetMinSize((240, 22))
        self.button_2.SetMinSize((22, 22))
        self.image_extensions.SetMinSize((200, 22))
        self.thumbnail_suffix.SetMinSize((120, 22))
        self.album_cols.SetMinSize((42, 22))
        self.album_rows.SetMinSize((42, 22))
        self.image_size_x.SetMinSize((60, 22))
        self.image_size_y.SetMinSize((60, 22))
        self.thumbnail_size_x.SetMinSize((60, 22))
        self.thumbnail_size_y.SetMinSize((60, 22))
        self.text_ctrl_11.SetMinSize((380, 32))
        self.text_ctrl_11.SetBackgroundColour(wx.Colour(239, 239, 239))
        self.text_ctrl_11.SetForegroundColour(wx.Colour(0, 0, 0))
        self.tmp_first.SetMinSize((130, 22))
        self.tmp_prev.SetMinSize((130, 22))
        self.tmp_index.SetMinSize((130, 22))
        self.tmp_next.SetMinSize((130, 22))
        self.tmp_last.SetMinSize((130, 22))
        self.notebook_1.SetBackgroundColour(wx.Colour(239, 239, 239))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.FlexGridSizer(2, 1, 0, 0)
        sizer_5_copy = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(3, 2, 10, 10)
        grid_sizer_4 = wx.FlexGridSizer(5, 2, 10, 10)
        sizer_2_copy = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_4_copy_1_copy = wx.FlexGridSizer(2, 2, 0, 0)
        grid_sizer_6_copy_1_copy = wx.FlexGridSizer(2, 2, 10, 10)
        grid_sizer_5_copy_1_copy = wx.FlexGridSizer(2, 2, 10, 10)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(2, 2, 10, 10)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 10, 10)
        grid_sizer_2 = wx.FlexGridSizer(1, 3, 10, 10)
        sizer_2 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(3, 1, 10, 10)
        grid_sizer_6.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_6.Add(self.button_3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_6.Add(self.exitBtn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(grid_sizer_6, 1, wx.ALL|wx.EXPAND, 10)
        sizer_2.Add(self.static_line_3, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        sizer_7.Add(self.text_ctrl_2, 0, wx.TOP|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        sizer_7.Add(self.bitmap_3, 0, wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_6, 1, wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        self.launch.SetAutoLayout(True)
        self.launch.SetSizer(sizer_2)
        sizer_2.Fit(self.launch)
        sizer_2.SetSizeHints(self.launch)
        sizer_3.Add(self.bitmap_1, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_2.Add(self.label_4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_2.Add(self.gallery_path, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_2.Add(self.button_2, 0, wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(grid_sizer_2, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, 10)
        sizer_3.Add(self.static_line_1, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 12)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.image_extensions, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.thumbnail_suffix, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(grid_sizer_1, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        self.basics.SetAutoLayout(True)
        self.basics.SetSizer(sizer_3)
        sizer_3.Fit(self.basics)
        sizer_3.SetSizeHints(self.basics)
        sizer_4.Add(self.bitmap_2, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 10)
        grid_sizer_3.Add(self.label_5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.album_cols, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.label_6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.album_rows, 0, wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(grid_sizer_3, 1, wx.ALL|wx.EXPAND, 10)
        self.album_layout.SetAutoLayout(True)
        self.album_layout.SetSizer(sizer_4)
        sizer_4.Fit(self.album_layout)
        sizer_4.SetSizeHints(self.album_layout)
        grid_sizer_4_copy_1_copy.Add(self.bitmap_1_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4_copy_1_copy.Add(self.bitmap_2_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_5_copy_1_copy.Add(self.label_5_copy_2_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_5_copy_1_copy.Add(self.image_size_x, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_5_copy_1_copy.Add(self.label_5_copy_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_5_copy_1_copy.Add(self.image_size_y, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4_copy_1_copy.Add(grid_sizer_5_copy_1_copy, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6_copy_1_copy.Add(self.label_7_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6_copy_1_copy.Add(self.thumbnail_size_x, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6_copy_1_copy.Add(self.label_8_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6_copy_1_copy.Add(self.thumbnail_size_y, 1000, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4_copy_1_copy.Add(grid_sizer_6_copy_1_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2_copy.Add(grid_sizer_4_copy_1_copy, 0, wx.ALL|wx.ADJUST_MINSIZE, 10)
        self.image_sizes.SetAutoLayout(True)
        self.image_sizes.SetSizer(sizer_2_copy)
        sizer_2_copy.Fit(self.image_sizes)
        sizer_2_copy.SetSizeHints(self.image_sizes)
        sizer_5.Add(self.text_ctrl_11, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_4.Add(self.label_7, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.tmp_first, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.label_7_copy, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.tmp_prev, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.label_7_copy_1, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.tmp_index, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.label_7_copy_1_copy_1, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.tmp_next, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.label_7_copy_3, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.tmp_last, 0, wx.ADJUST_MINSIZE, 0)
        sizer_5_copy.Add(grid_sizer_4, 1, wx.LEFT|wx.TOP|wx.BOTTOM, 10)
        sizer_5_copy.Add(self.static_line_2, 0, wx.ALL|wx.EXPAND, 20)
        grid_sizer_5.Add(self.label_1, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_8, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_9, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.text_ctrl_4, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.label_10, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_5.Add(self.text_ctrl_5, 0, wx.ADJUST_MINSIZE, 0)
        sizer_5_copy.Add(grid_sizer_5, 1, wx.RIGHT|wx.TOP|wx.BOTTOM, 10)
        self.panel_1.SetAutoLayout(True)
        self.panel_1.SetSizer(sizer_5_copy)
        sizer_5_copy.Fit(self.panel_1)
        sizer_5_copy.SetSizeHints(self.panel_1)
        sizer_5.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.templates.SetAutoLayout(True)
        self.templates.SetSizer(sizer_5)
        sizer_5.Fit(self.templates)
        sizer_5.SetSizeHints(self.templates)
        self.notebook_1.AddPage(self.launch, "Launch")
        self.notebook_1.AddPage(self.basics, "Basics")
        self.notebook_1.AddPage(self.album_layout, "Album layout")
        self.notebook_1.AddPage(self.image_sizes, "Image sizes")
        self.notebook_1.AddPage(self.templates, "Templates")
        sizer_1.Add(self.notebook_1, 1, wx.ALL|wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def onStartBtn(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onStartBtn' not implemented!"
        event.Skip()

    def onSaveSettingsBtn(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onSaveSettingsBtn' not implemented!"
        event.Skip()

    def onExitBtn(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onExitBtn' not implemented!"
        event.Skip()

    def onFileSelectorBtn(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `onFileSelectorBtn' not implemented!"
        event.Skip()

# end of class MainFrame


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MainFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
