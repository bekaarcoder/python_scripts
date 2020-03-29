from translate import Translator

with open('text.txt', 'r') as my_file:
  file_txt = my_file.read()
  print(f"Actual Text -> {file_txt}")

  translator = Translator(to_lang='hi')
  translated_text = translator.translate(file_txt)
  print(f"Translated Text -> {translated_text}")

  with open('translated.txt', 'w', encoding="utf-8") as output:
    output.write(translated_text)
