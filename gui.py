from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button  # Add this line to import the Button widget

# Conversion rate from INR to USD
conversion_rate = 0.014

class CurrencyConverter(App):
    
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=12)
        
        # Labels
        label_inr = Label(text='INR | Indian Rupee Amount:')
        label_usd = Label(text='USD | Dollar Equivalent:')
        
        # TextInputs
        self.input_inr = TextInput(multiline=False, input_type='number')
        self.output_usd = TextInput(multiline=False, readonly=True)
        
        # Button
        button_convert = Button(text='Convert')  # Corrected the import
        
        # Bind the button press to the convert function
        button_convert.bind(on_press=self.convert)
        
        # Add widgets to the layout
        layout.add_widget(label_inr)
        layout.add_widget(self.input_inr)
        layout.add_widget(label_usd)
        layout.add_widget(self.output_usd)
        layout.add_widget(button_convert)
        
        return layout
    
    def convert(self, instance):
        # Get input value and convert it to USD
        try:
            amount_inr = float(self.input_inr.text)
            amount_usd = amount_inr * conversion_rate
            self.output_usd.text = f'{amount_usd:.2f} USD'
        except ValueError:
            self.output_usd.text = 'Invalid input'

if __name__ == '__main__':
    CurrencyConverter().run()
