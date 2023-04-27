import csv
import datetime as dt
import sys


class Notes():
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = []
        try:
            with open(file_name, mode='r', newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=';', escapechar='\\')
                for _ in data:
                    self.notes.append([dt.datetime.strptime
                                       (_[0], '%Y-%m-%d %H:%M:%S'), _[1]])
        except:
            pass

    def __rewrite_csv__(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerows(self.notes)

    def add_note(self, text):
        self.notes.append([dt.datetime.today().replace(microsecond=0), text])
        with open(self.file_name, 'a+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';', escapechar='\\')
            csv_writer.writerow(self.notes[-1])

    def filter_by_dates(self, first, last):
        i = 0
        out = []
        for _ in self.notes:
            if first <= _[0] <= last:
                out.append([(i), _[0], _[1]])
            i += 1
        return out

    def print_by_dates(self, first, last):
        i = 0
        out = False
        for _ in self.notes:
            if first <= _[0] <= last:
                print(i, str(_[0]), _[1])
                out = True
            i += 1
        return out

    def print_by_id(self, index):
        if 0 <= index <= len(self.notes):
            print(index, str(self.notes[index][0]), self.notes[index][1])
            return True
        else:
            return False

    def del_by_index(self, index):
        if 0 <= index <= len(self.notes):
            self.notes.pop(index)
            self.__rewrite_csv__()
            return True
        else:
            return False

    def edit_by_index(self, index, new_text):
        if 0 <= index <= len(self.notes) and len(new_text) > 0:
            self.notes[index][0] = dt.datetime.today().replace(microsecond=0)
            self.notes[index][1] = new_text
            self.__rewrite_csv__()
            return True
        else:
            return False


class UserDialog():
    def print_menu(self):
        print('\n =====',
              'Ваш как-бы-Джарвис приветствует вас.',
              'Введите один из номеров команды ниже (цифру и enter)', sep=chr(10))
        print('1 - добавить заметку',
              '2 - показать заметки (с фильтром по дате от .. до ..)',
              '3 - редактировать заметку по ID',
              '4 - удалить заметку по ID',
              '0 - выход',
              sep='\n')

    def user_choice(self):
        ur_cmd = input('ожидаю цифру...:')
        if not ur_cmd.isdigit():
            print('Мискузи?... Введите цифру от 0 до 4')
        elif int(ur_cmd) not in range(5):
            print('Чрезмерно сложные цифры для простой задачи. Введите цифру от 0 до 4')
        else:
            return int(ur_cmd)

    def menu_cycle(self, notes):
        exit_flag = False
        while exit_flag == False:
            self.print_menu()
            ur_cmd = self.user_choice()
            if ur_cmd == 1:
                # добавить заметку
                inp = input('Введите текст заметки (или пустой ввод для отмены):')
                if len(inp) > 0:
                    notes.add_note(inp)
            elif ur_cmd == 2:
                # показать заметки по фильтру даты
                try:
                    d, m, y = input(
                        'Введите начальную дату фильтра (dd/mm/yyyy) (пустой ввод без начальной даты):').split('/')
                    min_date = dt.datetime(int(y), int(m), int(d))
                except:
                    print('(вывод без нижней границы даты)')
                    min_date = dt.datetime.min
                try:
                    d, m, y = input(
                        'Введите конечную дату фильтра (dd/mm/yyyy) (пустой ввод без конечной даты):').split('/')
                    max_date = dt.datetime(int(y), int(m), int(d))
                except:
                    print('(вывод без верхней границы даты)')
                    max_date = dt.datetime.max
                print('В запрашиваемом диапазоне найдены заметки:')
                if notes.print_by_dates(first=min_date, last=max_date) == False:
                    print('точнее НЕ найдены')
                input('ENTER для продолжения')

            elif ur_cmd == 3:
                # редактировать заметку по ID
                try:
                    inp_id = int(input('Введите ID заметки:'))
                    print('Заметка: ', end='')
                    if notes.print_by_id(inp_id):
                        inp = input('Введите новый текст заметки (или пустой ввод для отмены):')
                        if notes.edit_by_index(inp_id, inp) == False:
                            print('...осталась без изменений')
                    else:
                        print('не найдена.')
                except:
                    print('Ошибка ввода. Необходимо целое число')

            elif ur_cmd == 4:
                # удалить заметку по ID
                try:
                    inp_id = int(input('Введите ID заметки:'))
                    print('Заметка: ', end='')
                    if notes.print_by_id(inp_id):
                        inp = input('Удалить? (Y/N)')
                        if inp == 'Y' or inp == 'y':
                            notes.del_by_index(inp_id)
                    else:
                        print('не найдена.')
                except:
                    print('Ошибка ввода. Необходимо целое число')

            elif ur_cmd == 0:
                print('Наш экипаж прощается с вами и желает дальнейших успехов...')
                exit_flag = True


class FromCmd:
    def __init__(self, promt):
        self.promt = promt
        self.exec_cmd

    def exec_cmd(self, notes):
        if self.promt[1] in ('-help', '-h', '?', '-?'):
            print('Синтаксис консольных команд:')
            print('Добавить заметку ""-add Текст_заметки""')
            print('Изменить заметку ""-edit Номер_заметки Новый_Текст_заметки""')
            print('Удалить заметку ""-delete Номер_заметки""')
            print('Вывести список заметок ""-print""')
        elif self.promt[1] == '-add':
            ss = ''.join(self.promt[2:])
            if len(ss) > 0:
                notes.add_note(ss)
                return True
            else:
                print('после -add требуется текст заметки')
                return False
        elif self.promt[1] == '-delete':
            if self.promt[2].isdigit and 0 <= int(self.promt[2]) <= len(notes.notes):
                if notes.del_by_index(int(self.promt[2])) == True:
                    print('Заметка удалена')
                    return True
            else:
                print('Заметка по номеру не найдена')
                return False
        elif self.promt[1] == '-edit':
            if self.promt[2].isdigit and 0 <= int(self.promt[2]) <= len(notes.notes):
                ss = ''.join(self.promt[3:])
                if notes.edit_by_index(int(self.promt[2]), ss) == True:
                    return True
                else:
                    print('Заметка по номеру не найдена')
                    return False
            else:
                print('Заметка по номеру не найдена')
                return False
        elif self.promt[1] == '-print':
            notes.print_by_dates(dt.datetime.min, dt.datetime.max)
        else:
            return False

        if __name__ == '__main__':
            notes = Notes('Notes.csv')
            sys.argv = ['заметки.py', '-add', 'текст']
            cmd = FromCmd(sys.argv)
            if cmd.exec_cmd(notes) == False:
                jarvis = UserDialog(notes)
                jarvis.menu_cycle()