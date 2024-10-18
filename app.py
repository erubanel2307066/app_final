import tkinter as tk
from tkinter import PhotoImage  # Importamos PhotoImage para cargar la imagen

# Definir las funciones antes de usarlas
def agregar_tarea():
    tarea = entry_task.get()
    if tarea != "":
        listbox_tasks.insert(tk.END, tarea)
        entry_task.delete(0, tk.END)
        
#creamos la funcion eleminr tarea 
def eliminar_tarea():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas proyecto Hybridge")
root.geometry("500x600")

# Cargar la imagen del logo (asegurate de que el archivo PNG este en la misma carpeta o proporciona la ruta completa)
logo_image = PhotoImage(file="GACEEnt2.png")  # Asegurate de cambiar 'ruta_del_logo.png' por la ruta de tu archivo PNG

# Añadir la imagen del logo en un Label y centrarlo en la parte superior
logo_label = tk.Label(root, image=logo_image)
logo_label.grid(row=25, column=0, columnspan=2, pady=10)

# Campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=35)
entry_task.grid(row=1, column=0, padx=10, pady=10)

# Botón para agregar tareas con color de fondo y texto
btn_add = tk.Button(root, text="Agregar Tarea", command=agregar_tarea, bg="#4CAF50", fg="white")
btn_add.grid(row=1, column=1, padx=10)

# Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=25, height=10)
listbox_tasks.grid(row=2, column=0, columnspan=2, pady=10)

# Boton para eliminar tareas con color de fondo y texto
btn_delete = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea, bg="#f44336", fg="white")
btn_delete.grid(row=3, column=0, columnspan=2, pady=10)

# Hacer que la ventana sea responsiva
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Ajustar el listbox para que se expanda con la ventana
listbox_tasks.grid(sticky="nsew")

# Iniciar el loop principal de la interfaz
root.mainloop()