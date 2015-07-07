#!/usr/bin/env python

from gi.repository import Gtk, Gdk, Vte, GLib
import os

terminal = Vte.Terminal()
terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ['HOME'],
    ["/bin/bash"],
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )

win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)
win.add(terminal)
win.show_all()

Gtk.main()
