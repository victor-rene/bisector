#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Slash. Rotable and scalable image. The temperature property sets the color.
"""

from kivy.graphics import Color, Rectangle
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.graphics.instructions import InstructionGroup
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2015, bisector"
__credits__ = ["Kivy Team"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene@outlook.com"
__status__ = "Production"


class Slash(Widget):

    angle = NumericProperty()
    temperature = NumericProperty()
    """ 1. for hot, 0. for cold """

    def __init__(self, **kwargs):
        super(Slash, self).__init__(**kwargs)
        self._clr_inst = None
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(axis=(0, 0, 1))
        with self.canvas:
            self.color = Color(1, 1, 1, 1)
            self.rect = Rectangle(source='img/slash.png')
        with self.canvas.after:
            PopMatrix()
            Color(1, 1, 1, 1)
        self.bind(pos=self._update, size=self._update)

    def _update(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.on_angle()

    def on_angle(self, *args):
        self.rotation.origin = self.x + self.width / 2., self.y
        self.rotation.angle = self.angle

    def on_temperature(self, *args):
        if not self.color:
            return
        # h = .5 - self.temperature / 2.
        h = self.temperature / 2.
        s = v = .9
        a = 1.
        self.color.hsv = (h, s, v)
        
    def reset_color(self):
        self.color.rgba = (1., 1., 1., 1.)
