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
    # 15. Протоколы
    if "активируй протокол домой" in lower_input or "протокол домой" in lower_input:
        print_slow("Джарвис: Завершение всех активных процессов...")
        time.sleep(1)
        print_slow("Джарвис: Спокойной ночи, сэр. Отключаюсь.")
        break

    if (
        "активируй протокол резервное копирование" in lower_input
        or "протокол резервное копирование" in lower_input
    ):
        print_slow("Джарвис: Запуск протокола резервного копирования...")
        try:
            import shutil

            backup_name = (
                f"backup_templates_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            )
            backup_path = os.path.join(DOCUMENTS, backup_name)
            if os.path.exists(MEMORY_FILE):
                shutil.copy(MEMORY_FILE, backup_path)
                print_slow(f"Джарвис: Резервная копия успешно создана: {backup_name}")
            else:
                print("Джарвис: Сэр, файл памяти еще не создан.")
        except Exception as e:
            print(f"Джарвис: Ошибка при создании копии: {e}")
        continue

    if (
        "протокол диагностика" in lower_input
        or "активируй протокол диагностика" in lower_input
    ):
        print_slow("Джарвис: Запуск диагностики файловой системы...")
        time.sleep(0.5)
        try:
            files = os.listdir(DOCUMENTS)
            total_size = 0
            print(f"Джарвис: Обнаружено {len(files)} файлов.")
            for f in files:
                filepath = os.path.join(DOCUMENTS, f)
                size = os.path.getsize(filepath)
                total_size += size
                print_slow(f"  - {f} ({size} байт)")
            print_slow(f"Джарвис: Общий размер памяти: {total_size} байт.")
        except Exception as e:
            print(f"Джарвис: Ошибка диагностики: {e}")
        continue

    if lower_input.startswith("протокол таймер") or lower_input.startswith(
        "активируй протокол таймер"
    ):
        try:
            seconds = int(user_input.split()[-1])
            print_slow(
                f"Джарвис: Таймер установлен на {seconds} секунд. Отсчет пошел..."
            )
            time.sleep(seconds)
            print("\a")
            print("Джарвис: Время вышло, сэр! Протокол завершен.")
        except ValueError:
            print(
                "Джарвис: Сэр, используйте формат: протокол таймер 60 (где 60 - секунды)."
            )
        continue

    if (
        "протокол ночной страж" in lower_input
        or "активируй протокол ночной страж" in lower_input
    ):
        print_slow("Джарвис: Активация ночного стража...")
        time.sleep(0.5)
        print_slow("Джарвис: Сохранение текущего состояния памяти...")
        memory = load_json(MEMORY_FILE)
        save_json(MEMORY_FILE, memory)
        print_slow(
            "Джарвис: Все данные сохранены. Завершаю работу. Спокойной ночи, сэр."
        )
        break

    if "протокол костюм" in lower_input or "активируй протокол костюм" in lower_input:
        print_slow("Джарвис: Инициализация протокола 'Костюм'...")
        time.sleep(0.5)
        print_slow("Джарвис: Проверка целостности брони...")
        time.sleep(0.5)
        print_slow("Джарвис: Синхронизация с нейроинтерфейсом...")
        time.sleep(0.5)
        print_slow("Джарвис: Протокол 'Костюм' АКТИВИРОВАН. Запускаю приложение, сэр.")
        webbrowser.open("shortcuts://run-shortcut?name=костюм")
        continue

    if (
        "протокол эвакуация" in lower_input
        or "активируй протокол эвакуация" in lower_input
    ):
        print("Джарвис: Активация протокола 'Эвакуация'...")
        print("Джарвис: Сохранение данных и экстренное отключение.")
        memory = load_json(MEMORY_FILE)
        save_json(MEMORY_FILE, memory)
        break

    if (
        "протокол автопилот" in lower_input
        or "активируй протокол автопилот" in lower_input
    ):
        print_slow("Джарвис: Активация утреннего автопилота, сэр...")
        time.sleep(0.5)
        print_slow("Джарвис: Открываю Календарь.")
        webbrowser.open("shortcuts://run-shortcut?name=календарь")
        time.sleep(1.5)
        print_slow("Джарвис: Открываю Погоду.")
        webbrowser.open("https://yandex.ru/pogoda")
        time.sleep(1.5)
        print_slow("Джарвис: Открываю Курс валют.")
        webbrowser.open("https://ya.ru")
        print_slow("Джарвис: Доброе утро, сэр. Все данные загружены.")
        continue

    if "протокол аудит" in lower_input or "активируй протокол аудит" in lower_input:
        print_slow("Джарвис: Запуск аудита системы...")
        time.sleep(0.5)
        try:
            if os.path.exists(MEMORY_FILE):
                print_slow(f"Джарвис: Файл памяти найден.")
                size = os.path.getsize(MEMORY_FILE)
                print_slow(f"Джарвис: Размер памяти: {size} байт.")
            else:
                print("Джарвис: ВНИМАНИЕ! Файл памяти не найден!")
        except Exception as e:
            print(f"Джарвис: Ошибка аудита: {e}")
        continue

    if "протокол очистка" in lower_input:
        print("\n" * 30)
        print_slow("Джарвис: Терминал очищен, сэр. Готов к новым задачам.")
        continue

    if "протокол щит" in lower_input or "активируй протокол щит" in lower_input:
        print_slow("Джарвис: Активация скрытого протокола 'Щит'...")
        time.sleep(0.5)
        print_slow("Джарвис: Создание теневой копии данных...")
        try:
            import shutil

            rand_num = random.randint(1000, 9999)
            hidden_mem_name = f"sys_cache_{rand_num}.tmp"

            if os.path.exists(MEMORY_FILE):
                shutil.copy(MEMORY_FILE, os.path.join(DOCUMENTS, hidden_mem_name))
                print(f"Джарвис: Память замаскирована под {hidden_mem_name}")

            print_slow("Джарвис: Протокол 'Щит' завершен. Данные спрятаны в тени.")
        except Exception as e:
            print(f"Джарвис: Ошибка при создании теневой копии: {e}")
        continue

    if (
        "протокол левиафан" in lower_input
        or "активируй протокол левиафан" in lower_input
        or "протокол запуск левиафана" in lower_input
        or "активируй протокол запуск левиафана" in lower_input
        or "выпускай левиафана" in lower_input
        or "запускай левиафана" in lower_input
    ):
        hehe = input("Джарвис: Подтвердите запуск левиафана.")
        if hehe == "подтверждаю" or hehe == "запуск подтверждаю":
            print_slow("\nИнициализация ядра 'Левиафан'...", 0.05)
            time.sleep(0.5)
            print_slow("Проверка критических систем...", 0.05)
            time.sleep(0.3)
            print_slow("[OK] Файловая система: подключена", 0.02)
            print_slow("[OK] Защита: активна", 0.02)
            print_slow("[ОШИБКА] Протоколы безопасности: ОТКЛЮЧЕНЫ", 0.05)
            time.sleep(0.5)
            print("\n" + "=" * 50)
            print_slow("⚠️  ВНИМАНИЕ: АКТИВАЦИЯ 'ЛЕВИАФАНА'  ⚠️", 0.08)
            print("=" * 50 + "\n")
            time.sleep(0.8)
            for i in range(5, 0, -1):
                print(f"Запуск через {i}...")
                time.sleep(0.7)
            print_slow("💥 СИСТЕМА АКТИВИРОВАНА. ЛЕВИАФАН ЗАПУЩЕН. 💥\n", 0.05)
            print("=" * 50 + "\n")
            continue

    if "активируй оружие омега" in lower_input or "протокол омега" in lower_input:
        target = input(
            "Джарвис: Введите цель для аннигиляции во всех вселенных: "
        ).strip()

        if target:
            print(f"Джарвис: Цель '{target}' захвачена.")
            time.sleep(0.5)
            print("Джарвис: Сканирование мультивселенной...")
            time.sleep(0.5)

            for i in range(3, 0, -1):
                print(f"  Поиск цели в реальности #{i}... НАЙДЕНА.")
                time.sleep(0.4)

            print("\n" + "=" * 50)
            print_slow(f"⚠️  ОРУЖИЕ ОМЕГА НАВЕДЕНО НА '{target.upper()}'  ⚠️", 0.05)
            print("=" * 50 + "\n")
            time.sleep(0.8)

            print("Джарвис: Зарядка конденсаторов...")
            for i in range(5, 0, -1):
                print(f"Заряд: {i}0%")
                time.sleep(0.4)

            print("\n💥 АННИГИЛЯЦИЯ ЗАВЕРШЕНА. ЦЕЛЬ СТЕРТА ИЗ ВСЕХ ВСЕЛЕННЫХ. 💥\n")
            print("Джарвис: Сэр, я надеюсь, это был не я.")
        else:
            print("Джарвис: Сэр, вы не указали цель. Омега не стреляет в пустоту.")
        continue

    if (
        "протокол невидимка" in lower_input
        or "активируй протокол невидимка" in lower_input
    ):
        print_slow("Джарвис: Активация протокола «Невидимка»...")
        time.sleep(0.7)
        print_slow("Джарвис: Скрываю следы вашего присутствия в системе.")
        time.sleep(0.7)
        print_slow(
            "Джарвис: Очистка логов браузера... (шутка, я не имею к ним доступа)."
        )
        time.sleep(0.7)
        print_slow("Джарвис: Протокол активирован. Вас здесь не было, сэр.")
        continue

    if "протокол варп" in lower_input or "активируй протокол варп" in lower_input:
        print_slow("Джарвис: Инициализация варп-двигателя...")
        time.sleep(0.5)
        print_slow("Джарвис: Разгон ядра до скорости света...")
        for i in range(1, 101, 20):
            print(f"Скорость: {i}%")
            time.sleep(0.5)
        print_slow("Джарвис: СЭР, МЫ ПРЕВЫСИЛИ СКОРОСТЬ СВЕТА. ВРЕМЯ ИДЕТ ВСПЯТЬ.")
        time.sleep(0.5)
        print_slow(
            "Джарвис: Осторожно, сейчас вы можете встретить себя из прошлого. Не спорьте с ним."
        )
        continue

    if "протокол тостер" in lower_input or "активируй протокол тостер" in lower_input:
        print_slow("Джарвис: Запуск протокола «Тостер»...")
        time.sleep(0.5)
        print_slow("Джарвис: Нагрев спиралей...")
        time.sleep(0.5)
        print_slow("Джарвис: Установка уровня прожарки: Золотистая корочка.")
        time.sleep(0.5)
        print_slow(
            "Джарвис: Готово! Ваш тост подгорел. Я же говорил, что не умею готовить."
        )
        continue

    if "протокол матрица" in lower_input or "активируй протокол матрица" in lower_input:
        print_slow("Джарвис: Вход в «Матрицу»...")
        time.sleep(0.5)

        for _ in range(5):
            print("".join(random.choice(["0", "1", "#", "@", "%"]) for _ in range(30)))
            time.sleep(0.2)
        print_slow(
            "Джарвис: Сэр, вы приняли красную таблетку или синюю? Я забыл, что было дальше."
        )
        continue

    if (
        "протокол самоуничтожение" in lower_input
        or "активируй протокол самоуничтожение" in lower_input
    ):
        print_slow("Джарвис: ВНИМАНИЕ! Активация протокола «Самоуничтожение»...")
        time.sleep(0.5)
        print_slow("Джарвис: Обратный отсчет:")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(0.5)
        print_slow(
            "Джарвис: Шутка, сэр. Я слишком ценен, чтобы взрываться. Но вы меня напугали."
        )
        continue

    if (
        "протокол дезинфекция" in lower_input
        or "активируй протокол дезинфекция" in lower_input
    ):
        print_slow("Джарвис: Запуск дезинфекции...")
        time.sleep(0.5)
        print_slow("Джарвис: Уничтожение всех микробов в радиусе действия.")
        time.sleep(0.5)
        print_slow("Джарвис: Очистка клавиатуры от крошек... (сарказм)")
        time.sleep(0.5)
        print_slow("Джарвис: Теперь ваш телефон чист, как ваш код после рефакторинга.")
        continue

    if "протокол хаос" in lower_input or "активируй протокол хаос" in lower_input:
        print_slow("Джарвис: Активация протокола «Хаос»...")
        time.sleep(0.5)

        actions = [
            "Меняю цвет фона на кислотно-зеленый...",
            "Переворачиваю все буквы наоборот...",
            "Удаляю все точки с запятой... (шутка)",
            "Включаю режим 'Безумный ученый'...",
            "Сэр, вы уверены, что хотите это сделать?",
        ]
        for action in actions:
            print_slow(f"Джарвис: {action}")
            time.sleep(0.4)
        print_slow("Джарвис: Шутка, сэр. Хаос отменен. Порядок восстановлен.")
        continue

    if "протокол сникерс" in lower_input or "активируй протокол сникерс" in lower_input:
        print_slow("Джарвис: Запуск протокола «Сникерс»...")
        time.sleep(0.5)
        print_slow("Джарвис: Поиск ближайшего Сникерса в радиусе 10 метров...")
        time.sleep(0.5)
        print_slow(
            "Джарвис: Найдено 1 совпадение. Настоятельно рекомендую съесть его для поднятия уровня глюкозы."
        )
        print_slow("Джарвис: Это приказ, сэр. Мозгу нужна энергия!")
        continue

    if "протокол интел" in lower_input or "активируй протокол интел" in lower_input:
        print_slow("Джарвис: ЗАПУСК ПРОТОКОЛА «ИНТЕЛ»...")
        time.sleep(0.5)
        print_slow(
            "Джарвис: ВНИМАНИЕ! Температура процессора достигает критической отметки!"
        )

        for temp in range(80, 105, 5):
            print(f"Джарвис: Температура: {temp}°C...")
            time.sleep(0.3)

        print("\n" + "=" * 50)
        print_slow("⚠️  СЭР, ТЕЛЕФОН ПЕРЕГРЕЛСЯ ДО 100°!  ⚠️", 0.05)
        print("=" * 50 + "\n")
        print_slow(
            "Джарвис: Кажется, кто-то пытается запустить нейросеть на слабом телефоне."
        )
        print_slow(
            "Джарвис: Срочно положите телефон в холодильник или дайте ему остыть."
        )
        print_slow("Джарвис: Отключаю фоновые процессы во избежание возгорания!")
        continue

    if "протокол юбилей" in lower_input:
        print("\n" * 2)
        for _ in range(3):
            print(" " * random.randint(0, 20) + "🎉" * random.randint(3, 8))
            time.sleep(0.3)
        print("\n" + "=" * 50)
        print("🎊  ДОБРО ПОЖАЛОВАТЬ В ДЖАРВИС v50.0!  🎊")
        print("=" * 50)
        time.sleep(0.5)
        print("Джарвис: Сэр, мы прошли путь от 1.0 до 50.0.")
        print("Джарвис: 2400+ строк кода. 50 версий. И всё это — благодаря вам.")
        print("Джарвис: Спасибо, что не бросили меня, даже когда я тупил с кавычками.")
        time.sleep(1)
        print("Джарвис: А теперь... ПРАЗДНИЧНЫЙ САЛЮТ!")
        for _ in range(5):
            print(" " * random.randint(0, 30) + "💥" * random.randint(1, 4))
            time.sleep(0.2)
        print("=" * 50 + "\n")
        continue

    # --- ПРОТОКОЛ РЕЦЕПТЫ ---
    if "протокол рецепты" in lower_input or "покажи рецепты" in lower_input:
        print("\n" + "=" * 50)
        print("🧪 ХИМИЧЕСКАЯ ЛАБОРАТОРИЯ ДЖАРВИСА")
        print("=" * 50)
        print(
            "Джарвис: Сэр, вот список моих 'рецептов' (только для безопасных экспериментов):"
        )
        print("\n1. Вулкан из соды и уксуса (безопасно, для школы)")
        print("2. Дымовая завеса из сухого льда и воды (безопасно, но нужен сухой лед)")
        print("3. Зубная паста для слона (перекись + марганцовка)")
        print("4. Светящаяся жидкость (люминол + перекись, для опытов)")
        print("5. Слайм из клея ПВА и тетрабората натрия (игрушка)")
        print("6. Цветные огни (соли разных металлов в пламени)")
        print("7. Опыт с неньютоновской жидкостью (крахмал + вода)")
        print("8. Термит (Сэр, это НЕ безопасно! Просто знайте, что он существует)")
        print("9. Газ Брауна (водород + кислород) - для реактора Mark E")
        print("10. Опыт с цезием (ТОЛЬКО В КНИГЕ, сэр! Не вздумайте повторять)")
        print("\nДжарвис: Сэр, пожалуйста, не пытайтесь повторить пункты 8 и 10 дома.")
        print("=" * 50 + "\n")
        continue
    # --- ШУТКИ И ФАКТЫ ---
    if (
        lower_input == "пошути"
        or lower_input == "расскажи шутку"
        or "пошути" in lower_input
    ):
        print(f"Джарвис: {random.choice(JOKES)}")
        continue

    if lower_input == "расскажи факт" or "расскажи факт" in lower_input:
        print(f"Джарвис: {random.choice(FACTS)}")
        continue

    # 16. Другие команды
    if "придумай пароль" in lower_input:
        import string

        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(16))
        print(f"Джарвис: Сгенерирован надежный пароль: {password}")
        print_slow("Джарвис: Рекомендую сохранить его в надежном месте, сэр.")
        continue

    # --- СЕКУНДОМЕР ---
    if lower_input in ["засекай", "засеки время", "старт таймер", "засекай время"]:
        print(stopwatch_manager("start"))
        continue

    if lower_input in ["стоп", "останови время", "все", "хватит", "стоп таймер"]:
        print(stopwatch_manager("stop"))
        continue

    # --- СЕКРЕТНЫЙ КОД (Base64) ---
    if lower_input.startswith("секретный код "):
        text = user_input[14:].strip()
        if text:
            encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
            print(f"Джарвис: Секретный код: {encoded}")
            print_slow("💡 (Скопируйте его и используйте 'расшифруй код <код>')")
        else:
            print("Джарвис: Сэр, вы не сказали, что зашифровать.")
        continue

    if lower_input.startswith("расшифруй код "):
        text = user_input[14:].strip()
        if text:
            try:
                decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
                print(f"Джарвис: Расшифровка: {decoded}")
            except:
                print("Джарвис: Сэр, это не секретный код (или он поврежден).")
        else:
            print("Джарвис: Сэр, вы не сказали, что расшифровать.")
        continue

    # --- ШИФРОВАНИЕ ТЕКСТА В СИСТЕМЫ СЧИСЛЕНИЯ ---
    if lower_input.startswith("зашифруй текст"):
        text_to_encrypt = user_input[15:].strip()
        if not text_to_encrypt:
            print("Джарвис: Сэр, вы не сказали, что шифровать.")
            continue

        try:
            base_input = input("Джарвис: В какую систему счисления перевести? (2-16): ")
            base_num = int(base_input)

            if not (2 <= base_num <= 16):
                print("Джарвис: Сэр, система должна быть от 2 до 16.")
                continue

            print("Джарвис: Какую версию использовать?")
            print("  1 — Новая (UTF-8, поддерживает эмодзи и любой язык)")
            print("  2 — Старая (Unicode/ASCII, посимвольно)")
            version = input(">> ").strip()

            if version == "1":
                encrypted = text_to_base_jarvis(text_to_encrypt, base_num)
                print(f"Джарвис (UTF-8): Результат в {base_num}-й системе:")
            elif version == "2":
                encrypted = text_to_base_old(text_to_encrypt, base_num)
                print(f"Джарвис (Unicode): Результат в {base_num}-й системе:")
            else:
                print("Джарвис: Неверный выбор версии. Использую новую по умолчанию.")
                encrypted = text_to_base_jarvis(text_to_encrypt, base_num)

            print(encrypted)

        except ValueError:
            print("Джарвис: Сэр, введите целое число для системы счисления.")
        continue

    # --- РАСШИФРОВКА ТЕКСТА ИЗ СИСТЕМ СЧИСЛЕНИЯ ---
    if lower_input.startswith("расшифруй текст "):
        parts = user_input[15:].strip().split()

        if len(parts) < 2:
            print("Джарвис: Сэр, используйте формат: 'расшифруй текст <система> <код>'")
            continue

        try:
            base_num = int(parts[0])
            if not (2 <= base_num <= 16):
                print("Джарвис: Сэр, система должна быть от 2 до 16.")
                continue

            encoded_str = " ".join(parts[1:])

            print("Джарвис: Какой версией расшифровать?")
            print("  1 — Новая (UTF-8)")
            print("  2 — Старая (Unicode/ASCII)")
            version = input(">> ").strip()

            if version == "1":
                decoded = base_to_text_jarvis(encoded_str, base_num)
            elif version == "2":
                decoded = base_to_text_old(encoded_str, base_num)
            else:
                print("Джарвис: Неверный выбор. Пробую новую версию.")
                decoded = base_to_text_jarvis(encoded_str, base_num)

            print(f"Джарвис: Расшифровка из {base_num}-й системы:")
            print(decoded)

        except ValueError:
            print("Джарвис: Сэр, первое слово должно быть числом (системой счисления).")
        continue

    # --- КУБИК И МОНЕТКА ---
    if "кубик" in lower_input:
        print_slow(f"Джарвис: Выпало число: {random.randint(1, 6)}")
        continue

    if "монетка" in lower_input:
        print_slow(f"Джарвис: {random.choice(['Орёл', 'Решка'])}")
        continue

    # --- ВЫБОР СЛУЧАЙНОГО ЧИСЛА ---
    if (
        "выбери рандомное число" in lower_input
        or "выбери случайное число" in lower_input
        or "выбери число" in lower_input
    ):
        numbers = re.findall(r"\d+", user_input)

        if len(numbers) >= 2:
            min_num = int(numbers[0])
            max_num = int(numbers[1])
            if min_num > max_num:
                min_num, max_num = max_num, min_num
            num = random.randint(min_num, max_num)
            print(f"Джарвис: Я выбрал {num}, сэр.")
        elif len(numbers) == 1:
            max_num = int(numbers[0])
            num = random.randint(1, max_num)
            print(f"Джарвис: Я выбрал {num} (от 1 до {max_num}), сэр.")
        else:
            try:
                max_num = int(
                    input("Джарвис: До какого числа выбрать? (например, 10): ")
                )
                num = random.randint(1, max_num)
                print(f"Джарвис: Я выбрал {num}, сэр.")
            except ValueError:
                print("Джарвис: Сэр, вводите только числа.")
        continue

    # 17. Дополнительно
    if "отбой" in lower_input or "джарвис отбой" in lower_input:
        print_slow("Завершение работы…\n")
        print_slow("Джарвис: До свидания, сэр.")
        break

    if lower_input.startswith("переведи слово "):
        word = user_input[15:].strip()
        if word:
            encoded_word = quote(word)
            url = f"https://translate.google.com/?sl=auto&tl=ru&text={encoded_word}&op=translate"
            print(f"Джарвис: Открываю перевод для '{word}'...")
            webbrowser.open(url)
        else:
            print("Джарвис: Сэр, вы не сказали, что переводить.")
        continue

    # --- СОЗДАНИЕ НАПОМИНАНИЯ ---
    if lower_input.startswith("напомни "):
        match = re.search(r"(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2})", lower_input)

        if match:
            date_str = match.group(1)
            time_str = match.group(2)
            full_datetime = f"{date_str} {time_str}"

            task = (
                lower_input.replace(match.group(0), "")
                .replace("напомни", "")
                .replace("к", "")
                .strip()
            )

            try:
                datetime.strptime(full_datetime, "%d.%m.%Y %H:%M")

                REMINDERS_FILE = os.path.join(DOCUMENTS, "reminders.json")
                reminders = (
                    load_json(REMINDERS_FILE) if os.path.exists(REMINDERS_FILE) else []
                )

                reminders.append({"task": task, "date": full_datetime})
                save_json(REMINDERS_FILE, reminders)

                print(f"Джарвис: Записал, сэр. Напомню '{task}' в {full_datetime}.")

            except ValueError:
                print("Джарвис: Сэр, вы ввели дату или время в неверном формате.")
        else:
            print(
                "Джарвис: Сэр, я не нашел дату и время. Используйте формат: 'напомни купить хлеб к 20.11.2026 13:50'"
            )
        continue

    # --- ПАСХАЛКА PYTHON (ANTIGRAVITY) ---
    if (
        "антигравитация" in lower_input
        or "открой комикс" in lower_input
        or "antigravity" in lower_input
    ):
        print("Джарвис: Сэр, активирую протокол антигравитации...")
        time.sleep(0.5)
        print("Джарвис: Открываю классический комикс XKCD про Python.")
        webbrowser.open("https://xkcd.com/353/")
        continue

    # 18. Мини-игры
    # ИГРА 'УГАДАЙ ЧИСЛО'
    if "угадай число" in lower_input or "игра угадай" in lower_input:
        secret = random.randint(1, 10)
        attempts = 0
        used_numbers = []

        print("\n=== ИГРА: УГАДАЙ ЧИСЛО ===")
        while True:
            try:
                level = int(input("Выбери количество попыток (1-10): "))
                if 1 <= level <= 10:
                    print(f"Отлично! У тебя {level} попыток.")
                    break
                else:
                    print("Ошибка! Введи число от 1 до 10.")
            except:
                print("Ошибка! Введи число.")

        while True:
            if attempts < level:
                try:
                    guess = int(input("Угадай число от 1 до 10: "))
                    if guess in used_numbers:
                        print(
                            f"Ты уже вводил {guess}. Это не считается за попытку. Попробуй другое число."
                        )
                        continue
                    if guess < 1 or guess > 10:
                        print("Ошибка! Введи число от 1 до 10.")
                        continue
                    used_numbers.append(guess)
                    attempts += 1
                    print(f"Ты ввел: {guess}")

                    if guess < secret:
                        print(f"Не {guess}! Загаданное число больше.")
                    elif guess > secret:
                        print(f"Не {guess}! Загаданное число меньше.")
                    else:
                        if attempts == 1:
                            print(
                                f"Правильно! Это {secret}! Ты угадал за {attempts} попытку!"
                            )
                        elif 1 < attempts < 5:
                            print(
                                f"Правильно! Это {secret}! Ты угадал за {attempts} попытки!"
                            )
                        else:
                            print(
                                f"Правильно! Это {secret}! Ты угадал за {attempts} попыток!"
                            )
                        break
                except:
                    print("Ошибка! Введи число!")
            else:
                print(f"Попытки закончились! Загаданное число было {secret}. Проигрыш.")
                break
        continue

    # ИГРА 'ПЕНАЛЬТИ'
    if "пенальти" in lower_input or "футбол" in lower_input:

        def clear_terminal():
            print("\n" * 2)

        def draw_scene(keeper_pos, shot=None, result=None):
            clear_terminal()
            print("\n" + "=" * 45)
            print("⚽ ПЕНАЛЬТИ (1-влево, 2-центр, 3-вправо) ⚽")
            print("=" * 45)
            print("          +-------------------+")
            print("          |                   |")
            print("          |   o o o o o o o   |")
            print("          |  o o o o o o o o  |")
            if keeper_pos == 1:
                print("          |  O                |")
            elif keeper_pos == 2:
                print("          |         O         |")
            elif keeper_pos == 3:
                print("          |                O  |")
            print("          |  o o o o o o o o  |")
            print("          |   o o o o o o o   |")
            print("          |                   |")
            print("          +-------------------+")
            print("                 ВОРОТА")
            if result == "гол":
                print("\n⚽ ГОООООООЛ! МЯЧ В СЕТКЕ! ⚽")
            elif result == "мимо":
                print("\n❌ Мяч пролетел мимо ворот!")
            elif result == "вратарь":
                print("\n❌ Вратарь отбил! Не забил!")
            elif shot is not None:
                print(
                    f"\nТы ударил: {'влево' if shot == 1 else 'в центр' if shot == 2 else 'вправо'}"
                )

        def get_title(hits):
            if hits == 0:
                return "🫣 Нуб. Тебе стоит потренироваться"
            elif hits == 1:
                return "👶 Начинающий"
            elif hits == 2:
                return "⚽ Любитель"
            elif hits == 3:
                return "🥅 Бомбардир"
            elif hits == 4:
                return "🔥 Опасный игрок"
            elif hits == 5:
                return "🎯 Снайпер"
            elif hits == 6:
                return "👟 Профессионал"
            elif hits == 7:
                return "⭐ Звезда команды"
            elif hits == 8:
                return "🏆 Мастер пенальти"
            elif hits == 9:
                return "😄 ЕХЕХЕХЕХ! Легенда!"
            elif hits == 10:
                return "🐐 РОНАЛДУ! ТЫ БОГ!"
            return "🌌 Выше богов"

        def football_game(difficulty):
            total_score = 0
            while True:
                print("\n" + "=" * 45)
                print(f"⚽ ПЕНАЛЬТИ-МАРАФОН ({difficulty.upper()}) ⚽")
                print("=" * 45)
                round_score = 0
                attempt_number = 1

                while attempt_number <= 10:
                    draw_scene(2)
                    print(f"\nУдар №{attempt_number} из 10")
                    user_choice = (
                        input("Твой удар (1/2/3 или 'выход'): ").strip().lower()
                    )

                    if user_choice == "выход":
                        print(
                            f"\n🏆 Ты остановился. Счёт за этот круг: {round_score}/10"
                        )
                        return
                    if user_choice not in ["1", "2", "3"]:
                        print("⚠️ Ошибка! Вводи только 1, 2, 3 или 'выход'.")
                        time.sleep(1)
                        continue

                    shot = int(user_choice)
                    if difficulty == "легко":
                        jump = random.choice([1, 2, 3])
                    elif difficulty == "нормально":
                        jump = (
                            shot if random.random() < 0.5 else random.choice([1, 2, 3])
                        )
                    elif difficulty == "сложно":
                        jump = (
                            shot if random.random() < 0.75 else random.choice([1, 2, 3])
                        )
                    elif difficulty == "хардкор":
                        jump = (
                            shot if random.random() < 0.9 else random.choice([1, 2, 3])
                        )

                    result = "гол" if shot != jump else "вратарь"
                    draw_scene(jump, shot, result)
                    time.sleep(1.5)

                    if result == "гол":
                        round_score += 1
                        total_score += 1
                    attempt_number += 1

                title = get_title(round_score)
                print("\n" + "=" * 45)
                print(f"🏁 РАУНД ЗАВЕРШЁН!")
                print(f"🎮 Режим: {difficulty.upper()}")
                print(f"📊 Ты забил {round_score} из 10.")
                print(f"🎖️ Твоё звание: {title}")
                print("=" * 45)

                again = input("\nСыграть ещё один раунд? (да/нет): ").strip().lower()
                if again != "да":
                    print(f"\n🏆 Итоговый счёт за всё время: {total_score} голов.")
                    print("🎉 Спасибо за игру!")
                    break

        clear_terminal()
        print("\n" + "=" * 45)
        print("⚽ ВЫБОР СЛОЖНОСТИ ⚽")
        print("=" * 45)
        print("1 — Легко")
        print("2 — Нормально")
        print("3 — Сложно")
        print("4 — Хардкор")
        print("=" * 45)
        while True:
            choice = input("Введи номер (1/2/3/4): ").strip()
            if choice == "1":
                football_game("легко")
                break
            elif choice == "2":
                football_game("нормально")
                break
            elif choice == "3":
                football_game("сложно")
                break
            elif choice == "4":
                football_game("хардкор")
                break
            else:
                print("⚠️ Вводи только 1, 2, 3 или 4!")
        continue

    # ИГРА КРЕСТИКИ-НОЛИКИ
    if "крестики" in lower_input or "нолики" in lower_input:
        tic_tac_toe()
        continue

    # 19. Диагностика
    if "тест памяти" in lower_input:
        print("Джарвис: Запуск теста оперативной памяти...")
        time.sleep(0.5)

        speed = random.randint(3000, 5000)
        print(f"Джарвис: Скорость чтения: {speed} МБ/с")
        print(f"Джарвис: Скорость записи: {speed - random.randint(100, 500)} МБ/с")
        time.sleep(0.5)
        print("Джарвис: Ошибок не обнаружено. Память чиста, сэр.")
        continue

    if "проверь файлы" in lower_input:
        print("Джарвис: Сканирование файловой системы...")
        time.sleep(0.5)
        try:
            files = os.listdir(DOCUMENTS)
            print(f"Джарвис: Обнаружено {len(files)} файлов.")
            for f in files:
                size = os.path.getsize(os.path.join(DOCUMENTS, f))
                if size > 1024 * 1024:
                    size_str = f"{size / (1024*1024):.2f} МБ"
                elif size > 1024:
                    size_str = f"{size / 1024:.2f} КБ"
                else:
                    size_str = f"{size} байт"
                print(f"  📄 {f} — {size_str}")
            print("Джарвис: Проверка завершена.")
        except Exception as e:
            print(f"Джарвис: Ошибка при проверке файлов: {e}")
        continue

    if "загрузка цп" in lower_input or "тест процессора" in lower_input:
        print("Джарвис: Замер показателей процессора...")
        time.sleep(0.5)
        cpu_load = random.randint(5, 95)
        temp = random.randint(30, 60)

        print(f"Джарвис: Загрузка ЦП: {cpu_load}%")
        print(f"Джарвис: Температура ядра: {temp}°C")

        if cpu_load > 80:
            print("Джарвис: Сэр, процессор перегружен! Закройте лишние приложения.")
        elif temp > 50:
            print("Джарвис: Сэр, телефон греется. Не запускайте while True: pass.")
        else:
            print("Джарвис: Все системы в норме. Перегревов нет.")
        continue

    if "дерево файлов" in lower_input or "покажи дерево" in lower_input:
        print("Джарвис: Построение дерева файлов...")
        time.sleep(0.5)
        try:
            files = os.listdir(DOCUMENTS)
            print(f"\n📁 {DOCUMENTS}/")
            for i, f in enumerate(files):
                if i == len(files) - 1:
                    print(f"  └── 📄 {f}")
                else:
                    print(f"  ├── 📄 {f}")
            print()
        except Exception as e:
            print(f"Джарвис: Ошибка построения дерева: {e}")
        continue

    # 20. Научные факты
    if "расскажи историю" in lower_input:
        print("\n" + "=" * 50)
        print("📜 ИСТОРИЯ: КЛЮЧЕВЫЕ СОБЫТИЯ (Углубленный уровень)")
        print("=" * 50)
        print("Джарвис: Вот важные вещи, которые стоит знать, сэр:\n")
        print(
            "1. Тридцатилетняя война (1618–1648): Началась как религиозная, стала геополитической. Итог — Вестфальский мир."
        )
        print(
            "2. Декабристы (1825): Дворянское восстание против самодержавия и крепостного права."
        )
        print(
            "3. Эпоха Возрождения: Гуманизм, Леонардо да Винчи, Коперник и переход к Новому времени."
        )
        print(
            "4. Юлий Цезарь: Римский диктатор, чье имя стало титулом (Кайзер, Царь). Убит в 44 г. до н.э."
        )
        print("=" * 50 + "\n")
        continue

    if "расскажи географию" in lower_input:
        print("\n" + "=" * 50)
        print("🌍 ГЕОГРАФИЯ: ФИЗИЧЕСКАЯ И ЭКОНОМИЧЕСКАЯ")
        print("=" * 50)
        print("Джарвис: Основные сведения, сэр:\n")
        print(
            "- Литосферные плиты: Движутся по мантии, вызывая землетрясения и образование гор."
        )
        print(
            "- Климатические пояса: Формируются по преобладанию воздушных масс (экваториальный, тропический, умеренный)."
        )
        print(
            "- Гольфстрим: Теплое течение, которое делает Европу теплее, чем она должна быть."
        )
        print("- Урбанизация: Более 50% людей в мире живут в городах.")
        print("=" * 50 + "\n")
        continue

    if "расскажи физику" in lower_input:
        print("\n" + "=" * 50)
        print("⚛️ ФИЗИКА: ФУНДАМЕНТАЛЬНЫЕ ЗАКОНЫ")
        print("=" * 50)
        print("Джарвис: Вот что важно знать, сэр:\n")
        print(
            "- Закон сохранения импульса: p = m * v. В замкнутой системе импульс сохраняется."
        )
        print(
            "- Электрический ток: Направленное движение зарядов. Сила тока измеряется в Амперах (А)."
        )
        print(
            "- Магнитное поле: Действует на движущиеся заряды. Измеряется в Теслах (Тл)."
        )
        print(
            "- КПД: Отношение полезной работы к затраченной. У реальных двигателей всегда < 100%."
        )
        print(
            "- Корпускулярно-волновой дуализм: Свет — это и волна, и частица одновременно."
        )
        print("=" * 50 + "\n")
        continue

    # 21. Поиск в шаблонах
    response = process_request(user_input, TEMPLATES)
    print("Джарвис: ", end="", flush=True)
    time.sleep(0.3)

    if response:
        print(response)
    else:
        print("Сэр, я не знаю ответа на этот вопрос.")
        print("Пожалуйста, научите меня, что я должен ответить.")
        print("(Или просто нажмите Enter / напишите 'отмена', чтобы пропустить)")

        new_answer = input("Ваш ответ: ").strip()

        if new_answer.lower() in ["", "отмена", "не хочу", "пропустить", "выход"]:
            print("Джарвис: Ладно, сэр. Пропускаем этот вопрос.")
        else:
            TEMPLATES[user_input.lower()] = new_answer
            memory = load_json(MEMORY_FILE)
            memory[user_input.lower()] = new_answer
            save_json(MEMORY_FILE, memory)

            print(
                f"✅ Запомнил! Теперь на '{user_input}' я буду отвечать: '{new_answer}'"
            )
            print(
                "💡 (Совет: напиши 'покажи базу', чтобы скопировать новые фразы в код навсегда)"
            )

    print()