import tkinter as tk
from tkinter import messagebox

class RecipeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe Generator")

        # Ingredients List
        self.ingredients_listbox = tk.Listbox(master)
        self.ingredients_listbox.pack(pady=10)

        # Entry for adding ingredients
        self.new_ingredient_entry = tk.Entry(master)
        self.new_ingredient_entry.pack(pady=5)

        # Buttons for adding and removing ingredients
        add_button = tk.Button(master, text="Add Ingredient", command=self.add_ingredient)
        add_button.pack(pady=5)

        remove_button = tk.Button(master, text="Remove Ingredient", command=self.remove_ingredient)
        remove_button.pack(pady=5)

        # Button to generate recipes
        generate_button = tk.Button(master, text="Generate Recipes", command=self.generate_recipes)
        generate_button.pack(pady=10)

    def add_ingredient(self):
        ingredient = self.new_ingredient_entry.get()
        if ingredient:
            self.ingredients_listbox.insert(tk.END, ingredient)
            self.new_ingredient_entry.delete(0, tk.END)

    def remove_ingredient(self):
        selected_index = self.ingredients_listbox.curselection()
        if selected_index:
            self.ingredients_listbox.delete(selected_index)

    def generate_recipes(self):
        ingredients = self.ingredients_listbox.get(0, tk.END)
        if not ingredients:
            messagebox.showinfo("Recipe Generator", "Please add ingredients first.")
            return

        # Here you can implement your recipe generation logic using the 'ingredients' list
        # For simplicity, let's just display a message with the ingredients for now.
        recipe_message = "Generated Recipe:\n\n" + "\n".join(ingredients)
        messagebox.showinfo("Recipe Generator", recipe_message)


def main():
    root = tk.Tk()
    app = RecipeGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()