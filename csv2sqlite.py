#!/usr/bin/python

"""Take a CSV file, read it into memory, use the first row as the column 
names, and make an sqlite database out of it."""

import csv
import sqlite3
import sys

def slurp(csv_filename):
    db_name = csv_filename.split(".")[0]
    with open(csv_filename) as csv_filehandle:
        reader = csv.reader(csv_filehandle)
        header = list
        for count, value in enumerate(reader):
            if count == 0:
                header = value
        #print(header)
                makeTable(db_name, header)
            else:
                writeRow(db_name, header, value)


def makeTable(db_name, header):
    conn = sqlite3.connect(db_name+".db")
    conn.execute('pragma journal_mode=wal')
    cursor = conn.cursor()
    table_creation_string = f"create table {db_name} (id integer primary key"
    for column in header:
        table_creation_string += f", {column} text"
    table_creation_string += ")"
    #print(table_creation_string)
    try:
        cursor.execute(table_creation_string)
    except sqlite3.OperationalError:
        cursor.execute(f"drop table {db_name}")
        cursor.execute(table_creation_string)
    conn.commit()


def writeRow(db_name, header, row):
    conn = sqlite3.connect(db_name+".db")
    cursor = conn.cursor()
    if len(row) != len(header):
        print("Error: header length and row length don't match.")
        print(f"Header: {header}")
        print(f"Row: {row}")
    else:
        row_insert_string = f"insert into {db_name} ("
        column_names = ""
        for column_name in header:
            column_names += column_name + ","
        column_names = column_names[:-1]
        question_marks = len(header)*"?,"
        question_marks = question_marks[:-1]
        #print(f"Column Names: {column_names}")
        #print(f"Question Marks: {question_marks}")
        row_insert_string += f"{column_names}) values ({question_marks})"
        #print(row_insert_string)
        
        cursor.execute(row_insert_string, row)
        conn.commit()



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: csv2sqlite.py csvFilename")
        #slurp("tmp.csv")
    else:
        #print(sys.argv)
        slurp(sys.argv[1])