#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Katana. A rotable and scalable image.
"""

from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.properties import NumericProperty
from kivy.uix.image import Image

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2015, bisector"
__credits__ = ["Kivy Team"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene@outlook.com"
__status__ = "Production"


class Katana(Image):
    
    angle = NumericProperty()
    
    def __init__(self, **kwargs):
        super(Katana, self).__init__(**kwargs)
        self.source = 'img/katana.png'
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(axis=(0, 0, 1))
        with self.canvas.after:
            PopMatrix()
        self.bind(pos=self._update, size=self._update)
        
    def _update(self, *args):
        self.on_angle()
            
    def on_angle(self, *args):
        self.rotation.origin = self.center
        self.rotation.angle = self.angle
