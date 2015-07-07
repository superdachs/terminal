#!/usr/bin/env python

from gi.repository import Gtk, Gdk, Vte, GLib
import os


class Handler:

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)


class Terminal:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.builder.add_from_file("terminal.glade")
        self.builder.connect_signals(Handler())

    def run(self):
        window = self.builder.get_object("window1")
        window.set_title("terminal")
        window.set_default_size(640, 480)

        terminal = Vte.Terminal()
        terminal.connect("child-exited", Handler.onDeleteWindow)

        terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/bash"],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )

        window.add(terminal)
        window.show_all()
        Gtk.main()




if __name__ == "__main__":
    app = Terminal()
    app.run()
