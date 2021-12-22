from datetime import datetime, timedelta

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

KV = """
Container:
        orientation: 'vertical'
        padding: 60
        spacing: 30
        
        days: days
        step: step
        visual: visual
        
        TextInput:
                id: days
                input_filter: 'int'
                multiline: False
                hint_text: 'Дні'
                pos_hint: {'center_x': 0.5, 'y': 0.1}
                size_hint: 0.3, 0.3
        TextInput:
                id: step
                input_filter: 'int'
                multiline: False
                hint_text: 'Шаг'
                color_text: 'red'
                pos_hint: {'center_x': 0.5, 'y': 0.1}
                size_hint: 0.3, 0.3
        Label:
                id: visual
                text: 'Тут буде ваша копілочка))'
                pos_hint: {'center_x': 0.5, 'y': 0.1}
                size_hint: 0.3, 0.3

        Button:
                text: 'Розрахувати'
                size_hint: 0.3, 0.3
                pos_hint: {'center_x': 0.5, 'y': 0.1}
                on_release: root.result()
"""

class Container(BoxLayout):

    def result(self):
        days = int(self.days.text)
        step = int(self.step.text)

        money_count = 0
        for numbers in range(1, days + 1):
            res = step * numbers
            money_count += res

        month_uk = [
            'Січні',
            'Лютому',
            'Березні',
            'Квітні',
            'Травні',
            'Червні',
            'Липні',
            'Серпні',
            'Вересні',
            'Жовтні',
            'Листопаді',
            'Грудні',
        ]

        to_day_and_result = datetime.today() + timedelta(days)

        month = list(str(to_day_and_result.strftime('%m')))
        print(month)
        if '0' in month:
            print(3)
            month.remove('0')
            month_res = month_uk[int(month[0]) - 1]
        else:
            month = int(to_day_and_result.strftime('%m'))
            month_res = month_uk[month - 1]


        day_res = to_day_and_result.strftime('%d/%Y ')

        self.visual.text = f'У {month_res} {day_res}Вийде - {money_count}\nЗ шагом - {step}\nДнів - {days}'


class MyApp(App):

    running = True


    def build(self):

        return Builder.load_string(KV)

    def on_enter(self):
        return self
    def btn_press(self, instance):
        print(self.on_enter())
    def on_stop(self):
        self.running = False

MyApp().run()

