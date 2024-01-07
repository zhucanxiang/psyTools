
from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com.hk',
      'translate.google.cn'
    ])

translations = translator.translate(['hello'],dest='zh-cn')

for translation in translations:
    print(translation.text)
