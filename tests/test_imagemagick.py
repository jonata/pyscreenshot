from pyscreenshot.util import use_x_display
from bt import backend_to_check, prog_check

if use_x_display():
    if prog_check(["import", "-version"]):

        def test_imagemagick():
            backend_to_check("imagemagick")
