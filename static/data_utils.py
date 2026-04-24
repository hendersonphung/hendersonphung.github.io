"""Data related utility functions."""

__author__ = ["730871000", "730854494"]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted


"""These are the functions we wrote/will write in class!"""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Visualize the first N rows of table."""
    # Produce a dict[str, list[str]] table with only the first N rows.
    result: dict[str, list[str]] = {}  # Establish a empty dictionary, return

    # Where the table will look like: {'column name': ["", ""]}
    # Loop through each 'column name' (key) in table (dict)
    for column in table:
        # Establish empty list for every key to store values inside the dict's list[str]
        s: list[str] = []

        # Loop through first N items in the table's list[str]
        for i in range(N):
            # Append the str at index to s list
            s.append(table[column][i])
        # Result dict at column key takes on s list, which has the first N rows of list.
        result[column] = s

    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Select relevant columns."""
    # Produce a dict[str, list[str]] table with specific columns.
    result: dict[str, list[str]] = {}
    # Establish empty dict, will be returned

    # Loop through columns list
    for column in columns:
        # Assign the items in column list as a key in the result dict and the values of
        # the key are pulled from the table at that column.
        result[column] = table[column]
    return result


def concat(t1: dict[str, list[str]], t2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine different sources of data."""
    # Produce a dict[str, list[str]] from two tables (sources)
    result: dict[str, list[str]] = {}
    # Establish empty dict, will be returned

    # Loop through each key in dict t1
    for column in t1:
        # Assign result dict at key with list[str] at same key in t1
        result[column] = t1[column]

    for column in t2:
        # If key in result dict matches key at t2
        if column in result:
            # Append the list established at that key
            # For index in range of the list[str]
            for i in range(len(t2[column])):
                # Append each item of list to result dict at the same column.
                result[column].append(t2[column][i])
        # Otherwise, assign key at result to list[str] of t2 at key
        else:
            result[column] = t2[column]
    return result


def count(input: list[str]) -> dict[str, int]:
    """Count number of times value appeared in input list."""
    # Produce dict[str, int] given a list[str]

    # Each key in dict is a unique value in input list
    # Each int in dict is number of times it appears in input list
    # Establish empty dict
    result: dict[str, int] = {}

    # Loop through each item in input list
    # Check to see if item has in dictionary as key
    for item in input:
        # If item found in dict, increase value of key by 1
        if item in result:
            result[item] += 1
        # If not found in dict, assign initial count of 1 to key
        else:
            result[item] = 1
        # Return resulting dict
    return result


def average_score(
    table: dict[str, list[str]], column: list[str]
) -> dict[str, list[str]]:
    """Calculate avg scores of column results and makes it tabulable."""

    result: dict[str, list[str]] = {"Column Names": [], "Average Scores": []}

    for col in column:
        count: int = 0
        for i in range(len(table[col])):
            count += int(table[col][i])

        average: float = count / len(table[col])

        result["Column Names"].append(col)
        result["Average Scores"].append(f"{average} out of 7")

    return result
