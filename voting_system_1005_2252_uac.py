# 代码生成时间: 2025-10-05 22:52:42
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.storage.jsonstore import JsonStore

# 投票系统的JSON存储文件
STORE_FILE = 'votes.store'

# 投票选项的数据结构
class VoteOption(BoxLayout):
    value = StringProperty('')  # 投票选项的字符串表示
    selected = BooleanProperty(False)  # 是否被选中

    def on_touch_down(self, touch):
        # 处理触摸事件，切换选中状态
        if self.collide_point(*touch.pos):
            self.selected = not self.selected
            return True

# 投票系统的主界面
class VotingSystem(GridLayout):
    options = ListProperty([])  # 投票选项列表
    current_option = StringProperty('')  # 当前选中的选项

    def __init__(self, **kwargs):
        super(VotingSystem, self).__init__(**kwargs)
        self.store = JsonStore(STORE_FILE)
        self.load_options()
        self.bind(options=self.update_store)

    def load_options(self):
        # 加载已有的投票选项
        if 'votes' in self.store:
            self.options = [VoteOption(value=str(option)) for option in self.store['votes']]
        else:
            self.options = []

    def add_option(self):
        # 添加新的投票选项并更新存储
        new_option = self.option_input.text
        if new_option and new_option not in [option.value for option in self.options]:
            self.options.append(VoteOption(value=new_option))
            self.store.put('votes', self.options)
            self.option_input.text = ''
        else:
            self.show_error('Invalid option.')

    def cast_vote(self):
        # 投票并更新存储
        selected_option = next((option for option in self.options if option.selected), None)
        if selected_option:
            self.store.put('vote', selected_option.value)
            self.show_message('Vote cast successfully!')
        else:
            self.show_error('Please select an option.')

    def show_message(self, message):
        # 显示消息
        Window.alert(title='Info', message=message)

    def show_error(self, message):
        # 显示错误
        Window.alert(title='Error', message=message)

    def update_store(self, instance, options):
        # 更新存储中的选项列表
        self.store.put('votes', [option.value for option in options])

# 投票系统的应用类
class VotingApp(App):
    def build(self):
        return VotingSystem()

if __name__ == '__main__':
    VotingApp().run()