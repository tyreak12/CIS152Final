import tkinter as tk
from tkinter import messagebox
from collections import deque
import heapq

# Creating "node" class
class Item:
    def __init__(self, id, name, price, quantity, priority):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.priority = priority

# creating inventory/linked list class 
class Inventory:
    def __init__(self):
        self.items = deque()
        self.priority_queue = []
    # Add method 
    def add_item(self, item):
        self.items.append(item)
        heapq.heappush(self.priority_queue, (item.priority, item))
    
    # Remove method
    def remove(self, id):
        for i in range(len(self.items)):
            if self.items[i].id == id:
                del self.items[i]
                return True
        return False
    
    
    # creating method to update price
    def update_price(self, id, price):
        for item in self.items:
            if item.id == id:
                item.price = price
                return True
        return False
    def update_quantity(self, id, quantity):
        for item in self.items:
            if item.id == id:
                item.quantity = quantity
                return True
        return False

    #  Linear Search method
    def linear_search(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None
    
    def print_queue(self):
        return[item[1].name for item in self.priority_queue]

# Creating class for GUI 
class App(tk.Tk):
    def __init__(self, inventory):
        tk.Tk.__init__(self)
        self.inventory = inventory
        self.title("inventory Manager")
        self.geometry("500x500")
    
    #creating text box for ID
        self.id_label = tk.Label(self, text="Item ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

    #creating text box for item
        self.item_label = tk.Label(self, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(self)
        self.item_entry.pack()
    
    #creating text box for price
        self.price_label = tk.Label(self, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()
    
    #creating text box for quanity
        self.quantity_label = tk.Label(self, text="Quantity: ")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()
    
    #creating text box for priority
        self.priority_label = tk.Label(self, text="Priority")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(self)
        self.priority_entry.pack()

    # creating add button
        self.add_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Item", command=self.remove_item)
        self.delete_button.pack()

        self.update_price_button = tk.Button(self, text="Update Price", command=self.update_price)
        self.update_price_button.pack()

        self.update_quantity_button = tk.Button(self, text="Update Quantity", command=self.update_quantity)
        self.update_quantity_button.pack()

        self.search_button = tk.Button(self, text="Search Item", command=self.search_item)
        self.search_button.pack()

        self.print_priority_queue_button = tk.Button(self, text="Print Priority Queue", command=self.print_queue)
        self.print_priority_queue_button.pack()

        

    def clear_entry(self):
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)

    def add_item(self):
        id = self.id_entry.get()
        name = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        priority = self.priority_entry.get()
        item = Item(id, name, price, quantity, priority)
        self.inventory.add_item(item)
        messagebox.showinfo("Success", f"Item: {name} succesfully added!")
        self.clear_entry()

    def remove_item(self):
        id = self.id_entry.get()
        if self.inventory.delete_item(id):
            messagebox.showinfo(f"Item: {self.name} successfully removed")
        self.clear_entry()
    
    def update_price(self):
        price = self.price_entry.get()
        id = self.id_entry.get()
        if self.inventory.update_price(id, price):
            messagebox.showinfo("Success!", f"{self.name} Price updated!")
        else:
            messagebox.showinfo("Failure", "item not found")
        self.clear_entry()
    
    def update_quantity(self):
        quantity = self.quantity_entry.get()
        id = self.id_entry.get()
        if self.inventory.update_quantity(id, quantity):
            messagebox.showinfo("Success!", f"{self.name} Quantity updated!")
        else:
            messagebox.showinfo("Failure", "item not found")
        self.clear_entry()

    def search_item(self):
        id = self.id_entry.get()
        item = self.inventory.linear_search(id)
        if item:
            messagebox.showinfo("Success", f"Item found! \nName: {item.name}\nPrice: {item.price}\nQuantity: {item.quantity}")
        else:
            messagebox.showerror("Item not found!", f"Item {self.name} not found!")
    
    def print_queue(self):
        items = self.inventory.print_queue()
        messagebox.showinfo("Priority Queue", "\n".join(items))

inventory = Inventory()
app = App(inventory)
app.mainloop()
    












