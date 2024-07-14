from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Loginscreen(GridLayout):
	def __init__(self):
		super().__init__()

		#Text title
		self.cols = 1
		self.text_title = "Input:"
		self.text_label = Label(text=self.text_title,size_hint_y = 1)

		#Button
		self.gridlayout_button = GridLayout(cols = 2)
		self.button1 = Button(text = "1")
		self.button1.bind(on_press = self.event)
		self.button2 = Button(text = "2")
		self.button2.bind(on_press = self.event)
		self.gridlayout_button.add_widget(self.button1)
		self.gridlayout_button.add_widget(self.button2)
		self.gridlayout_button1 = GridLayout(cols = 1)
		self.button3 = Button(text = "3")
		self.button3.bind(on_press = self.event)
		self.button4 = Button(text = "4")
		self.button4.bind(on_press = self.event)
		self.gridlayout_button1.add_widget(self.button3)
		self.gridlayout_button1.add_widget(self.button4)
		self.gridlayout_button_simeline = GridLayout(cols = 2)
		self.gridlayout_button_simeline.add_widget(self.gridlayout_button)
		self.gridlayout_button_simeline.add_widget(self.gridlayout_button1)

		#Print in screen
		self.add_widget(self.text_label)
		self.add_widget(self.gridlayout_button_simeline)

	def event(self,x):
		self.text_label.text = x.text
		
		

class main(App):

	def build(self):

		return Loginscreen()

if __name__ == '__main__':
	main().run()