#!/usr/bin/env python3

from datetime import datetime
import typer
from pathlib import Path
from typing import List, Optional
import re
import pandas as pd
import random
import string
import os

app = typer.Typer(add_completion=False)


@app.command()
def main(
    rows: int = typer.Option(
        50, help="The number of rows that will output in the csv file."
    ),
    output_path: Optional[Path] = typer.Option(
        "./", help="The path of where the csv file will be saved."
    ),
    column_data: Optional[List[str]] = typer.Option(
        ..., help="The input data to be saved in the file."
    ),
):
    """
    Outputs a csv with generated data for columns specified using --column-data.
    """

    parsed_column_data = parseColumnData(column_data)
    generated_data = generateDataFrame(parsed_column_data, rows)

    writeToCsvFile(output_path, generated_data)


def parseColumnData(column_data):
    """
    Parses the column_data option from a string of tuples to list of tuples.
    """

    columns = []
    for tuple_string in column_data:
        try:
            columns += [
                eval(ele.strip()) for ele in re.split("(?<=\\)),", tuple_string)
            ]
        except Exception as e:
            print("Ivalid format for option column-data.")
            print(
                "Use format: --column-data \"('int_data', 'integer'), ('string_data', 'string')\""
            )
            exit(1)

    return columns


def generateDataFrame(column_data, num_rows):
    """
    Returns a `DataFrame` with `num_rows` of genrated data for the column_data option.
    """

    df = pd.DataFrame()
    columns = []
    letters = string.ascii_lowercase

    for column in column_data:
        column_name = column[0]
        columns.append(column_name)
        column_data_type = column[1]

        column_data = []

        # Generate data for columns
        for i in range(num_rows):
            if column_data_type == "string":
                column_data.append("".join(random.choice(letters) for i in range(10)))

            elif column_data_type == "integer":
                column_data.append(random.randint(0, 999999))

            else:
                print("Ivalid format for option column-data.")
                print(
                    "Use format: --column-data \"('int_data', 'integer'), ('string_data', 'string')\""
                )
                exit(1)

        df[column_name] = column_data

    return df


def writeToCsvFile(path, df):
    """
    Writes a `DataFrame` to a csv file for a given `Path`.
    Filename is generated from the current time.
    """

    datetime_format = "%Y-%m-%d-%H_%M_%S"
    date = datetime.now()
    filename = date.strftime(datetime_format) + ".csv"

    if not os.path.exists(path):
        os.makedirs(path)

    df.to_csv(os.path.join(path, filename))


if __name__ == "__main__":
    app()
