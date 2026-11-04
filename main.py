# Очистка старых напоминаний при запуске
clean_expired_reminders()

print("====================================")
print("🤖 ГИБРИДНЫЙ ДЖАРВИС v54.0")
print("====================================")
print("Напишите 'справочник', чтобы увидеть все команды.")
print("Напишите 'выход', чтобы завершить работу.\n")

# Переменная для отслеживания времени
последний_ввод = time.time()

время_старта = None

while True:
    if time.time() - последний_ввод > 60:
        msg = random.choice(INITIATIVE_MESSAGES)
        print(f"\n\n🤖 Джарвис: {msg}")
        последний_ввод = time.time()

    try:
        user_input = input("> ").strip()
    except KeyboardInterrupt:
        print("\nЗавершение работы...")
        break

    # Сбрасываем таймер, так как ты что-то ввел
    последний_ввод = time.time()

    if not user_input:
        continue
    print(f"Вы: {user_input}")
    if user_input.lower() in ["выход", "exit"]:
        print_slow("Джарвис: До свидания, сэр.")
        break

    lower_input = user_input.lower()

    # --- ПЕРЕВОД ЧИСЕЛ ИЗ ОДНОЙ СИСТЕМЫ В ДРУГУЮ ---
    if "переведи" in lower_input or "в системе" in lower_input:
        # Ожидаем формат: "переведи 1010 из 2 в 10"
        parts = lower_input.split()

        if "из" in parts and "в" in parts:
            try:
                idx_from = parts.index("из")
                idx_to = parts.index("в")

                num_str = parts[idx_from - 1]
                from_base = int(parts[idx_from + 1])
                to_base = int(parts[idx_to + 1])

                if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):
                    print("Джарвис: Сэр, поддерживаются системы от 2 до 16.")
                    continue

                dec_val = base_to_dec(num_str, from_base)
                if dec_val is None:
                    print(
                        f"Джарвис: Сэр, число {num_str} не подходит для {from_base}-й системы."
                    )
                else:
                    result = dec_to_base(dec_val, to_base)
                    print(
                        f"Джарвис: Число {num_str} из {from_base}-й в {to_base}-ю систему: {result}"
                    )
            except (ValueError, IndexError):
                print("Джарвис: Сэр, используйте формат: 'переведи 1010 из 2 в 10'")
            continue

    # --- ВЫЧИСЛЕНИЯ В СИСТЕМАХ СЧИСЛЕНИЯ ---
    if "посчитай" in lower_input:
        text = lower_input.replace("посчитай", "").strip()

        try:
            base = 10
            if " в " in text:
                expr, base_str = text.rsplit(" в ", 1)
                base = int(base_str)
            else:
                expr = text

            if not (2 <= base <= 16):
                print("Джарвис: Сэр, система счисления должна быть от 2 до 16.")
                continue

            if "+" in expr:
                num1_str, num2_str = expr.split("+")
                op = "+"
            elif "-" in expr:
                num1_str, num2_str = expr.split("-")
                op = "-"
            elif "*" in expr:
                num1_str, num2_str = expr.split("*")
                op = "*"
            elif "/" in expr:
                num1_str, num2_str = expr.split("/")
                op = "/"
            else:
                print("Джарвис: Сэр, я не нашел знак действия (+, -, *, /).")
                continue

            num1 = base_to_dec(num1_str.strip(), base)
            num2 = base_to_dec(num2_str.strip(), base)

            if num1 is not None and num2 is not None:
                if op == "+":
                    res = num1 + num2
                elif op == "-":
                    res = num1 - num2
                elif op == "*":
                    res = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        print("Джарвис: Сэр, на ноль делить нельзя.")
                        continue
                    res = num1 / num2

                res_base = dec_to_base(int(res), base)
                print(
                    f"Джарвис: {num1_str.strip()} {op} {num2_str.strip()} в {base}-й системе = {res_base} (в десятичной: {res})"
                )
            else:
                print(
                    f"Джарвис: Сэр, одно из чисел недопустимо для {base}-й системы. Проверьте цифры (0-{base-1})."
                )

        except Exception as e:
            print(f"Джарвис: Сэр, ошибка вычисления: {e}")
            print("Используйте формат: 'посчитай 1010 + 111 в 2'")
        continue

    # 1. СПРАВОЧНИК
    if "справочник" in lower_input:
        print("\n" + "=" * 50)
        print("📖 СПРАВОЧНИК КОМАНД ДЖАРВИСА v54.0")
        print("=" * 50)

        print("\n[БАЗОВЫЕ КОМАНДЫ]:")
        print("  справочник - этот список")
        print("  покажи базу - выводит все выученные фразы")
        print("  редактировать <слово> <ответ> - меняет ответ")
        print("  удалить <слово> - удаляет фразу из памяти")
        print("  пошути - рассказать случайную шутку")
        print("  расскажи факт - рассказать случайный факт")

        print("\n[ПРИЛОЖЕНИЯ И САЙТЫ]:")
        print("  открой <сайт> - ютуб, яндекс, вк, гитхаб, википедия, стим")
        print(
            "  <название приложения> - камера, телефон, фото, музыка, файлы, заметки, карты, впн, календарь"
        )
        print("  поищи <запрос> - ищет в Яндексе")
        print("  <ссылка> - если написать site.com или site.ru, Джарвис откроет его")

        print("\n[ИНСТРУМЕНТЫ]:")
        print("  посчитай <число> <операция> <число> - калькулятор")
        print("  2+2 - умный калькулятор (без пробелов)")
        print("  погода - прогноз погоды")
        print("  курс валют - курс доллара и евро")
        print("  придумай пароль - генерирует надежный пароль")
        print("  кубик / монетка - генератор случайных чисел")
        print(
            "  калькулятор физики - 7 формул (Ньютон, Ом, энергия, плотность, давление, Гук, мощность)"
        )
        print("  засекай / стоп - запускает и останавливает секундомер")
        print("  переведи <число> из <X> в <Y> - перевод между системами счисления")
        print("  посчитай <число> <+-> <число> в <X> - вычисления в разных системах")
        print(
            "  выбери число <от X до Y> - выбирает случайное число (например, 'выбери число от 1 до 10')"
        )
        print(
            "  напомни <текст> к <ДД.ММ.ГГГГ> <ЧЧ:ММ> - создать напоминание (например: напомни купить хлеб к 20.11.2026 13:50)"
        )
        print("  переведи слово <текст> - открывает переводчик Google")

        print("\n[ДИАГНОСТИКА]:")
        print("  тест памяти - проверяет оперативную память")
        print("  проверь файлы - показывает размеры всех файлов")
        print("  загрузка цп - имитирует проверку процессора и температуры")
        print("  дерево файлов - показывает структуру памяти")

        print("\n[ШИФРОВАНИЕ]:")
        print("  секретный код <текст> - шифрует текст в Base64")
        print("  расшифруй код <код> - расшифровывает Base64")
        print("  зашифруй текст <текст> - переводит текст в любую систему (2-16)")
        print(
            "  расшифруй текст <система> <код> - переводит код обратно в текст (например: расшифруй текст 2 1000001)"
        )

        print("\n[РАБОТА С ФАЙЛАМИ]:")
        print("  список файлов - показывает файлы в папке")
        print("  прочитай <файл> - читает текстовый файл")
        print("  создай файл <имя> <текст> - создает файл")
        print("  удали файл <имя> - безопасно удаляет файл из папки")

        print("\n[ПРОТОКОЛЫ]:")
        print("  протокол резервное копирование - создает бэкап памяти")
        print("  протокол диагностика - проверяет файлы")
        print("  протокол таймер <секунды> - запускает таймер")
        print("  протокол ночной страж - сохраняет память и выключается")
        print("  протокол костюм - запускает приложение через ярлык")
        print("  протокол эвакуация - сохраняет память и экстренно выключается")
        print("  протокол автопилот - открывает календарь, погоду и курс валют")
        print("  протокол аудит - проверяет наличие файлов")
        print("  протокол щит - создает теневые копии файлов памяти")
        print("  протокол очистка - визуально очищает терминал")
        print("  протокол домой - завершает работу программы")
        print(
            "  протокол рецепты - список химических экспериментов (от безопасных до безумных)"
        )
        print("  протокол юбилей - праздничный салют")

        print("\n[ПРИКОЛЫ]:")
        print("  активируй оружие омега - удаляет цель из всех вселенных")
        print("  протокол левиафан - запускает ракету 'левиафан'")
        print("  протокол невидимка - скрывает следы вашего присутствия")
        print("  протокол варп - разгоняет ядро Джарвиса до скорости света")
        print("  протокол тостер - запускает процесс подгорания тостов")
        print("  протокол матрица - выводит цифровой дождь на экран")
        print("  протокол самоуничтожение - запускает обратный отсчет (шутка)")
        print("  протокол дезинфекция - очищает систему от вирусов и крошек")
        print("  протокол хаос - вносит случайный беспорядок в систему")
        print("  протокол сникерс - ищет ближайший Сникерс")
        print("  протокол интел - имитирует перегрев процессора до 100 градусов")
        print("  протокол юбилей - празднует наше достижение")
        print("  антигравитация - открывает легендарный комикс Python (XKCD)")

        print("\n[ИГРЫ]:")
        print("  угадай число - сыграть в угадайку")
        print("  пенальти - сыграть в футбол")
        print("  крестики-нолики - сыграть против Джарвиса")

        print("\n[НАУКА]:")
        print("  расскажи историю - краткие факты про историю")
        print("  расскажи географию - краткие факты по географии")
        print("  расскажи физику - базовые факты по физике")

        print("\n" + "=" * 50)
        print("\n  выход - завершить работу")
        print("=" * 50 + "\n")
        continue

    # 2. Показать базу
    if "покажи базу" in lower_input:
        print("\nВывожу базу данных...")
        print("-" * 50)
        for k, v in TEMPLATES.items():
            print(f'    "{k}": "{v}",')
        print("-" * 50 + "\n")
        continue

    # 3. РЕДАКТИРОВАТЬ ДИАЛОГ
    if lower_input.startswith("редактировать "):
        parts = user_input[13:].strip().split(" ", 1)
        if len(parts) < 2:
            print(
                "Джарвис: Сэр, используйте формат: редактировать <слово> <новый ответ>"
            )
            continue
        key_to_edit = parts[0].lower().strip()
        new_response = parts[1]
        if key_to_edit in TEMPLATES:
            old_response = TEMPLATES[key_to_edit]
            TEMPLATES[key_to_edit] = new_response
            memory = load_json(MEMORY_FILE)
            memory[key_to_edit] = new_response
            save_json(MEMORY_FILE, memory)
            print(f"✅ Отредактировано! Слово: '{key_to_edit}'")
            print(f"   Было: '{old_response}'")
            print(f"   Стало: '{new_response}'")
        else:
            print(f"Джарвис: Сэр, я не нашел в базе слово '{key_to_edit}'.")
        continue

    # 4. УДАЛИТЬ ДИАЛОГ
    if lower_input.startswith("удалить "):
        key_to_delete = user_input[8:].strip().lower()
        if not key_to_delete:
            print("Джарвис: Сэр, укажите, что именно нужно удалить.")
            continue
        found = False
        if key_to_delete in TEMPLATES:
            del TEMPLATES[key_to_delete]
            found = True
        memory = load_json(MEMORY_FILE)
        if key_to_delete in memory:
            del memory[key_to_delete]
            save_json(MEMORY_FILE, memory)
            found = True
        if found:
            print(f"🗑️ Фраза '{key_to_delete}' полностью удалена из памяти Джарвиса.")
        else:
            print(f"Джарвис: Сэр, я не нашел слово '{key_to_delete}' в базе.")
        continue

    # --- КАЛЬКУЛЯТОР ФИЗИКИ ---
    if "калькулятор физики" in lower_input or "физика" in lower_input:
        physics_calculator()
        continue

    # 5. ОТКРЫТИЕ ПРИЛОЖЕНИЙ (Ярлыки)
    apps = [
        "камера",
        "калькулятор",
        "настройки",
        "телефон",
        "фото",
        "файлы",
        "музыка",
        "переводчик",
        "ии",
        "макс",
        "заметки",
        "обсидиан",
        "карты",
        "впн",
        "календарь",
    ]
    for app in apps:
        if app in lower_input and not lower_input.startswith("открой"):
            print(f"Джарвис: Запускаю {app} через Команды, сэр...")
            webbrowser.open(f"shortcuts://run-shortcut?name={app}")
            break
    else:
        pass

    # 6. ОТКРЫТИЕ САЙТОВ
    if lower_input.startswith("открой"):
        site = lower_input[6:].strip()
        sites = {
            "ютуб": "ютуб",
            "youtube": "ютуб",
            "яндекс": "яндекс",
            "yandex": "яндекс",
            "вк": "вк",
            "вконтакте": "вк",
            "гитхаб": "гитхаб",
            "github": "гитхаб",
            "википедия": "википедия",
            "вики": "википедия",
            "стим": "стим",
            "steam": "стим",
        }
        found = False
        for key, shortcut_name in sites.items():
            if key in site:
                print(f"Джарвис: Открываю {key.capitalize()} через Команды, сэр...")
                webbrowser.open(f"shortcuts://run-shortcut?name={shortcut_name}")
                found = True
                break
        if not found:
            print(f"Джарвис: Сэр, я не знаю, как открыть '{site}'.")
        continue

    # --- ОТКРЫТИЕ САЙТА ПО ПРЯМОЙ ССЫЛКЕ ---
    if re.match(
        r"^[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}$", lower_input
    ) and not lower_input.startswith("поищи"):
        url = user_input if user_input.startswith("http") else f"https://{user_input}"
        print(f"Джарвис: Обнаружена ссылка, сэр. Открываю {url}...")
        webbrowser.open(url)
        continue

    # 7. ПОИСК В ЯНДЕКСЕ
    if lower_input.startswith("поищи "):
        query = user_input[6:].strip()
        if query:
            encoded_query = quote(query)
            url = f"https://yandex.ru/search/?text={encoded_query}"
            print(f"Джарвис: Ищу в Яндексе '{query}', сэр...")
            webbrowser.open(url)
        else:
            print("Джарвис: Сэр, вы не сказали, что искать.")
        continue

    # 8. Калькулятор
    if re.match(r"^\s*-?\d+(\.\d+)?\s*[\+\-\*\/]\s*-?\d+(\.\d+)?\s*$", user_input):
        expr = user_input.replace(",", ".")
        res = safe_calculator(expr)
        if isinstance(res, str):
            print(f"Джарвис: {res}")
        else:
            print(f"Джарвис: Результат: {res}")
        continue

    # 9. Погода
    if "погода" in lower_input:
        print("Джарвис: Открываю прогноз погоды, сэр...")
        webbrowser.open("https://yandex.ru/pogoda")
        continue

    # 10. Курс валют
    if (
        "курс валют" in lower_input
        or "курс доллара" in lower_input
        or "курс евро" in lower_input
    ):
        print("Джарвис: Открываю актуальные курсы валют, сэр...")
        webbrowser.open("https://www.cbr.ru/currency_base/daily/")
        continue

    # 11. СПИСОК ФАЙЛОВ
    if "список файлов" in lower_input:
        print("Джарвис: Сканирую папку Documents, сэр...")
        try:
            files = os.listdir(DOCUMENTS)
            if not files:
                print("  Папка пуста.")
            else:
                print("  Найдены следующие файлы:")
                for f in files:
                    size = os.path.getsize(os.path.join(DOCUMENTS, f))
                    print(f"  📄 {f} ({size} байт)")
        except Exception as e:
            print(f"  ⚠️ Ошибка при чтении списка файлов: {e}")
        continue

    # 12. ПРОЧИТАТЬ ФАЙЛ
    if lower_input.startswith("прочитай "):
        filename = user_input[8:].strip()
        if "/" in filename or ".." in filename:
            print("Джарвис: Сэр, я могу читать только файлы из моей папки.")
            continue
        filepath = os.path.join(DOCUMENTS, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"Джарвис: Содержимое файла '{filename}':")
                print("-" * 30)
                print(content[:500])
                if len(content) > 500:
                    print("... (файл слишком длинный)")
                print("-" * 30)
            except Exception as e:
                print(f"Джарвис: Не удалось прочитать файл. Ошибка: {e}")
        else:
            print(f"Джарвис: Файл '{filename}' не найден.")
        continue

    # 13. СОЗДАТЬ ФАЙЛ
    if lower_input.startswith("создай файл "):
        parts = user_input[11:].strip().split(" ", 1)
        if len(parts) < 2:
            print("Джарвис: Сэр, используйте формат: создай файл <имя> <текст>")
            continue
        filename = parts[0]
        text = parts[1]
        if "/" in filename or ".." in filename:
            print("Джарвис: Сэр, недопустимое имя файла.")
            continue
        filepath = os.path.join(DOCUMENTS, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Джарвис: Файл '{filename}' успешно создан и сохранен.")
        except Exception as e:
            print(f"Джарвис: Не удалось создать файл. Ошибка: {e}")
        continue

    # 14. Удалить файл
    if lower_input.startswith("удали файл "):
        filename = user_input[11:].strip()
        if not filename:
            print("Джарвис: Сэр, укажите имя файла.")
            continue

        print(f"Джарвис: Попытка удалить файл '{filename}'...")
        time.sleep(0.5)
        result = delete_file_safe(filename)
        print(f"Джарвис: {result}")
        continue