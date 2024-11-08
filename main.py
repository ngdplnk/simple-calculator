from kivy.lang import Builder
from kivymd.app import MDApp

__version__ = "0.1"

kv_string = """
MDGridLayout:
    cols: 1
    rows: 2
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.9, 0.9
    MDTextField:
        id: text_field
        hint_text: 'Your expression'
        helper_text: 'Press the buttons below'
        helper_text_mode: 'on_focus'
        text: '0'
        size_hint_y: None
        multiline: False
        readonly: True
        mode: 'rectangle'
        font_size: '30sp'
        focus: True
        on_focus: self.focus = True
    MDGridLayout:
        rows: 5
        cols: 4
        resizeable: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.8, 0.8
        padding: [10, 30, 10, 10]
        spacing: [10, 10]
        MDRoundFlatButton:
            text: 'AC'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.clear_text_field()
        MDRoundFlatButton:
            text: '('
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('(')
        MDRoundFlatButton:
            text: ')'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press(')')
        MDRoundFlatButton:
            text: '^'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('**')
        MDRoundFlatButton:
            text: '7'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('7')
        MDRoundFlatButton:
            text: '8'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('8')
        MDRoundFlatButton:
            text: '9'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('9')
        MDRoundFlatButton:
            text: '*'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('*')
        MDRoundFlatButton:
            text: '4'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('4')
        MDRoundFlatButton:
            text: '5'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('5')
        MDRoundFlatButton:
            text: '6'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('6')
        MDRoundFlatButton:
            text: '-'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('-')
        MDRoundFlatButton:
            text: '1'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('1')
        MDRoundFlatButton:
            text: '2'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('2')
        MDRoundFlatButton:
            text: '3'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('3')
        MDRoundFlatButton:
            text: '+'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('+')
        MDRoundFlatButton:
            text: '0'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('0')
        MDRoundFlatButton:
            text: '.'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.on_button_press('.')
        MDRoundFlatButton:
            text: 'DEL'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.backspace()
        MDRoundFlatButton:
            text: '='
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            padding: [30, 30, 30, 30]
            on_press: app.calculate()
"""

class Calculator(MDApp):
    def build(self):
        self.title = 'Calculator'
        self.icon = 'assets/icon.png'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.expression = ''
        return Builder.load_string(kv_string)

    def on_button_press(self, button_text):
        if self.expression == '0' and button_text != '.' and button_text != '(' and button_text != ')':
            self.expression = ''
        self.expression += button_text
        self.root.ids.text_field.text = self.expression

    def calculate(self):
        try:
            self.root.ids.text_field.text = str(eval(self.expression))
        except Exception as e:
            # Handle error cases, such as division by zero
            self.root.ids.text_field.text = 'Error'

    def backspace(self):
        if self.expression != '0' and self.root.ids.text_field.text != '0' and self.root.ids.text_field.text != 'Error' and self.expression != 'Error':
            if len(self.expression) == 1:
                self.expression = '0'
                self.root.ids.text_field.text = self.expression
            else:
                self.expression = self.expression[:-1]
                self.root.ids.text_field.text = self.expression
        else:
            pass

    def clear_text_field(self):
        self.root.ids.text_field.text = '0'
        self.expression = '0'

if __name__ == '__main__':
    Calculator().run()