from kivy.app import App
from kivy.lang import Builder
from kivy.properties import (ListProperty, StringProperty, NumericProperty,
                             ObjectProperty)
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''
<MappingOptions>:
    orientation: 'vertical'
    texture_mapping: 'none'
    line_width: slider.value if slider else 10
    line_widget: line_wid
    Widget:
        id: line_wid
        canvas:
            Color:
                rgba: 1, 0, 0, 1
            Line:
                close: True
                source: 'colours2.png'
                width: root.line_width
                points: root.line_points
                texture_mapping: root.texture_mapping
                tex_coords: [0, 0, 1, 0, 1, 1, 0, 1]
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: sp(40)
        Label:
            text: 'texture mapping:'
        Button:
            text: 'none'
            on_press: root.texture_mapping = 'none'
        Button:
            text: 'repeat'
            on_press: root.texture_mapping = 'repeat'
        Button:
            text: 'pointwise_stretch'
            on_press: root.texture_mapping = 'pointwise_stretch'
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: sp(40)
        Slider:
            id: slider
            min: 1
            max: 40
            value: 10
        Button:
            text: 'clear'
            on_press: root.line_points = []
''')


class MappingOptions(BoxLayout):
    line_points = ListProperty([])
    texture_mapping = StringProperty('none')
    line_width = NumericProperty(10)
    line_widget = ObjectProperty()

    def on_touch_down(self, touch):
        super(MappingOptions, self).on_touch_down(touch)
        self.on_touch_move(touch)

    def on_touch_move(self, touch):
        super(MappingOptions, self).on_touch_move(touch)
        if self.line_widget.collide_point(*touch.pos):
            self.line_points.extend(touch.pos)


class LinesApp(App):
    def build(self):
        return MappingOptions()

if __name__ == "__main__":
    LinesApp().run()
