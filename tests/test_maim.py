from pyscreenshot.util import use_x_display
from bt import backend_to_check, prog_check

if use_x_display():
    if prog_check(["maim", "--version"]):

        def test_maim():
            backend_to_check("maim")
