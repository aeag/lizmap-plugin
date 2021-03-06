# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lizmapDialog
                 A QGIS plugin
 Publication plugin for Lizmap web application, by 3liz.com
                -------------------
    begin        : 2011-11-01
    copyright      : (C) 2011 by 3liz
    email        : info@3liz.com
 ***************************************************************************/

/****** BEGIN LICENSE BLOCK *****
 Version: MPL 1.1/GPL 2.0/LGPL 2.1

 The contents of this file are subject to the Mozilla Public License Version
 1.1 (the "License"); you may not use this file except in compliance with
 the License. You may obtain a copy of the License at
 http://www.mozilla.org/MPL/

 Software distributed under the License is distributed on an "AS IS" basis,
 WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 for the specific language governing rights and limitations under the
 License.

 The Original Code is 3liz code,

 The Initial Developer of the Original Code are René-Luc D'Hont rldhont@3liz.com
 and Michael Douchin mdouchin@3liz.com
 Portions created by the Initial Developer are Copyright (C) 2011
 the Initial Developer. All Rights Reserved.

 Alternatively, the contents of this file may be used under the terms of
 either of the GNU General Public License Version 2 or later (the "GPL"),
 or the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 in which case the provisions of the GPL or the LGPL are applicable instead
 of those above. If you wish to allow use of your version of this file only
 under the terms of either the GPL or the LGPL, and not to allow others to
 use your version of this file under the terms of the MPL, indicate your
 decision by deleting the provisions above and replace them with the notice
 and other provisions required by the GPL or the LGPL. If you do not delete
 the provisions above, a recipient may use your version of this file under
 the terms of any one of the MPL, the GPL or the LGPL.

 ***** END LICENSE BLOCK ***** */
"""

import os
from PyQt4 import QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import *


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui_lizmap.ui'))


class lizmapDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(lizmapDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
