from my_easy_translate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='en',
    target_language='zh-CN',
    timeout=10
)
result = translator.translate('This is an example.')
print(result)