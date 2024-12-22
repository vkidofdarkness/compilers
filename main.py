import tkinter as tk
from tkinter import filedialog, messagebox
import re
import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from RusLangLexer import RusLangLexer
from RusLangParser import RusLangParser
from eval_visitor import EvalVisitor

# Класс для перенаправления вывода print в текстовое поле
class OutputRedirector:
    def __init__(self, output_widget):
        self.output_widget = output_widget

    def write(self, message):
        self.output_widget.configure(state='normal')
        self.output_widget.insert(tk.END, message)
        self.output_widget.configure(state='disabled')

    def flush(self):
        pass  # Для совместимости с sys.stdout

# Класс для обработки ошибок ANTLR
class IDEErrorListener(ErrorListener):
    """Класс для обработки ошибок ANTLR."""
    def __init__(self, output_widget):
        super().__init__()
        self.output_widget = output_widget
        self.has_error = False  # Флаг наличия ошибок

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Обработка синтаксических ошибок."""
        error_message = f"Синтаксическая ошибка: строка {line}, столбец {column}: {msg}\n"
        self.output_widget.configure(state='normal')
        self.output_widget.insert(tk.END, error_message)
        self.output_widget.configure(state='disabled')
        self.has_error = True  # Устанавливаем флаг ошибки

# Основной класс IDE
class IDE:
    def __init__(self, root):
        self.root = root
        self.root.title("RusLang IDE")
        self.set_window_icon()

        # Верхняя панель инструментов
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        tk.Button(toolbar, text="Открыть", command=self.open_file).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Сохранить", command=self.save_file).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Запустить", command=self.run_code).pack(side=tk.LEFT, padx=2, pady=2)

        # Основное текстовое поле для редактора
        self.text_widget = tk.Text(root, wrap=tk.WORD, undo=True, width=80)
        self.text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Поле для отображения строки и столбца
        self.status_bar = tk.Label(root, text="Строка: 1 | Столбец: 0", anchor=tk.E, bg="lightgray")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Поле для вывода
        self.output = tk.Text(root, wrap=tk.WORD, height=10, width=80, state='disabled', bg="#f4f4f4")
        self.output.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=5, pady=5)

        # Подключение подсветки
        self.setup_syntax_highlighting()

        # Привязка событий
        self.text_widget.bind("<KeyRelease>", self.on_code_change)
        self.text_widget.bind("<ButtonRelease>", self.update_status_bar)
        self.text_widget.bind("<<Paste>>", self.on_paste)  # Обновляем подсветку после вставки
        self.update_status_bar()

        # Создание контекстного меню
        self.create_context_menu()

    def set_window_icon(self):
        """Устанавливает иконку окна программы."""
        try:
            self.root.iconbitmap("icon.ico")
        except Exception as e:
            print(f"Не удалось загрузить иконку: {e}")

    def update_status_bar(self, event=None):
        """Обновляет статусную строку с текущей позицией курсора."""
        cursor_position = self.text_widget.index(tk.INSERT).split('.')
        line = cursor_position[0]
        column = cursor_position[1]
        self.status_bar.config(text=f"Строка: {line} | Столбец: {column}")

    def setup_syntax_highlighting(self):
        """Настраивает подсветку синтаксиса."""
        self.keywords = ["цел", "лог", "стр", "если", "тогда", "иначе", "пока", "иначеесли"]
        self.function_keywords = ["вывести"]  # Ключевые слова для функций
        self.operators = ["=", r"\+", "-", r"\*", "/", "%", ">", "<", ">=", "<=", "==", "!="]
        self.comment_pattern = r"//.*"

        self.text_widget.tag_configure("keyword", foreground="blue")
        self.text_widget.tag_configure("function", foreground="purple")  # Цвет для функции вывести
        self.text_widget.tag_configure("operator", foreground="orange")
        self.text_widget.tag_configure("comment", foreground="green")

    def highlight_syntax(self, event=None):
        """Обновляет подсветку синтаксиса."""
        current_position = self.text_widget.index(tk.INSERT)

        # Удаляем старые теги
        self.text_widget.tag_remove("keyword", "1.0", tk.END)
        self.text_widget.tag_remove("function", "1.0", tk.END)
        self.text_widget.tag_remove("operator", "1.0", tk.END)
        self.text_widget.tag_remove("comment", "1.0", tk.END)

        # Получаем весь текст из редактора
        full_text = self.text_widget.get("1.0", tk.END)

        # Подсветка многострочных комментариев
        multiline_comment_pattern = r"/\*.*?\*/"
        for match in re.finditer(multiline_comment_pattern, full_text, re.DOTALL):
            start_idx = f"1.0 + {match.start()} chars"
            end_idx = f"1.0 + {match.end()} chars"
            self.text_widget.tag_add("comment", start_idx, end_idx)

        # Обрабатываем текст построчно
        lines = full_text.splitlines()
        for line_no, line in enumerate(lines):
            start_idx = f"{line_no + 1}.0"

            # Подсветка ключевых слов
            for keyword in self.keywords:
                for match in re.finditer(rf'\b{keyword}\b', line):
                    start = f"{line_no + 1}.{match.start()}"
                    end = f"{line_no + 1}.{match.end()}"
                    self.text_widget.tag_add("keyword", start, end)

            # Подсветка функции (например, вывести)
            for func in self.function_keywords:
                for match in re.finditer(rf'\b{func}\b', line):
                    start = f"{line_no + 1}.{match.start()}"
                    end = f"{line_no + 1}.{match.end()}"
                    self.text_widget.tag_add("function", start, end)

            # Подсветка операторов
            for operator in self.operators:
                for match in re.finditer(operator, line):
                    start = f"{line_no + 1}.{match.start()}"
                    end = f"{line_no + 1}.{match.end()}"
                    self.text_widget.tag_add("operator", start, end)

            # Подсветка однострочных комментариев
            comment_match = re.search(self.comment_pattern, line)
            if comment_match:
                start = f"{line_no + 1}.{comment_match.start()}"
                end = f"{line_no + 1}.{comment_match.end()}"
                self.text_widget.tag_add("comment", start, end)

        # Восстанавливаем позицию курсора
        self.text_widget.mark_set(tk.INSERT, current_position)

    def create_context_menu(self):
        """Создаёт контекстное меню для текстового поля и подключает горячие клавиши."""
        # Создаём контекстное меню
        self.context_menu = tk.Menu(self.text_widget, tearoff=0)
        self.context_menu.add_command(label="Копировать", command=lambda: self.text_widget.event_generate("<<Copy>>"))
        self.context_menu.add_command(label="Вырезать", command=lambda: self.text_widget.event_generate("<<Cut>>"))
        self.context_menu.add_command(label="Вставить", command=lambda: self.text_widget.event_generate("<<Paste>>"))
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Выделить всё", command=lambda: self.text_widget.event_generate("<<SelectAll>>"))

        # Подключаем контекстное меню к текстовому виджету (правая кнопка мыши)
        self.text_widget.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        """Отображает контекстное меню."""
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def save_file(self):
        """Сохраняет текст из редактора в файл."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовый файл", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_widget.get("1.0", tk.END).strip())
            messagebox.showinfo("Сохранение", "Файл успешно сохранён!")

    def open_file(self):
        """Открывает файл и загружает его содержимое в редактор."""
        file_path = filedialog.askopenfilename(filetypes=[("Текстовый файл", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert("1.0", content)
            self.highlight_syntax()  # Обновляем подсветку после загрузки

    def run_code(self):
        """Запускает код из текстового редактора, выполняя его через интерпретатор."""
        code = self.text_widget.get("1.0", tk.END).strip()
        if not code:
            self.display_output("Введите код для выполнения.")
            return

        try:
            # Очищаем поле вывода
            self.output.configure(state='normal')
            self.output.delete("1.0", tk.END)
            self.output.configure(state='disabled')

            sys.stdout = OutputRedirector(self.output)
            input_stream = InputStream(code)
            lexer = RusLangLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = RusLangParser(token_stream)

            # Настраиваем обработчик ошибок
            error_listener = IDEErrorListener(self.output)
            lexer.removeErrorListeners()
            parser.removeErrorListeners()
            lexer.addErrorListener(error_listener)
            parser.addErrorListener(error_listener)

            # Разбираем программу
            tree = parser.program()

            # Проверяем наличие ошибок
            if error_listener.has_error:
                self.output.configure(state='normal')
                self.output.insert(tk.END, "Программа не выполнена из-за ошибок.\n")
                self.output.configure(state='disabled')
                sys.stdout = sys.__stdout__
                return

            # Интерпретируем код через EvalVisitor
            visitor = EvalVisitor()
            visitor.visit(tree)

            sys.stdout = sys.__stdout__
        except Exception as e:
            self.output.configure(state='normal')
            self.output.insert(tk.END, f"Ошибка: {str(e)}\n")
            self.output.configure(state='disabled')
            sys.stdout = sys.__stdout__

    def display_output(self, message):
        """Отображает сообщение в поле вывода."""
        self.output.configure(state='normal')
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, message)
        self.output.configure(state='disabled')

    def on_code_change(self, event=None):
        """Обновляет подсветку синтаксиса при изменении текста."""
        self.update_status_bar()
        self.highlight_syntax()

    def on_paste(self, event=None):
        """Обновляет подсветку синтаксиса после вставки текста."""
        self.text_widget.after(1, self.highlight_syntax)

if __name__ == "__main__":
    root = tk.Tk()
    app = IDE(root)
    root.mainloop()
