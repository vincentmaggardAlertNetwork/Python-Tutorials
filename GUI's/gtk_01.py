import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def test(button):
    print('The Button has been clicked!')

win = Gtk.Window()
test_btn = Gtk.Button('Click Me...')
win.add(test_btn)
test_btn.connect("clicked", test)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
