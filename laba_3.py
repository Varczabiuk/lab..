import copy


class Dokument:
    def __init__(self, nazva, tekst):
        self.nazva = nazva
        self.tekst = tekst

    def pokazaty(self):
        print(f" Документ: {self.nazva}")
        print("Зміст:", self.tekst)
        print("-----")

    def klonuvaty(self):
        return copy.deepcopy(self)


class Editor:
    def __init__(self):
        self.shablony = {}

    def dodaty_shablon(self, imya, dokument):
        self.shablony[imya] = dokument

    def stvoryty_kopiyu(self, imya):
        dokument = self.shablony.get(imya)
        return dokument.klonuvaty() if dokument else None


# Демонстрація
if __name__ == "__main__":
    # Створюємо шаблон документа
    original = Dokument("Контракт", "Це типовий договір для співпраці.")

    # Додаємо в редактор
    editor = Editor()
    editor.dodaty_shablon("типовий_контракт", original)

    # Клонуємо документ
    kopiya = editor.stvoryty_kopiyu("типовий_контракт")
    kopiya.nazva = "Контракт із Google"
    kopiya.tekst = "Це змінений договір для компанії Google."

    # Виводимо результати
    print(" Оригінал:")
    original.pokazaty()

    print(" Копія:")
    kopiya.pokazaty()