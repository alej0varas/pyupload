#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.1 on Tue Jan  8 17:42:08 2008

import wx

# begin wxGlade: extracode
# end wxGlade



class MarcoPrincipal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MarcoPrincipal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.caja_con_3_staticbox = wx.StaticBox(self, -1, "sizer_1")
        self.texto_nombre_archivo = wx.TextCtrl(self, -1, "")
        self.boton_examinar = wx.Button(self, -1, "Examinar")
        self.boton_subir = wx.Button(self, -1, "Subir")
        self.texto_estado = wx.TextCtrl(self, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.examinar_handler, self.boton_examinar)
        self.Bind(wx.EVT_BUTTON, self.subir_handler, self.boton_subir)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MarcoPrincipal.__set_properties
        self.SetTitle("Ftp_Uploader")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MarcoPrincipal.__do_layout
        caja = wx.BoxSizer(wx.VERTICAL)
        caja_con_3 = wx.StaticBoxSizer(self.caja_con_3_staticbox, wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.texto_nombre_archivo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.boton_examinar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        caja_con_3.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.boton_subir, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        caja_con_3.Add(sizer_1, 1, wx.EXPAND, 0)
        caja_con_3.Add(self.texto_estado, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        caja.Add(caja_con_3, 1, wx.EXPAND, 0)
        self.SetSizer(caja)
        caja.Fit(self)
        self.Layout()
        # end wxGlade

    def examinar_handler(self, event): # wxGlade: MarcoPrincipal.<event_handler>
        print "Event handler `examinar_handler' not implemented!"
        event.Skip()

    def subir_handler(self, event): # wxGlade: MarcoPrincipal.<event_handler>
        print "Event handler `subir_handler' not implemented!"
        event.Skip()

# end of class MarcoPrincipal


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    FTP_Uploader = MarcoPrincipal(None, -1, "")
    app.SetTopWindow(FTP_Uploader)
    FTP_Uploader.Show()
    app.MainLoop()
