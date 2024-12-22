from RusLangVisitor import RusLangVisitor
from RusLangParser import RusLangParser

class EvalVisitor(RusLangVisitor):
    def __init__(self):
        super().__init__()
        # Здесь храним переменные и их значения
        self.memory = {} 
    # --------------------------
    # Визит "программы" в целом
    # --------------------------
    def visitProgram(self, ctx: RusLangParser.ProgramContext):
        # Перебираем все глобальные операторы
        return self.visitChildren(ctx)

    # --------------------------
    # Объявления переменных
    # --------------------------
    def visitVarDeclaration(self, ctx: RusLangParser.VarDeclarationContext):
        vartype = ctx.getChild(0).getText()  # "цел", "лог", "стр"
        # varList -> IDENT (COMMA IDENT)* 
        for ident in ctx.varList().IDENT():
            name = ident.getText()
            # Инициализируем значением по умолчанию:
            if vartype == 'цел':
                self.memory[name] = 0
            elif vartype == 'стр':
                self.memory[name] = ""
            elif vartype == 'лог':
                self.memory[name] = False
            else:
                self.memory[name] = None
        return None

    # --------------------------
    # Присваивание: a = expr;
    # --------------------------
    def visitAssignmentStatement(self, ctx: RusLangParser.AssignmentStatementContext):
        var_name = ctx.IDENT().getText()
        val = self.visit(ctx.expr())  # вычислим expr

        # Преобразуем значение к нужному типу (целое, строка или логическое)
        if isinstance(val, int):
            self.memory[var_name] = int(val)
        elif isinstance(val, str):
            self.memory[var_name] = str(val)
        elif isinstance(val, bool):
            self.memory[var_name] = bool(val)
        else:
            self.memory[var_name] = val  # Сохраняем, если это неизвестный тип
        return None

    # --------------------------
    # Вывод: вывести(expr);
    # --------------------------
    def visitPrintStatement(self, ctx: RusLangParser.PrintStatementContext):
        val = self.visit(ctx.expr())
        print(val)
        return None

    # --------------------------
    # ifStatement: 
    #   если (expr) тогда blockStatement (иначеPart)?
    # --------------------------
    def visitIfStatement(self, ctx: RusLangParser.IfStatementContext):
        # Проверяем основное условие (если)
        if self.visit(ctx.expr()):  # Если основное условие истинно
            self.visit(ctx.blockStatement())
            return None  # Завершаем обработку, если условие выполнено
        else:
            # Проверяем все блоки "иначеесли"
            for elifPart in ctx.иначеЕслиPart():
                if self.visit(elifPart.expr()):  # Если условие elif истинно
                    self.visit(elifPart.blockStatement())
                    return None  # Прекращаем выполнение, если найдено истинное условие

            # Проверяем блок "иначе", если он существует
            if ctx.иначеPart():
                self.visit(ctx.иначеPart().blockStatement())

        return None

    # --------------------------
    # иначеPart: иначе blockStatement
    # --------------------------
    def visitИначеPart(self, ctx: RusLangParser.ИначеPartContext):
        # просто заходим в блок
        self.visit(ctx.blockStatement())
        return None

    # --------------------------
    # whileStatement: 
    #   пока (expr) blockStatement
    # --------------------------
    def visitWhileStatement(self, ctx: RusLangParser.WhileStatementContext):
        # Выполняем цикл, пока условие истинно
        while self.visit(ctx.expr()):
            self.visit(ctx.blockStatement())
        return None

    # --------------------------
    # blockStatement: { statement* }
    # --------------------------
    def visitBlockStatement(self, ctx: RusLangParser.BlockStatementContext):
        # Просто обходим всех детей (statement)
        return self.visitChildren(ctx)

    # --------------------------
    # Выражения (expr)
    # --------------------------
    def visitAtom(self, ctx: RusLangParser.AtomContext):
        # atom : INT_NUMBER | ИСТИНА | ЛОЖЬ | IDENT | LPAREN expr RPAREN
        if ctx.INT_NUMBER():
            return int(ctx.INT_NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.ИСТИНА():
            return True
        elif ctx.ЛОЖЬ():
            return False
        elif ctx.IDENT():
            var_name = ctx.IDENT().getText()
            return self.memory.get(var_name, 0)  # если нет в памяти, возвращаем 0
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitRelationalExpr(self, ctx: RusLangParser.RelationalExprContext):
        # Вычисляем левый операнд
        left = self.visit(ctx.additiveExpr(0))

        # Проверяем наличие второго операнда
        if ctx.additiveExpr(1):
            right = self.visit(ctx.additiveExpr(1))  # Вычисляем правый операнд
            operator = ctx.getChild(1).getText()  # Оператор сравнения

            if operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right

        # Если нет второго операнда, возвращаем левый
        return left

    def visitAdditiveExpr(self, ctx: RusLangParser.AdditiveExprContext):
        # Вычисляем первый операнд (всегда существует)
        left = self.visit(ctx.multiplicativeExpr(0))

        # Если есть второй операнд (например, в случае "a + b"), обработаем его
        if ctx.multiplicativeExpr(1):
            right = self.visit(ctx.multiplicativeExpr(1))
            operator = ctx.getChild(1).getText()  # Оператор "+" или "-"
            if operator == '+':
                # Если оба операнда строки или один из них — строка
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)  # Конкатенация строк
                return left + right
            elif operator == '-':
                return left - right

        # Если второго операнда нет, возвращаем только первый операнд
        return left
    
    def visitMultiplicativeExpr(self, ctx: RusLangParser.MultiplicativeExprContext):
        # Вычисляем первый операнд
        left = self.visit(ctx.atom(0))

        # Проверяем наличие второго операнда
        if ctx.atom(1):
            right = self.visit(ctx.atom(1))
            operator = ctx.getChild(1).getText()  # Оператор: "*", "/", "%"

            if operator == '*':
                return left * right
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Деление на ноль")
                return left / right
            elif operator == '%':
                return left % right

        # Если второго операнда нет, возвращаем только первый операнд
        return left
