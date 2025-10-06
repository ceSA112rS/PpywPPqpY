# 代码生成时间: 2025-10-07 01:39:29
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import sys

# 模拟的信用评分模型
class CreditScoringModel:
    def __init__(self):
        self.weights = {
            "age": 0.05,
            "income": 0.15,
            "debt": 0.10,
            "loan_amount": 0.20,
            "credit_history": 0.10,
            "employment_history": 0.30,
            "education": 0.10
        }

    def calculate_score(self, data):
        """根据输入数据计算信用评分"""
        try:
            score = sum(self.weights[key] * data[key] for key in self.weights)
            return score
        except KeyError as e:
            raise ValueError(f"Missing data for {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

# Kivy应用界面
class CreditScoringApp(BoxLayout):
    def __init__(self, **kwargs):
        super(CreditScoringApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.model = CreditScoringModel()
        self.build_ui()

    def build_ui(self):
        self.add_widget(Label(text="Credit Scoring App"))

        # 输入字段
        self.inputs = [
            TextInput(multiline=False) for _ in self.model.weights.keys()
        ]
        for i, input_field in enumerate(self.inputs):
            label = Label(text=list(self.model.weights.keys())[i])
            self.add_widget(label)
            self.add_widget(input_field)

        # 评分按钮
        self.score_button = Button(text="Calculate Score")
        self.score_button.bind(on_press=self.calculate_score)
        self.add_widget(self.score_button)

        # 结果标签
        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def calculate_score(self, instance):
        """计算信用评分并显示结果"""
        try:
            data = {key: float(input_field.text) for key, input_field in zip(self.model.weights.keys(), self.inputs)}
            score = self.model.calculate_score(data)
            self.result_label.text = f"Credit Score: {score:.2f}"
        except ValueError as ve:
            self.show_error_popup(str(ve))
        except Exception as e:
            self.show_error_popup(str(e))

    def show_error_popup(self, message):
        """显示错误信息弹窗"""
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

# 主应用类
class MainApp(App):
    def build(self):
        return CreditScoringApp()

# 运行应用
if __name__ == '__main__':
    MainApp().run()