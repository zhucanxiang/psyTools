from my_easy_translate import EasyGoogleTranslate

class GoogleTranslate:
    def __init__(self):
        # easygoogletranslate: https://github.com/ahmeterenodaci/easygoogletranslate/tree/main
        self.en2cn_translator = translator = EasyGoogleTranslate(
                source_language='en',
                target_language='zh-CN',
                timeout=10
        )

    def translate(self, query):
        return self.en2cn_translator.translate(query)

if __name__ == '__main__':
    en2cn_translator = GoogleTranslate()
    query = "This is a example."
    print("origin: {}\ntarget: {}".format(query, en2cn_translator.translate(query)))