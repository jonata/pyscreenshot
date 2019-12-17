from easyprocess import EasyProcess
from PIL import Image
import logging
from pyscreenshot.tempexport import read_prog_img, extract_version

log = logging.getLogger(__name__)


PROGRAM = 'scrot'


class ScrotWrapper(object):
    name = 'scrot'
    childprocess = True

    def __init__(self):
        p = EasyProcess([PROGRAM, '-version'])
        p.enable_stdout_log = False
        p.enable_stderr_log = False
        p.call()

    def grab(self, bbox=None):
        im = read_prog_img([PROGRAM, '--silent'])
        if bbox:
            im = im.crop(bbox)
        return im

    def backend_version(self):
        return extract_version(
            EasyProcess([PROGRAM, '-version']).call().stdout)
