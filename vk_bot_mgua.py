class analysis():

    def __init__(self):

        self.url = "https://msal.ru/melk/"
        from selenium import webdriver
        from time import sleep
        import pandas as pd

        self.webdriver = webdriver
        self.sleep = sleep
        self.pd = pd

    def gen_pd_table(self,html_for_table):
        pd = self.pd
        table = pd.read_html(html_for_table,
                         skiprows = 2,
                         header = 0,
                         attrs = {'id': 'eventtable'} #'class': 'text-center'},
                        )
        table = table[0].drop(index=[0])
        return table



    def parse_table(self,program,condition,name_of_the_direction):
        try:
            options = self.webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = self.webdriver.Chrome(executable_path='', options=options)
            sleep = self.sleep

            driver.get(url = self.url)


            element_city = driver.find_element_by_name('step1')
            branch = element_city.find_element_by_id('years')
            branch.click()
            city = branch.find_element_by_id('')
            city.click()
            sleep(1)


            element_programm = driver.find_element_by_id('step2')
            proggram_study = element_programm.find_element_by_id('years')
            proggram_study.click()
            curerent_programm = proggram_study.find_element_by_id(program)
            curerent_programm.click()
            sleep(1)

            condition_education = driver.find_element_by_id('step3')
            condition_education_but = condition_education.find_element_by_id('years')
            condition_education_but.click()
            type_education = condition_education_but.find_element_by_id(condition)
            type_education.click()
            sleep(1)

            type_of_list = driver.find_element_by_id('step4')
            type_of_list = type_of_list.find_element_by_id('model')
            type_of_list.click()
            currrent_type_of_list = type_of_list.find_element_by_xpath("//option[@data-valuse='" + name_of_the_direction + "']")
            currrent_type_of_list.click()
            sleep(5)

            table_of_list = driver.find_element_by_id('eventtable')
            table_of_list = table_of_list.find_element_by_xpath("//select[@title='Выбрать количество строк на странице']")
            table_of_list.click()
            table_of_list = table_of_list.find_element_by_xpath("//option[@value='all']")
            table_of_list.click()
            sleep(1)

            html_for_table = driver.page_source

            
            sleep(1)

        finally:
            driver.close()

        return html_for_table
    
    
    
##################################################################    
    
    
    
    
    def counting_applications_for_paid_training(self,table):
        count = len(table[table["Согласие на зачисление"] == "Да"])
        return count

    def analaze_paid_brach(self):
        print("Анализ платныx направлений")

        full_path = [ ]
        
        paid_brach_data = []

        for i in range(len(full_path)):
            try:
                html_for_tabl = self.parse_table(full_path[i][0],full_path[i][1],full_path[i][2])
                print(f"Скачались данные по направлению {full_path[i]}")
                table = self.gen_pd_table(html_for_tabl)
                print(f"Таблица данных по направлению {full_path[i]} подготовилась")
                count = self.counting_applications_for_paid_training(table)
                print(f"Подано согласий на зачисление {count} из {full_path[i][3]} доступных")
                print(f"Таблица данных по направлению  {full_path[i]} обработалась")
                paid_brach_data.append([full_path[i][2], count, full_path[i][3]])
            except Exception as e:
                print(f"Ошибка по направлению {full_path[i]}")
                print(e)
                paid_brach_data = None
        
        return paid_brach_data
    
    
    
#########################################################################    
    
    
    def counting_applications_for_budget_training(self,table):
        Our_number = table[table["СНИЛС / ID присвоенное ВУЗом"].str.match('')]["№"]
        analaze_list = (table[table["№"] < Our_number.values[0]])
        
        statistic_for_budget = []
        
        statistic_for_budget.append(len(analaze_list))
        statistic_for_budget.append(len(analaze_list[table["Согласие в другом конкурсе"] == "Нет"]))
        statistic_for_budget.append(len(analaze_list[table["Согласие на зачисление"] == "Да"]))
        statistic_for_budget.append(min(analaze_list[table["Согласие на зачисление"] == "Да"]["Сумма баллов"]))
        return statistic_for_budget
    
    def analaze_budget_brach(self):
    
        full_path = 
       ]
        
        paid_brach_data = []

        for i in range(len(full_path)):
            print(i)
            try:
                html_for_tabl = self.parse_table(full_path[i][0],full_path[i][1],full_path[i][2])
                print(f"Скачались данные по направлению {full_path[i]}")
                table = self.gen_pd_table(html_for_tabl)

vk_session = vk_api.VkApi(token = "") 
longpoll = VkLongPoll(vk_session)
New_analysis = analysis()


def sender(id_sender, text): # функция отправления
    vk_session.method('messages.send', {'user_id' : id_sender, 'message' : text, 'random_id' : 0}) # это просто запомнить
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            msg = event.text.lower() # последние сообщение пользователя
            id_sender = event.user_id #id беседы в который был ивент 
            if msg == 'привет': 
                
                sender(id_sender, 'Приветики') # отправляем в sender(id, text) id беседы и текст
            elif msg == ('отчет' or 'отчёт'):
                sender(id_sender, "Начинаю сбор информации")
                sender(id_sender, "Информация по платным направлениям")
                paid_data = New_analysis.analaze_paid_brach()
                if paid_data != None:
                    for i in range(len(paid_data)):  
                        text = f"На направление {paid_data[i][0]} поданой согласий {paid_data[i][1]} из {paid_data[i][2]} свободных мест на направлении"
                        sender(id_sender, text)
                else:
                    print("Ошибка")
                    sender(id_sender, "Произошла какая-то ошибка")
    
                sender(id_sender, "Информация по бюджетным направлениям")

                budget_data = New_analysis.analaze_budget_brach()
                if budget_data != None:
                    for i in range(len(budget_data)):  
                        text = f"На направление {budget_data[i][0]}, в котором бюджетных мест:{budget_data[i][5]}\n Вся статистика приведенная ниже относиться только к тем, у кого баллов больше, чем у тебя.\n Всего в списке:{budget_data[i][1]}\n Потенциальных конкурентов(тех кто не подал соглапсие в другой конкурс):{budget_data[i][2]}\n Поданно согласий на зачисление: {budget_data[i][3]}\n Балл последнего подавшего на зачисление зачисление перед тобой: {budget_data[i][4]}\n"                    
                        sender(id_sender, text)
                else:
                    print("Ошибка")
                    sender(id_sender, "Произошла какая-то ошибка")
class analysis():
    
    
    def __init__(self):

        self.url = "https://msal.ru/melk/"
        from selenium import webdriver
        from time import sleep
        import pandas as pd

        self.webdriver = webdriver
        self.sleep = sleep
        self.pd = pd
        
    def gen_pd_table(self,html_for_table):
        pd = self.pd
        table = pd.read_html(html_for_table,
                         skiprows = 2,
                         header = 0,
                         attrs = {'id': 'eventtable'} #'class': 'text-center'},
                        )
                        text = f"На направление {budget_data[i][0]}, в котором бюджетных мест:{budget_data[i][5]}\n Вся статистика приведенная ниже относиться только к тем, у кого баллов больше, чем у тебя.\n Всего в списке:{budget_data[i][1]}\n Потенциальных конкурентов(тех кто не подал соглапсие в другой конкурс):{budget_data[i][2]}\n Поданно согласий на зачисление: {budget_data[i][3]}\n Балл последнего подавшего на зачисление зачисление перед тобой: {budget_data[i][4]}\n"                    

                        sender(id_sender, text)
                    else:
                    print("Ошибка")
                    sender(id_sender, "Произошла какая-то ошибка")
