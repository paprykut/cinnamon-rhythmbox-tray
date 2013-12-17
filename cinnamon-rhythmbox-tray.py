#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2013 - Mikolaj Romel <mikolaj.romel@gmail.com>
#
# Published under the BSD License.
#
# Some of the code is taken from rhythmbox-systray by Elder Marco, kudos.
#

from gi.repository import GObject, RB, Peas

class HideRhythmbox(GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super(HideRhythmbox, self).__init__()

    def do_activate(self):
        """
        Activate delete event listener.
        """

        self.shell = self.object

        # We need to handle the delete-event signal in order to make possible
        # to us to minimize Rhythmbox to the system tray when the user tries
        # to close the main window.
        self.window = self.shell.get_property ('window')
        self.window_id = self.window.connect ('delete-event',
                                               self.delete_event_cb)
        
    def do_deactivate(self):
        """
        Deactivate.
        """

        self.window.disconnect(self.window_id)
        del self.window

    def delete_event_cb (self, widget, event):
        """
        Hide the main window.
        """

        self.window.hide()
        return True
