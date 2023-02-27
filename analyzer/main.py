import csv

from rich.table import Table
from rich.console import Console

# Do not alter
def load_file(filename: str = "") -> list:
    """ Opens a CSV file """
    data = []
    with open(filename, "r") as fh:
        reader = csv.reader(fh)
        for row in reader:
            data.append(row)
    return data

def save_file(filename: str = "", columns: list = [], rows: list = []) -> None:
    """ Saves a CSV file """
    data = [columns] + rows
    with open(filename, "w") as fh:
        writer = csv.writer(fh, delimiter = ",")
        for row in data:
            writer.writerow(row)

def norm_types(data: list = []) -> list:
    """ PROF: I wrote this improvement because it's really annoying not to? """
    for item in data:
        idx = data.index(item)
        try:
            val = int(item)
            data[idx] = val
        except:
            pass
    return data

def display_table() -> None:
    table = Table(title="NEIGHBORHOOD SURVEY RESULTS")
    for col in COLS:
        table.add_column(col)
    for row in ROWS:
        row = [str(elem) for elem in row]
        table.add_row(*row)
    console = Console()
    console.print(table)

def sorter(column: str = "ID") -> None:
    idx = col_idx(column)
    ROWS.sort(key = lambda ROWS: ROWS[idx])
# Do not alter

# TODO: Create get_row function per README

# TODO: Create get_col function per README

# TODO: Create counter function per README

# TODO: Create min_value function per README

# TODO: Create max_value function per README

# TODO: Create get_mode function per README

# TODO: Create get_median function per README
        
# TODO: Create avg_column function per README

def main():
    # Do not alter
    data = load_file(filename = "data/responses.csv")
    global COLS 
    COLS = data[0]
    global ROWS 
    ROWS = data[1:]
    # Do not alter
    
    while True:

        print("1. Save data")
        print("2. Display data")
        print("0. Quit")
        
        response = int(input("Enter an operation to perform: "))
        
        # Do not alter
        if response == 0:
            break
        elif response == 1:
            save_file(
                filename = "data/responses.csv",
                columns = cols,
                rows = rows
            )
        elif response == 2:
            display_table()
        # Do not alter
        """
            TODO: Create menu structure to call correct functions.
        """

if __name__ == "__main__":
    main()
