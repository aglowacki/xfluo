# #########################################################################
# Copyright (c) 2018, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2018. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################


from PyQt5 import QtCore, QtWidgets


class HotspotControlsWidget(QtWidgets.QWidget):

    def __init__(self):
        super(HotspotControlsWidget, self).__init__()

        self.initUI()

    def initUI(self):
        self.xSize = 10
        self.ySize = 10
        button1size = 250
        button2size = 122.5
        button3size = 73.3
        button4size = 57.5

        self.xUpBtn = QtWidgets.QPushButton("x: +")
        self.xUpBtn.setMaximumWidth(button4size)
        self.xUpBtn.setMinimumWidth(button4size)
        self.xUpBtn.clicked.connect(self.xUp)
        self.xDownBtn = QtWidgets.QPushButton("x: -")
        self.xDownBtn.setMaximumWidth(button4size)
        self.xDownBtn.setMinimumWidth(button4size)
        self.xDownBtn.clicked.connect(self.xDown)
        self.yUpBtn = QtWidgets.QPushButton("y: +")
        self.yUpBtn.setMaximumWidth(button4size)
        self.yUpBtn.setMinimumWidth(button4size)
        self.yUpBtn.clicked.connect(self.yUp)
        self.yDownBtn = QtWidgets.QPushButton("y: -")
        self.yDownBtn.setMaximumWidth(button4size)
        self.yDownBtn.setMinimumWidth(button4size)
        self.yDownBtn.clicked.connect(self.yDown)
        self.xSizeLbl = QtWidgets.QLabel("x Size")
        self.xSizeLbl.setMaximumWidth(button4size)
        self.xSizeLbl.setMinimumWidth(button4size)
        self.ySizeLbl = QtWidgets.QLabel("y Size")
        self.ySizeLbl.setMaximumWidth(button4size)
        self.ySizeLbl.setMinimumWidth(button4size)
        self.xSizeTxt = QtWidgets.QLineEdit(str(self.xSize))
        self.xSizeTxt.setMaximumWidth(button4size)
        self.xSizeTxt.setMinimumWidth(button4size)
        self.ySizeTxt = QtWidgets.QLineEdit(str(self.ySize))
        self.ySizeTxt.setMaximumWidth(button4size)
        self.ySizeTxt.setMinimumWidth(button4size)

        self.combo1 = QtWidgets.QComboBox(self)
        self.combo1.setMaximumWidth(button1size)
        self.combo1.setMinimumWidth(button1size)
        self.combo2 = QtWidgets.QComboBox(self)
        self.combo2.setMaximumWidth(button2size)
        self.combo2.setMinimumWidth(button2size)
        self.combo3 = QtWidgets.QComboBox(self)
        self.combo3.setMaximumWidth(button1size)
        self.combo3.setMinimumWidth(button1size)
        self.lbl3 = QtWidgets.QLabel("hotspot group#")
        self.lbl3.setMaximumWidth(button2size)
        self.lbl3.setMinimumWidth(button2size)

        for i in range(5):
            self.combo2.addItem(str(i + 1))
        self.btn1 = QtWidgets.QPushButton("Hotspots to a line")
        self.btn1.setMaximumWidth(button1size)
        self.btn1.setMinimumWidth(button1size)
        self.btn2 = QtWidgets.QPushButton("Hotspots to a sine curve")
        self.btn2.setMaximumWidth(button1size)
        self.btn2.setMinimumWidth(button1size)
        self.btn3 = QtWidgets.QPushButton("set y")
        self.btn3.setMaximumWidth(button1size)
        self.btn3.setMinimumWidth(button1size)
        self.btn4 = QtWidgets.QPushButton("Clear hotspot data")
        self.btn4.setMaximumWidth(button1size)
        self.btn4.setMinimumWidth(button1size)

        hb1 = QtWidgets.QHBoxLayout()
        hb1.addWidget(self.xSizeLbl)
        hb1.addWidget(self.xUpBtn)
        hb1.addWidget(self.xDownBtn)
        hb1.addWidget(self.xSizeTxt)
        hb2 = QtWidgets.QHBoxLayout()
        hb2.addWidget(self.ySizeLbl)
        hb2.addWidget(self.yUpBtn)
        hb2.addWidget(self.yDownBtn)
        hb2.addWidget(self.ySizeTxt)

        hb3 = QtWidgets.QHBoxLayout()
        hb3.addWidget(self.lbl3)
        hb3.addWidget(self.combo2)

        vb1 = QtWidgets.QVBoxLayout()
        vb1.addLayout(hb1)
        vb1.addLayout(hb2)

        vb2 = QtWidgets.QVBoxLayout()
        vb2.addLayout(hb3)
        vb2.addWidget(self.btn1)
        vb2.addWidget(self.btn2)
        vb2.addWidget(self.btn3)
        vb2.addWidget(self.btn4)

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.combo1)
        vb.addWidget(self.combo3)
        vb.addLayout(vb1)
        vb.addLayout(vb2)

        self.setLayout(vb)

    def changeXSize(self):
        self.xSize = int(self.xSizeTxt.text())

    def changeYSize(self):
        self.ySize = int(self.ySizeTxt.text())

    def xUp(self):
        self.changeXSize()
        self.changeYSize()
        self.xSize += 2
        self.xSizeTxt.setText(str(self.xSize))

    def xDown(self):
        self.changeXSize()
        self.changeYSize()
        self.xSize -= 2
        self.xSizeTxt.setText(str(self.xSize))

    def yUp(self):
        self.changeXSize()
        self.changeYSize()
        self.ySize += 2
        self.ySizeTxt.setText(str(self.ySize))

    def yDown(self):
        self.changeXSize()
        self.changeYSize()
        self.ySize -= 2
        self.ySizeTxt.setText(str(self.ySize))
