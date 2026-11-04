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