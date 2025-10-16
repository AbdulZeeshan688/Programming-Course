# TASK LEARN ABOUT THE FUNCATIONS IN PYTGONimport subprocess
def initialize():
    print("Initialization complete.")
def process_data(data):
    return data.upper()
def save_results(results):
    print(f"Saving results: {results}")

def main():
    initialize()
    data = "Sample Data"
    processd_data = process_data(data)
    save_results(processd_data)

main() 