from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Tenebre(App):
    def build(self):
        tela = BoxLayout(orientation='vertical',
                         padding=20, spacing=15)

        tela.add_widget(Label(
            text='TENEBRE ONLINE',
            font_size=30,
            color=(0, 1, 0, 1)
        ))

        self.entrada = TextInput(
            hint_text='Digite um comando...',
            size_hint_y=None,
            height=50
        )
        tela.add_widget(self.entrada)

        botao = Button(
            text='EXECUTAR',
            size_hint_y=None,
            height=50
        )
        botao.bind(on_press=self.executar)
        tela.add_widget(botao)

        self.resposta = Label(text='Olá! Eu sou o TENEBRE.')
        tela.add_widget(self.resposta)

        return tela

    def executar(self, instance):
        comando = self.entrada.text.lower().strip()

        if comando in ['oi', 'olá']:
            self.resposta.text = 'TENEBRE: Olá! Como posso ajudar?'
        elif comando == 'ajuda':
            self.resposta.text = 'Comandos: oi, olá, ajuda, sair'
        elif comando == 'sair':
            self.stop()
        else:
            self.resposta.text = 'TENEBRE: Comando não reconhecido.'

Tenebre().run()
