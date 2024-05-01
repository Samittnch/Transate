from googletrans import Translator

# ایجاد یک شیء مترجم
translator = Translator()

# ترجمه از فارسی به انگلیسی
result_en = translator.translate('سلام', src='fa', dest='en')
print(result_en.text) # نمایش متن ترجمه شده به انگلیسی

# ترجمه از انگلیسی به فارسی
result_fa = translator.translate('Hello', src='en', dest='fa')
print(result_fa.text) # نمایش متن ترجمه شده به فارسی

