from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout

from menuscreen import MenuScreen
from gamescreen import GameScreen


class RootWidget(ScreenManager):

    def __init__(self, **kwargs):
        super(ScreenManager, self).__init__(**kwargs)
        ms = MenuScreen(self, name='menu')
        self.add_widget(ms)
        gs = GameScreen(self, name='game')
        self.add_widget(gs)
        self.current = 'menu'
        
    def newgame(self, *args):
        self.current = 'game'
        

class BisectorApp(App):
    
    def build(self):
        return RootWidget()

        
if __name__ == '__main__':
    BisectorApp().run()
