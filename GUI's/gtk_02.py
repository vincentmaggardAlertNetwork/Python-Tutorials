import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def test(button):
    print('The Button has been clicked!')

win = Gtk.Window()
grid = Gtk.Grid()
win.add(grid)
test_btn = Gtk.Button('Click Me...')
test_btn.connect("clicked", test)
test_btn2 = Gtk.Button('Click Me Again...')
test_btn2.connect("clicked", test)
grid.attach(test_btn, 0, 0, 1, 1)
grid.attach(test_btn2, 1, 0, 1, 1)
grid.attach(Gtk.Label('This Is A Test.'), 0, 1, 1, 1)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
