from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# Функция для получения случайного английского слова и его определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Функция для перевода текста с английского на русский
def translate_to_russian(text):
    try:
        translator = Translator()
        translation = translator.translate(text, src="en", dest="ru")
        return translation.text
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        print("Возвращаю оригинальный текст.")
        return text

# Основная игра
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить данные. Попробуйте позже.")
            break

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Перевод слова и его определения на русский
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        print(f"Значение слова: {russian_definition}")
        user_input = input("Что это за слово? ").strip()

        if user_input.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово было: {russian_word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
word_game()
