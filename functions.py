def print_slow(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


_SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def physics_calculator():
    print("\n=== КАЛЬКУЛЯТОР ФИЗИКИ v2.0 ===")
    print("1. Второй закон Ньютона (F = m * a)")
    print("2. Закон Ома (I = U / R)")
    print("3. Кинетическая энергия (E = m * v^2 / 2)")
    print("4. Плотность (ρ = m / V)")
    print("5. Давление (P = F / S)")
    print("6. Закон Гука (F = k * Δx)")
    print("7. Мощность (N = A / t)")
    print("0. Выход в главное меню")

    choice = input("Выберите формулу (1-7/0): ").strip()

    if choice == "0":
        return
    elif choice == "1":
        try:
            m = float(input("Введите массу (кг): "))
            a = float(input("Введите ускорение (м/с^2): "))
            print(f"Джарвис: Сила F = {m * a} Ньютонов.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "2":
        try:
            u = float(input("Введите напряжение (Вольты): "))
            r = float(input("Введите сопротивление (Омы): "))
            if r == 0:
                print("Джарвис: Сэр, на ноль делить нельзя.")
            else:
                print(f"Джарвис: Сила тока I = {u / r} Ампер.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "3":
        try:
            m = float(input("Введите массу (кг): "))
            v = float(input("Введите скорость (м/с): "))
            print(f"Джарвис: Кинетическая энергия E = {0.5 * m * v**2} Джоулей.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "4":
        try:
            m = float(input("Введите массу (кг): "))
            v = float(input("Введите объем (м^3): "))
            if v == 0:
                print("Джарвис: Сэр, объем не может быть нулевым.")
            else:
                print(f"Джарвис: Плотность ρ = {m / v} кг/м^3.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "5":
        try:
            f = float(input("Введите силу (Ньютоны): "))
            s = float(input("Введите площадь (м^2): "))
            if s == 0:
                print("Джарвис: Сэр, площадь не может быть нулевой.")
            else:
                print(f"Джарвис: Давление P = {f / s} Паскалей.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "6":
        try:
            k = float(input("Введите жесткость (Н/м): "))
            dx = float(input("Введите удлинение (м): "))
            print(f"Джарвис: Сила упругости F = {k * dx} Ньютонов.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    elif choice == "7":
        try:
            a = float(input("Введите работу (Джоули): "))
            t = float(input("Введите время (секунды): "))
            if t == 0:
                print("Джарвис: Сэр, время не может быть нулевым.")
            else:
                print(f"Джарвис: Мощность N = {a / t} Ватт.")
        except ValueError:
            print("Джарвис: Сэр, вводите только числа.")
    else:
        print("Джарвис: Неверный выбор.")


def stopwatch_manager(action):
    global время_старта
    if action == "start":
        if время_старта is not None:
            return "Джарвис: Сэр, секундомер уже запущен! Скажите 'стоп', чтобы остановить."
        время_старта = time.time()
        return "Джарвис: Секундомер запущен, сэр! Время пошло."
    elif action == "stop":
        if время_старта is None:
            return (
                "Джарвис: Сэр, секундомер и так не работает. Сначала скажите 'засекай'."
            )
        elapsed = time.time() - время_старта
        время_старта = None

        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)

        result = "Джарвис: Секундомер остановлен!\n"
        if hours > 0:
            result += f"  ⏱️ Прошло времени: {hours} ч {minutes} мин {seconds} сек."
        elif minutes > 0:
            result += f"  ⏱️ Прошло времени: {minutes} мин {seconds} сек."
        else:
            result += f"  ⏱️ Прошло времени: {seconds} сек."
        return result


def safe_eval(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return _SAFE_OPS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        return _SAFE_OPS[type(node.op)](safe_eval(node.operand))
    else:
        raise TypeError("Недопустимая операция")


def safe_calculator(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        return safe_eval(tree.body)
    except Exception:
        return "Ошибка: неверное выражение"


def text_to_base_jarvis(text, base):
    """Кодирует текст: каждый байт UTF-8 -> число в системе base, через пробел."""
    if not (2 <= base <= 16):
        return "Ошибка: поддерживаются системы от 2 до 16"

    try:
        data = text.encode("utf-8")
        digits = "0123456789abcdef"
        result = []
        for byte in data:
            num = byte
            converted = ""
            if num == 0:
                converted = "0"
            else:
                while num > 0:
                    converted = digits[num % base] + converted
                    num //= base
            result.append(converted)
        return " ".join(result)
    except Exception as e:
        return f"Ошибка шифрования: {e}"


def base_to_text_jarvis(encoded_text, base):
    """Расшифровывает строку с числами, разделёнными пробелами (UTF-8)."""
    if not (2 <= base <= 16):
        return "Ошибка: поддерживаются системы от 2 до 16"

    parts = encoded_text.split()
    if not parts:
        return "Ошибка: пустая строка"

    byte_values = []
    for part in parts:
        try:
            value = int(part, base)
            if not 0 <= value <= 255:
                return f"Ошибка: число {value} не является байтом (0–255). Проверьте систему счисления."
            byte_values.append(value)
        except ValueError:
            return f"Ошибка: '{part}' не является числом в {base}-й системе."

    try:
        return bytes(byte_values).decode("utf-8")
    except UnicodeDecodeError:
        return "Ошибка: не удалось расшифровать текст. Возможно, неверная система счисления или код повреждён (потеряны пробелы)."


# Посимвольное кодирование (Unicode/ASCII)
def text_to_base_old(text, base):
    """Переводит каждый символ (ord) в систему счисления."""
    if not (2 <= base <= 16):
        return "Ошибка: поддерживаются системы от 2 до 16"

    digits = "0123456789ABCDEF"
    result = []

    for char in text:
        ascii_code = ord(char)
        if ascii_code == 0:
            converted = "0"
        else:
            converted = ""
            temp = ascii_code
            while temp > 0:
                converted = digits[temp % base] + converted
                temp //= base
        result.append(converted)

    return " ".join(result)


def base_to_text_old(encoded_text, base):
    """Расшифровывает коды символов (chr)."""
    if not (2 <= base <= 16):
        return "Ошибка: поддерживаются системы от 2 до 16"

    result = []
    parts = encoded_text.split()

    for part in parts:
        try:
            ascii_code = int(part, base)
            result.append(chr(ascii_code))
        except ValueError:
            return f"Ошибка: '{part}' не является числом в {base}-й системе."

    return "".join(result)


def tic_tac_toe():
    # Игровое поле из 9 клеток
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "X"
    ai = "O"

    def print_board():
        # Отрисовка игрового поля
        def format_cell(cell):
            if cell == "X":
                return "[X]"
            elif cell == "O":
                return "[O]"
            else:
                return f" {cell} "

        print("\n" + "=" * 13)
        print(
            f"|{format_cell(board[0])}|{format_cell(board[1])}|{format_cell(board[2])}|"
        )
        print("|---|---|---|")
        print(
            f"|{format_cell(board[3])}|{format_cell(board[4])}|{format_cell(board[5])}|"
        )
        print("|---|---|---|")
        print(
            f"|{format_cell(board[6])}|{format_cell(board[7])}|{format_cell(board[8])}|"
        )
        print("=" * 13 + "\n")

    def check_win(b, mark):
        win_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in win_combos:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] == mark:
                return True
        return False

    def ai_move():
        # 1. Попытка выиграть
        for i in range(9):
            if board[i] not in ["X", "O"]:
                board_copy = board.copy()
                board_copy[i] = ai
                if check_win(board_copy, ai):
                    board[i] = ai
                    return

        # 2. Попытка заблокировать игрока
        for i in range(9):
            if board[i] not in ["X", "O"]:
                board_copy = board.copy()
                board_copy[i] = player
                if check_win(board_copy, player):
                    board[i] = ai
                    return

        # 3. Центр или случайная клетка
        if board[4] not in ["X", "O"]:
            board[4] = ai
        else:
            empty = [i for i, val in enumerate(board) if val not in ["X", "O"]]
            if empty:
                board[random.choice(empty)] = ai

    print("\n=== ИГРА: КРЕСТИКИ-НОЛИКИ ===")
    print("Джарвис: Сэр, вы играете за 'X', я за 'O'.")
    print("Вводите номер клетки от 1 до 9, чтобы сделать ход.")
    print_board()

    moves = 0
    while moves < 9:
        try:
            move = int(input("Ваш ход (1-9): ")) - 1
            if board[move] in ["X", "O"]:
                print("Джарвис: Сэр, эта клетка уже занята!")
                continue
            board[move] = player
            moves += 1
            print_board()

            if check_win(board, player):
                print("🎉 Джарвис: Поздравляю, сэр! Вы победили!")
                break

            if moves == 9:
                break

            print("Джарвис: Мой ход...")
            ai_move()
            moves += 1
            print_board()

            if check_win(board, ai):
                print(
                    "🤖 Джарвис: Сэр, я выиграл. Не расстраивайтесь, мой процессор быстрее."
                )
                break

        except (ValueError, IndexError):
            print("Джарвис: Сэр, введите число от 1 до 9.")
            continue

    if moves == 9 and not check_win(board, player) and not check_win(board, ai):
        print("🤝 Джарвис: Ничья! Вы достойный соперник, сэр.")


# Путь к папке с данными
DOCUMENTS = os.path.expanduser("~/Documents")
MEMORY_FILE = os.path.join(DOCUMENTS, "jarvis_templates_v2.json")


def load_json(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_json(filepath, data):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except:
        pass


def delete_file_safe(filename):
    # Защита от выхода за пределы папки с данными
    if "/" in filename or ".." in filename:
        return "Ошибка: недопустимое имя файла."

    filepath = os.path.join(DOCUMENTS, filename)

    if not os.path.exists(filepath):
        return f"Ошибка: файл '{filename}' не найден."

    try:
        os.remove(filepath)
        return f"Файл '{filename}' успешно удален."
    except Exception as e:
        return f"Не удалось удалить файл. Ошибка: {e}"


def dec_to_base(dec_num, base):
    """Переводит десятичное число в любую систему (2-16)."""
    if dec_num == 0:
        return "0"

    digits = "0123456789ABCDEF"
    is_negative = dec_num < 0
    dec_num = abs(dec_num)
    result = ""

    while dec_num > 0:
        result = digits[dec_num % base] + result
        dec_num //= base

    if is_negative:
        result = "-" + result
    return result


def base_to_dec(num_str, base):
    """Переводит число из указанной системы счисления в десятичную."""
    try:
        return int(str(num_str).strip(), base)
    except (ValueError, TypeError):
        return None


def get_time():
    return datetime.now().strftime("%H:%M")


def get_greeting():
    """Возвращает приветствие в зависимости от времени суток."""
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def clean_expired_reminders():
    """Удаляет старые напоминания из файла."""
    REMINDERS_FILE = os.path.join(DOCUMENTS, "reminders.json")

    if not os.path.exists(REMINDERS_FILE):
        return

    try:
        with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
            reminders = json.load(f)

        now = datetime.now()
        active_reminders = []
        removed_count = 0

        for reminder in reminders:
            try:
                reminder_time = datetime.strptime(reminder["date"], "%Y-%m-%d %H:%M")
                if reminder_time > now:
                    active_reminders.append(reminder)
                else:
                    removed_count += 1
            except:
                active_reminders.append(reminder)

        if removed_count > 0:
            with open(REMINDERS_FILE, "w", encoding="utf-8") as f:
                json.dump(active_reminders, f, ensure_ascii=False, indent=2)
            print_slow(
                f"Джарвис: Очистка завершена. Удалено старых напоминаний: {removed_count}"
            )

    except Exception as e:
        print(f"Джарвис: Ошибка при очистке напоминаний: {e}")


def process_request(user_input, templates):
    clean_input = re.sub(r"[^\w\s]", "", user_input.lower().strip())

    # Удаляем слово "джарвис" из любого места текста
    clean_input = re.sub(r"\bджарвис\b", "", clean_input).strip()

    def get_response(response_text):
        if "{time}" in response_text:
            response_text = response_text.replace("{time}", get_time())
        if "{greeting}" in response_text:
            response_text = response_text.replace("{greeting}", get_greeting())
        if "|" in response_text:
            variants = [v.strip() for v in response_text.split("|")]
            return random.choice(variants)
        current_hour = datetime.now().hour
        if current_hour >= 23 or current_hour < 5:
            if random.random() < 0.5:
                response_text += (
                    "\nДжарвис: Сэр, сейчас глубокая ночь. Вам следует выспаться."
                )

        return response_text

    # 1. Точное совпадение
    if clean_input in templates:
        return get_response(templates[clean_input])

    # 2. Частичное совпадение
    for key, response in templates.items():
        if " " in key and key in clean_input:
            return get_response(response)

    # 3. Поиск похожих слов (опечатки)
    best_match = None
    best_ratio = 0.0

    for key in templates.keys():
        if abs(len(key) - len(clean_input)) > 3:
            continue

        ratio = difflib.SequenceMatcher(None, clean_input, key).ratio()

        if ratio > 0.85 and ratio > best_ratio:
            best_ratio = ratio
            best_match = key

    if best_match:
        return get_response(templates[best_match])

    return None