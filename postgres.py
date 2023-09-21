import psycopg2
import pandas as pd


df = pd.read_csv('C:\\Users\\91907\\OneDrive\\Documents\\vscode\\Python\\Web scraping\\PropReturns\\data_english.csv')

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host="localhost", 
        port="5432", 
        database="PropReturns",
        user="postgres", 
        password="tsopserg#7@"
    )

    cursor = conn.cursor()
    
    table_name = "Real_Estate"

    # Create table
    create_table_command = ('''CREATE TABLE IF NOT EXISTS Real_Estate(
            serial_number       INTEGER NOT NULL,
            document_number     INTEGER PRIMARY KEY,
            document_type       TEXT NOT NULL,
            revenue_office      TEXT NOT NULL,
            reg_year            DATE NOT NULL,
            Buyer_name          TEXT,
            Seller_name         TEXT,
            Other_information   TEXT NOT NULL,
            List_no_2           TEXT NOT NULL
        )'''
    )

    create_table_command = create_table_command.rstrip(", ")

    try:
        cursor.execute(create_table_command)
        conn.commit()
        print("Table created successfully.")

        for index, row in df.iterrows():
            insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s']*len(df.columns))})"
            cursor.execute(insert_query, tuple(row))
        

        conn.commit()
        print("Data inserted successfully.")
        
    except Exception as error:
        print(error)
    

except Exception as error:
    print(error)

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()