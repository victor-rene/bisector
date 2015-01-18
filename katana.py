from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.properties import NumericProperty
from kivy.uix.image import Image


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
