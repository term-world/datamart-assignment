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

def col_idx(column: str = "") -> int:
    return COLS.index(column)

def get_row(row_num: int = 0) -> list:
    return ROWS[row_num]

def get_col(column: str = "") -> list:
    values = []
    idx = col_idx(column)
    for row in ROWS:
        values.append(row[idx])
    return norm_types(values)

def counter(value: str = "") -> int:
    total = 0
    for row in ROWS:
        total += row.count(value)
    return total

def min_value(column: str = "") -> int:
    minima = 5
    idx = col_idx(column)
    for row in ROWS:
        value = int(row[idx])
        if value < minima:
            minima = value
    return minima

def max_value(column: str = "") -> int:
    maxima = 1
    idx = col_idx(column)
    for row in ROWS:
        value = int(row[idx])
        if value > maxima:
            maxima = value
    return maxima

def get_mode(column: str = "") -> int:
    value = 0
    times = 0
    data = get_col(column)
    for elem in data:
        times = data.count(elem)
        if times > count:
            value = elem
    return elem

def get_median(column: str = "") -> int:
    data = get_col(column)
    mid_point = len(data) // 2
    return data[mid_point]
        

def avg_column(column: str = "") -> float:
    values = get_col(column)
    return sum(values) / len(values)

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
        print("3. Get a single row")
        print("4. Count a value in the table")
        print("5. Get minimum of a column")
        print("6. Get maximum of a column")
        print("7. Average a column")
        print("8. Sort by a column")
        print("9. Get the mode of a column")
        print("10. Get the median of a column")
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
        elif response == 3:
            row_id = int(input("Enter row id to fetch: "))
            row = get_row(rows = rows, row_num = row_id)
            print(f"Fetched row: {row}")
        elif response == 4:
            to_count = input("Value to count occurences of: ")
            count = counter(value = to_count)
            print(f"Count of {to_count}: {count}")
        elif response == 5:
            column = input("Column to minimize: ")
            minima = min_value(column)
            print(f"Minimum of {column}: {minima}")
        elif response == 6:
            column = input("Column to maxmize: ")
            maxima = max_value(column)
            print(f"Maximum of {column}: {maxima}")
        elif response == 7:
            column = input("Column to average: ")
            average = avg_column(column)
            print(f"Average of {column}: {average}")
        elif response == 8:
            column = input("Column to sort on: ")
            sorter(column)
            display_table()
        elif response == 9:
            column = input("Column to get mode: ")
            mode = get_mode(column)
            print(f"Mode of {column}: {mode}")
        elif response == 10:
            column = input("Column to get median: ")
            sorter(column)
            middle = get_median(column)
            print(f"Median of {column}: {median}")

if __name__ == "__main__":
    main()