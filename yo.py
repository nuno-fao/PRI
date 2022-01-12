from googletrans import Translator

translator = Translator()
result = translator.translate('melhor jogo de tiros', dest='en')
print(result.text)