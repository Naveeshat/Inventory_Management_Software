import csv
from datetime import datetime

class Tool:
    def __init__ (self,name,quantity,location,last_maintenance,serial_number,category):
      self.name = name
      self.quantity = quantity
      self.location = location
      self.last_maintenance = last_maintenance
      self.serial_number =serial_number 
      self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.quantity} in {self.location},serial:{self.serial_number}, Last Maintenance: {self.last_maintenance}"
   
class Inventory:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)
        print(f"Added tool: {tool.name}")

    def remove_tool (self, serial_number):
        for tool in self.tools:
           if tool.serial_number == serial_number:
               self.tools.remove(tool)
               print(f"Removed tool with serial number: {serial_number}")
               return
        print(f"Tool with serial number {serial_number} not found.")
    
    def update_tool(self, serial_number, name=None, quantity=None, location=None, last_maintenance=None, category=None) :
        for tool in self.tools:
            if tool.serial_number == serial_number:
                if name is not None:
                    tool.name = name
                if quantity is not None:
                    tool.quantity = quantity
                if location is not None:
                    tool.location = location
                if last_maintenance is not None:
                    tool.last_maintenance = last_maintenance
                if category is not None:
                    tool.category = category
                print(f"Updated tool with serial number: {serial_number}")
                return
        print(f"Tool with serial number {serial_number} not found.")
    
    def generate_report(self):
        with open('inventory_report.csv','w', newline='') as file:
           writer = csv.writer(file)
           writer.writerow(['Name','Quantity','Location','Last Maintenance','Serial Number', 'Category'])
           for tool in self.tools:
               writer.writerow([tool.name, tool.quantity, tool.location, tool.last_maintenance, tool.serial_number, tool.category])
        print("Report generated: inventory_report.csv")
    
    def validate_input(self, input_value, expected_type):
        if not isinstance(input_value, expected_type):
           raise ValueError(f"Expected input of type {expected_type.__name__}, got {type(input_value).__name__}")
                          
class InventoryManager:
    def __init__(self):
       self.inventory = Inventory()
    
    def run(self):
        while True:
            print("\noptions: 1) Add Tool 2) Remove Tool 3) Update Tool 4) Generate Report 5) Exit")
            choice = input("choose an option: ")
            if choice == '1':
               self.add_tool()
            elif choice == '2':
               self.remove_tool()
            elif choice == '3':
               self.update_tool()
            elif choice == '4':
                self.inventory.generate_report()
            elif choice == '5' :
                print ("Exiting the program. ")
                break
            else:
                print("Invalid choice, please try again. ")

    def add_tool(self):
       name = input("Enter tool name: ")
       quantity = int(input("Enter quantity: "))
       location = input("Enter location: ")
       last_maintenance = input("Enter last maintenance date(YYYY-MM-DD): ")
       serial_number = input("Enter serial number: ")
       category = input("Enter category: ")
       new_tool = Tool(name, quantity,location, last_maintenance, serial_number,category)
       self.inventory.add_tool(new_tool)

    def remove_tool(self):
        serial_number = input("Enter serial number of the tool to remove: ")
        self.inventory.remove_tool(serial_number)

    def update_tool(self): 
        serial_number = input("Enter serial number of the tool to update: ")
        name = input("Enter new name ( leave blank for no change): ")
        quantity = input("Enter new quantity(leave blank for no change): ") or None
        location = input("Enter new location (leave blank for no change): ") or None
        last_maintenance = input("Enter new last maintenance date (leave blank for no change): ") or None
        category = input("Enter new category (leave blank for no change): ") or None
        self.inventory.update_tool(serial_number,name, quantity, location, last_maintenance, category)

if __name__ == "__main__":
    manager =   InventoryManager()
    manager.run()

