#3Создайте графическую оболочку для скрипта, написанного в ходе
#выполнения задания № 4 лабораторной работы № 2, в виде диалогового
#окна (рис. 2). Рекомендуется использовать wxPython 

#5Напишите скрипт с графическим интерфейсом пользователя для
#демонстрации работы класса StringFormatter. Примеры окон приведены
#на рис. 4 (все элементы управления необходимо обязательно
#реализовать те же, что присутствуют на рисунке).
class MainFrame(wx.Frame):
    ''' Класс главного окна '''

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Main Frame", size=(500, 400))
        self.create_menu()

        panel = wx.Panel(self, -1)
        self.tree_ctrl = wx.TreeCtrl(panel, -1, size=(200, 320), pos=(10, 10),
                                     style=wx.TR_DEFAULT_STYLE |
                                     wx.TR_FULL_ROW_HIGHLIGHT |
                                     wx.TR_EDIT_LABELS)

        self.list_box = wx.ListCtrl(panel, -1, style=wx.LC_REPORT,
                                    size=(250, 200), pos=(230, 120))
        self.list_box.InsertColumn(0, "Title")
        self.list_box.InsertColumn(1, "Type")

        wx.StaticText(panel, -1, "CD title:", pos=(230, 20))
        self.text_cd = wx.TextCtrl(panel, -1, size=(190, 20), pos=(290, 20))

        message_button = wx.Button(
            panel, -1, "Add!", size=(250, 30), pos=(230, 70))
        self.Bind(wx.EVT_BUTTON, self.on_add_disc, message_button)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])
        self.statusbar.SetStatusText("wxPython Program", 1)
        self.statusbar.SetStatusText("(c) 2016 Author", 2)

        self.init_model()

    def init_model(self):
        self.discs = {'cd': ['1972 - Foxtrot', '1980 - Duke', '2002 - Up'],
                      'dvd': ['Forrest Gump', 'Home Alone']}

        self.update_views()

    def update_views(self):
        self.tree_ctrl.DeleteAllItems()
        self.list_box.DeleteAllItems()

        root = self.tree_ctrl.AddRoot('Disc Collection')

        for d in self.discs:
            disc_type = self.tree_ctrl.AppendItem(root, d)
            for item in self.discs[d]:
                self.tree_ctrl.AppendItem(disc_type, item)

        i = 0
        for d in self.discs:
            for item in self.discs[d]:
                self.list_box.InsertStringItem(i, item)
                self.list_box.SetStringItem(i, 1, d)
                if d == 'dvd':
                    self.list_box.SetItemBackgroundColour(i, "lightgreen")
                else:
                    self.list_box.SetItemBackgroundColour(i, "lightyellow")
                i += 1

    def menu_data(self):
        data = (("&Operations",
                 ({"&Add!": self.on_add_disc},)),
                ("&Help",
                 ({"&About...": self.on_about_click},
                  {"&Web-site": None})
                 ))
        return data

    def create_menu(self):
        menu = wx.MenuBar()

        for item in self.menu_data():
            menu_item = self.create_sub_menu(item[1])
            menu.Append(menu_item, item[0])

        self.SetMenuBar(menu)

    def create_sub_menu(self, itemgroup):
        groupmenu = wx.Menu()

        for item in itemgroup:
            # Каждый элемент меню представлен своим названием
            # и (опционально) обработчиком на свое нажатие
            title, handler = item.items()[0]
            menu_item = groupmenu.Append(-1, title)
            if handler:
                self.Bind(wx.EVT_MENU, handler, menu_item)

        return groupmenu

    def on_add_disc(self, event):
        if self.text_cd.Value != "":
            self.discs['cd'].append(self.text_cd.Value)

        self.statusbar.SetStatusText("Disc was added!")
        self.update_views()

    def on_about_click(self, event):
        dlg = wx.MessageDialog(None, "This is the coolest thing ever!",
                               "MessageDialog", wx.OK | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        dlg.Destroy()


class StringFrame(wx.Frame):
    ''' Класс окна работы со строками '''

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Обработка строк", size=(400, 320))

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Строка:", pos=(5, 20))
        self.entry_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 20))
        wx.StaticText(panel, -1, "Результат:", pos=(5, 230))
        self.result_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 230))

        sc = wx.SpinCtrl(panel, -1, "", (295, 55), (40, -1))
        sc.SetRange(1, 20)
        sc.SetValue(5)

        wx.CheckBox(panel, -1, "Удалить слова размером меньше",
                    (70, 60), (250, 20))
        wx.StaticText(panel, -1, "букв", pos=(340, 62))
        wx.CheckBox(panel, -1, "Заменить все цифры на *", (70, 80), (220, 20))
        wx.CheckBox(panel, -1, "Вставить пробелы между символами",
                    (70, 100), (280, 20))
        self.sort_checkbox = wx.CheckBox(panel, -1, "Сортировать слова в строке",
                                         (70, 120), (220, 20))

        self.radio_by_size = wx.RadioButton(
            panel, -1, "По размеру", (100, 140), (150, 20))
        self.radio_by_lex = wx.RadioButton(
            panel, -1, "Лексикографически", (100, 160), (150, 20))
        self.radio_by_size.Disable()
        self.radio_by_lex.Disable()

        format_button = wx.Button(panel, -1, "Форматирование",
                                  size=(300, 30), pos=(70, 190))

        self.Bind(wx.EVT_BUTTON, self.on_format_click, format_button)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.sort_checkbox)

    def on_format_click(self, event):
        # кое-что реализуем...
        input = self.entry_text.Value
        output = ' '.join(input)
        self.result_text.Value = output

    def on_check(self, event):
        if self.sort_checkbox.IsChecked():
            self.radio_by_size.Enable()
            self.radio_by_lex.Enable()
        else:
            self.radio_by_size.Disable()
            self.radio_by_lex.Disable()


class LogFrame(wx.Frame):
    ''' Класс окна отображения лога '''

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Искатель строк", size=(500, 400))
        self.create_menu()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-3, -2])

        sample_list = [r'Файл first.txt был обработан 05.03.2016 19:05:18:',
                       '',
                       'Строка 105, позиция 19 : найдено "5-12-2011"',
                       'Строка 120, позиция 7 : найдено "22-10-2012"',
                       '',
                       r'Файл example.txt был обработан 05.03.2015 19:08:24:',
                       '',
                       'Строка 3, позиция 10 : найдено "11-05-2014"',
                       'Строка 12, позиция 2 : найдено "23-11-2014"',
                       'Строка 12, позиция 17 : найдено "23-11-2014"']
        list_box = wx.ListBox(self, -1, (20, 20), (80, 120),
                              sample_list, wx.LB_SINGLE)
        list_box.SetSelection(0)

        self.statusbar.SetStatusText(
            "Обработан файл example.txt")
        self.statusbar.SetStatusText("15 036 байт", 1)

    def menu_data(self):
        data = (("&Файл",
                 ({"&Открыть...": self.on_open_file},)),
                ("&Лог",
                 ({"&Сохранить новый...": self.on_save_log},
                  {"&Добавить в лог": None},
                  {"&Просмотр лога": None})
                 ))
        return data

    def create_menu(self):
        menu = wx.MenuBar()

        for item in self.menu_data():
            menu_item = self.create_sub_menu(item[1])
            menu.Append(menu_item, item[0])

        self.SetMenuBar(menu)

    def create_sub_menu(self, itemgroup):
        groupmenu = wx.Menu()

        for item in itemgroup:
            title, handler = item.items()[0]
            menu_item = groupmenu.Append(-1, title)
            if handler:
                self.Bind(wx.EVT_MENU, handler, menu_item)

        return groupmenu

    def on_open_file(self, event):
        dlg = wx.FileDialog(self, message="Выберите файл", defaultDir="",
                            defaultFile="", wildcard="*.*", style=wx.OPEN)

        # при открытии файла просто обновляем строку состояния
        if dlg.ShowModal() == wx.ID_OK:
            self.statusbar.SetStatusText(dlg.GetPath())

    def on_save_log(self, event):
        # при попытке сохранения лога внезапно запускаем окно ))
        dlg = StringFrame()
        dlg.Show()


if __name__ == '__main__':
    # создаем объект приложения
    app = wx.App()

    # создаем объект окна MainFrame
    main_frame = MainFrame()
    # и показываем
    main_frame.Show()

    # создаем объект окна MainFrame
    string_frame = StringFrame()
    # и показываем
    string_frame.Show()

    # создаем объект окна MainFrame
    log_frame = LogFrame()
    # и показываем
    log_frame.Show()

    # запускаем главный цикл обработки сообщений
    app.MainLoop()