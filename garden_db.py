import tkinter as tk
from tkinter import ttk, messagebox

class NurseryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nursery Plant Management System")

        self.plants = []  # Each item: {'name': ..., 'category': ..., 'price': ..., 'count': ...}

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Nursery Plant Management", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=4, pady=10)

        # Input form
        ttk.Label(self.root, text="Plant Name:").grid(row=1, column=0, sticky="e")
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=1, column=1)

        ttk.Label(self.root, text="Category:").grid(row=2, column=0, sticky="e")
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self.root, textvariable=self.category_var, state="readonly")
        self.category_dropdown["values"] = ["Fruit", "Vegetable", "Bird Nest"]
        self.category_dropdown.grid(row=2, column=1)
        self.category_dropdown.current(0)

        ttk.Label(self.root, text="Price (₹):").grid(row=3, column=0, sticky="e")
        self.price_entry = ttk.Entry(self.root)
        self.price_entry.grid(row=3, column=1)

        ttk.Label(self.root, text="Count:").grid(row=4, column=0, sticky="e")
        self.count_entry = ttk.Entry(self.root)
        self.count_entry.grid(row=4, column=1)

        # Buttons
        ttk.Button(self.root, text="Add / Update Plant", command=self.add_or_update_plant).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Delete Selected Plant", command=self.delete_plant).grid(row=5, column=2, columnspan=2)

        # Treeview to show the plants
        self.tree = ttk.Treeview(self.root, columns=("Category", "Price", "Count"), show="headings", height=10)
        self.tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        self.tree.heading("Category", text="Category")
        self.tree.heading("Price", text="Price (₹)")
        self.tree.heading("Count", text="Count")
        self.tree["columns"] = ("Name", "Category", "Price", "Count")
        self.tree.column("Name", width=120)
        self.tree.column("Category", width=100)
        self.tree.column("Price", width=80)
        self.tree.column("Count", width=80)
        self.tree.heading("Name", text="Plant Name")
        self.tree.bind("<ButtonRelease-1>", self.fill_form_from_selection)

        # Total summary
        self.total_label = ttk.Label(self.root, text="Total Plant Types: 0", font=("Helvetica", 12))
        self.total_label.grid(row=7, column=0, columnspan=4, pady=5)

    def add_or_update_plant(self):
        name = self.name_entry.get().strip()
        category = self.category_var.get()
        price = self.price_entry.get().strip()
        count = self.count_entry.get().strip()

        if not name or not price or not count:
            messagebox.showwarning("Input Error", "All fields must be filled.")
            return

        try:
            price = float(price)
            count = int(count)
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be a number and count must be an integer.")
            return

        # Check if plant already exists
        for plant in self.plants:
            if plant["name"].lower() == name.lower():
                plant["category"] = category
                plant["price"] = price
                plant["count"] = count
                self.refresh_treeview()
                self.clear_entries()
                return

        # Add new plant
        self.plants.append({
            "name": name,
            "category": category,
            "price": price,
            "count": count
        })

        self.refresh_treeview()
        self.clear_entries()

    def delete_plant(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Delete", "Please select a plant to delete.")
            return

        plant_name = self.tree.item(selected[0])["values"][0]

        self.plants = [plant for plant in self.plants if plant["name"] != plant_name]
        self.refresh_treeview()

    def refresh_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for plant in self.plants:
            self.tree.insert("", "end", values=(plant["name"], plant["category"], f"{plant['price']:.2f}", plant["count"]))

        self.total_label.config(text=f"Total Plant Types: {len(self.plants)}")

    def fill_form_from_selection(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0])["values"]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[0])
        self.category_var.set(values[1])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, values[2])
        self.count_entry.delete(0, tk.END)
        self.count_entry.insert(0, values[3])

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.count_entry.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = NurseryApp(root)
    root.mainloop()
