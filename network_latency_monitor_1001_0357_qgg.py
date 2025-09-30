# 代码生成时间: 2025-10-01 03:57:21
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests
import time

"""
Network Latency Monitor using the Kivy framework.
This application allows users to monitor network latency by sending requests to a specified endpoint.
"""

class NetworkLatencyMonitorApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create UI elements
        self.endpoint_input = TextInput(text='', multiline=False, size_hint_y=None, height=40)
        self.latency_label = Label(text='Latency: N/A', size_hint_y=None, height=40)
        self.test_button = Button(text='Test Latency', size_hint_y=None, height=40)

        # Add UI elements to the main layout
        main_layout.add_widget(self.endpoint_input)
        main_layout.add_widget(self.latency_label)
        main_layout.add_widget(self.test_button)

        # Bind button click event to the test_latency method
        self.test_button.bind(on_press=self.test_latency)

        # Return the main layout
        return main_layout

    def test_latency(self, instance):
        # Get the endpoint from the text input
        endpoint = self.endpoint_input.text

        try:
            # Send a GET request to the endpoint
            response = requests.get(endpoint)

            # Calculate latency
            latency = time.time() - response.elapsed.total_seconds()

            # Update the latency label
            self.latency_label.text = f'Latency: {latency:.2f} seconds'
        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            self.latency_label.text = f'Error: {e}'
        except Exception as e:
            # Handle other exceptions
            self.latency_label.text = f'Error: {e}'


if __name__ == '__main__':
    NetworkLatencyMonitorApp().run()