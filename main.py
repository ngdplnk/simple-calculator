from kivy.lang import Builder
from kivymd.app import MDApp

__version__ = "0.1"

kv_string = """
MDGridLayout:
    cols: 1
    rows: 2
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.8, 0.8
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
    MDGridLayout:
        rows: 5
        cols: 4
        resizeable: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.8, 0.8
        padding: [10, 30, 10, 10]
        spacing: [10, 10]
        MDFillRoundFlatButton:
            text: 'AC'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.clear_text_field()
        MDFillRoundFlatButton:
            text: '('
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('(')
        MDFillRoundFlatButton:
            text: ')'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press(')')
        MDFillRoundFlatButton:
            text: '^'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('**')
        MDFillRoundFlatButton:
            text: '7'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('7')
        MDFillRoundFlatButton:
            text: '8'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('8')
        MDFillRoundFlatButton:
            text: '9'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('9')
        MDFillRoundFlatButton:
            text: '*'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('*')
        MDFillRoundFlatButton:
            text: '4'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('4')
        MDFillRoundFlatButton:
            text: '5'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('5')
        MDFillRoundFlatButton:
            text: '6'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('6')
        MDFillRoundFlatButton:
            text: '-'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('-')
        MDFillRoundFlatButton:
            text: '1'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('1')
        MDFillRoundFlatButton:
            text: '2'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('2')
        MDFillRoundFlatButton:
            text: '3'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('3')
        MDFillRoundFlatButton:
            text: '+'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('+')
        MDFillRoundFlatButton:
            text: '0'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('0')
        MDFillRoundFlatButton:
            text: '.'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.on_button_press('.')
        MDFillRoundFlatButton:
            text: 'DEL'
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
            on_press: app.backspace()
        MDFillRoundFlatButton:
            text: '='
            font_size: '25sp'
            bold: True
            size_hint: 0.2, 0.2
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
            # Evaluate the expression and update text field
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