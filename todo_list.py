class Task:
    """
    Класс для описания задачи в списке задач
    :param title: заголовок задачи
    :param description: описание задачи
    :param data: дата создания задачи
    :param end_data: дата окончания задачи
    :param is_done: флаг завершенности задачи
    """
    def __init__(self, title, description, data=None, end_data=None, priority=None, is_done=False):   
        self.title = title
        self.description = description
        self.data = data
        self.end_data = end_data
        self.priority = priority
        self.is_done = is_done
        
        
    def info_display(self):
        """
        Метод для вывода информации о задаче
        """
        print(f"Задача: {self.title}")
        print(f"Описание: {self.description}")
        print(f"Дата создания: {self.data}")
        print(f"Дата окончания: {self.end_data}")
        print(f"Приоритет: {self.priority}")
        print(f"Флаг завершенности: {'Выполнено' if self.is_done else 'Не выполнено'}")     # Если задача не выполнена, то выводится сообщение "Не выполнено"
        print("----------------------------------------")
        
        
class TodoList:
    """
    Класс для описания списка задач
    """
    def __init__(self):
        self.tasks = [] 
    
    def add_task(self, title, description, data, end_data, priority, is_done):              
        """Метод для добавления задачи в список"""
        self.tasks.append(Task(title, description, data, end_data, priority, is_done))              # Добавляем задачу в список
      
        
    def update_task(self, index, title, description, data, end_data, priority, is_done):            
        """Метод для изменения задачи в списке"""
        if 0 <= index < len(self.tasks):                                                         # Если индекс задачи в пределах допустимого диапазона
            self.tasks[index].title = title
            self.tasks[index].description = description
            self.tasks[index].data = data
            self.tasks[index].end_data = end_data
            self.tasks[index].priority = priority
            self.tasks[index].is_done = is_done
        else:
            print("___________________________")
            print("Неверный индекс задачи")       
            print("___________________________")
            
    def delete_task(self, index):
        """Метод для удаления задачи в списке"""
        if 0 <= index < len(self.tasks):                          # Проверка на валидность индекса
            self.tasks.pop(index)                                  # Удаление задачи из списка
        else:
            print("___________________________")
            print("Неверный индекс задачи")       
            print("___________________________")
            
    def mark_as_done(self, index):
        """Метод для отметки задачи как выполненной"""
        if 0 <= index < len(self.tasks):                          # Проверка на валидность индекса
            self.tasks[index].is_done = True                       # Отметка задачи как выполненной
        else:
            print("___________________________")
            print("Неверный индекс задачи")       
            print("___________________________")
            
    def sort_by_priority(self):
        """Метод для сортировки задач по приоритету"""
        self.tasks.sort(key=lambda task: task.priority if task.priority is not None else float("inf"))   # Сортировка задач по приоритету
            
    def sort_by_end_date(self):
        """Метод для сортировки задач по дате окончания"""
        self.tasks.sort(key=lambda task: task.end_data if task.end_data is not None else float("inf"))    # Сортировка задач по дате окончания
        
    def display_tasks(self):
        """Метод для вывода всех задач в списке"""
        for index, task in enumerate(self.tasks, start=1):                  # Перебор задач в списке
            print(f'номер: {index}')                                         # Вывод номера задачи
            task.info_display()                                              # Вывод информации о задаче
        
if __name__ == "__main__":
    todo_list = TodoList()  
    
    while True:
        try:
            print(f"1. Добавить задачу")
            print(f"2. Вывести все задачи")
            print(f"3. Удалить задачу")
            print(f"4. Изменить задачу")
            print(f"5. Отметить задачу как выполненную")
            print(f"6. Сортировать задачи по приоритету")
            print(f"7. Сортировать задачи по дате окончания")
            print(f"8. Выход")
            
            command = input("Введите команду: ")
            
            if command == "1":
                title = input("Введите заголовок задачи: ")
                description = input("Введите описание задачи: ")
                data = input("Введите дату создания задачи: ")
                end_data = input("Введите дату окончания задачи: ")
                priority = input("Введите приоритет задачи: ")
                is_done = False  # По умолчанию задача не выполнена
                
                todo_list.add_task(title, description, data, end_data, priority, is_done)
            
            elif command == "2":
                todo_list.display_tasks()
                    
            elif command == "3":
                try:
                    index = int(input("Введите номер задачи для удаления: ")) - 1
                    todo_list.delete_task(index)
                    print(f'Задача удалена')
                except (IndexError, ValueError):
                    print("___________________________")
                    print("Неверный номер")       
                    print("___________________________")
                
            elif command == "4":
                try:
                    index = int(input("Введите номер задачи для изменения: ")) - 1
                    title = input("Введите заголовок задачи: ")
                    description = input("Введите описание задачи: ")
                    data = input("Введите дату создания задачи: ")
                    end_data = input("Введите дату окончания задачи: ")
                    priority = input("Введите приоритет задачи: ")
                    
                    todo_list.update_task(index, title, description, data, end_data, priority, todo_list.tasks[index].is_done)
                    print("Задача обновлена")
                except ValueError:
                    print("___________________________")
                    print("Неверный ввод")       
                    print("___________________________")
                
            elif command == "5":
                try:
                    index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                    todo_list.mark_as_done(index)
                    print("Задача отмечена как выполненная")
                except (IndexError, ValueError):
                    print("___________________________")
                    print("Неверный номер")       
                    print("___________________________")
                
            elif command == "6":
                todo_list.sort_by_priority()
                print("Задачи отсортированы по приоритету.")
                
            elif command == "7":
                todo_list.sort_by_end_date()
                print("Задачи отсортированы по дате окончания.")
                
            elif command == "8":
                break
        except Exception as e:
            print("___________________________")
            print(f"Произошла ошибка: {e}")       
            print("___________________________")