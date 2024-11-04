import cProfile
from Original_code.Inventory_management_software import InventoryManager  # Import your main class

def run_program():
    manager = InventoryManager()  # Initialize your inventory manager
    manager.run()  # Run the main functionality

if __name__ == "__main__":
    # Profile the main functionality and save the output to a .stats file
    cProfile.run('run_program()', 'original_profile.stats')
