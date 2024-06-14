import tkinter as tk

class BMICalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de IMC")

        self.label_height = tk.Label(master, text="Altura (metros):")
        self.label_height.pack()
        self.entry_height = tk.Entry(master)
        self.entry_height.pack()

        self.label_weight = tk.Label(master, text="Peso (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(master)
        self.entry_weight.pack()

        self.button_calculate = tk.Button(master, text="Calcular", command=self.calculate_bmi)
        self.button_calculate.pack()

        self.label_result = tk.Label(master, text="")
        self.label_result.pack()

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.label_result.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            self.label_result.config(text="Por favor, digite valores numéricos válidos.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            message = "Você está abaixo do peso."
        elif bmi < 25:
            message = "Você está no peso normal."
        elif bmi < 30:
            message = "Você está com sobrepeso."
        else:
            message = "Você está com obesidade."
        self.label_result.config(text=f"{message} Seu IMC é: {bmi:.2f}")

root = tk.Tk()
app = BMICalculator(root)
root.mainloop()