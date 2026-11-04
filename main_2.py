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