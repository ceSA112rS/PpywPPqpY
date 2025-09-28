# 代码生成时间: 2025-09-29 00:01:23
import kivy\application
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
import random
import json


# 定义一个异常类，用于处理智能题库系统的错误
class QuestionBankException(Exception):
    pass


# 定义智能题库系统
class IntelligentQuestionBank(BoxLayout):
    def __init__(self, **kwargs):
        super(IntelligentQuestionBank, self).__init__(**kwargs)
        self.question_bank = self.load_question_bank()
        self.current_question_index = 0
        # 初始化界面布局
        self.init_ui()

    # 加载题库数据
    def load_question_bank(self):
        try:
            with open('question_bank.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise QuestionBankException('题库文件不存在')
        except json.JSONDecodeError:
            raise QuestionBankException('题库文件格式错误')

    # 初始化界面布局
    def init_ui(self):
        self.orientation = 'vertical'
        # 添加题目显示标签
        self.add_widget(Label(text='题目:', font_size=24))
        self.question_label = Label(font_size=18)
        self.add_widget(self.question_label)
        # 添加输入框
        self.input_box = TextInput(multiline=False)
        self.add_widget(self.input_box)
        # 添加提交按钮
        self.submit_button = Button(text='提交', on_press=self.submit_answer)
        self.add_widget(self.submit_button)

    # 提交答案
    def submit_answer(self, instance):
        answer = self.input_box.text
        if not answer.strip():
            self.show_error_popup('答案不能为空')
            return
        self.check_answer(answer)

    # 检查答案
    def check_answer(self, answer):
        current_question = self.question_bank[self.current_question_index]
        correct_answer = current_question['answer']
        if answer.lower() == correct_answer.lower():
            self.show_success_popup('答案正确！')
            self.next_question()
        else:
            self.show_error_popup('答案错误，正确答案是：' + correct_answer)

    # 显示成功提示框
    def show_success_popup(self, message):
        popup = Popup(title='成功', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

    # 显示错误提示框
    def show_error_popup(self, message):
        popup = Popup(title='错误', content=Label(text=message), size_hint=(None, None), size=(200, 200))
        popup.open()

    # 显示下一题
    def next_question(self):
        if self.current_question_index < len(self.question_bank) - 1:
            self.current_question_index += 1
            self.question_label.text = self.question_bank[self.current_question_index]['question']
        else:
            self.show_success_popup('所有题目已完成！')


# 定义应用程序类
class QuestionBankApp(kivy.application.App):
    def build(self):
        return IntelligentQuestionBank()


# 主函数
if __name__ == '__main__':
    QuestionBankApp().run()