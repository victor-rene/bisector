#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main module, builds the screen manager. The screen manager creates the other
screens.
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout

from menuscreen import MenuScreen
from gamescreen import GameScreen
from scorescreen import ScoreScreen

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2015, bisector"
__credits__ = ["Kivy Team"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene@outlook.com"
__status__ = "Production"


class RootWidget(ScreenManager):

    def __init__(self, **kwargs):
        super(ScreenManager, self).__init__(**kwargs)
        ms = MenuScreen(self, name='menu')
        self.add_widget(ms)
        gs = GameScreen(self, name='game')
        self.add_widget(gs)
        ss = ScoreScreen(self, name='score')
        self.add_widget(ss)
        self.current = 'menu'
        
    def newgame(self, *args):
        self.current = 'game'
        
    def menu(self, *args):
        self.current = 'menu'
        
    def show_scores(self, *args):
        self.current = 'score'
        self.get_screen('score').load_scores()
        

class BisectorApp(App):
    
    def build(self):
        return RootWidget()

        
if __name__ == '__main__':
    BisectorApp().run()
