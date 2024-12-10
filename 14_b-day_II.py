from sys import argv

while True:
    try:
        # Check if the correct number of arguments is provided
        if len(argv) != 2:
            raise ValueError("Invalid number of arguments.")

        # Unpack the arguments after verifying the correct length
        script, user_name = argv
        print(f"Привіт, {user_name}. Я {script} скрипт.")
        prompt = "> "

        print("Зараз я задам три питання.")

        # First Question
        print("Дощ чи сонце?")
        while True:
            rain_sun = input(prompt)
            if rain_sun in ("Дощ", "дощ", "Сонце", "сонце"):
                print("ok")
                break  # Exit the loop if input is valid
            else:
                print("Не розумію, спробуй ще раз: Дощ чи сонце?")

        # Second Question
        print("Спати чи їсти?")
        while True:
            sleep_eat = input(prompt)
            if sleep_eat in ("Спати", "спати", "Їсти", "їсти"):
                print("ok")
                break  # Exit the loop if input is valid
            else:
                print("Не розумію, спробуй ще раз: Спати чи їсти?")

        # Third Question
        print("Тобі добре зі мною?")
        while True:
            likes = input(prompt)
            if likes in ("Так", "так", "Ні", "ні"):
                print("ok")
                break  # Exit the loop if input is valid
            else:
                print("Не розумію, спробуй ще раз: Так чи Ні?")

        # Final Output
        print(f"Ok. Тож ти любиш {rain_sun}, радше {sleep_eat}, та кажеш '{likes}' на те, що мене так іноді хвилює.")
        break

    except ValueError:
        print("Помилка: Впиши ім'я поруч із назвою скрипта, будь ласка.")
        print("Приклад: python script_name.py UserName")
        break
