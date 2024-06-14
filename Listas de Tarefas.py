import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")

        # Criar elementos da interface
        self.label = tk.Label(self.master, text="Digite a tarefa:")
        self.label.pack()
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        self.add_button = tk.Button(self.master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()
        self.tasks_listbox = tk.Listbox(self.master)
        self.tasks_listbox.pack()
        self.remove_button = tk.Button(self.master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

        self.tasks = []
        self.update_tasks_listbox()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.entry.delete(0, tk.END)
            self.update_tasks_listbox()

    def remove_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            self.tasks.remove(selected_task)
            self.update_tasks_listbox()
        else:
            print("Nenhuma tarefa selecionada.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()