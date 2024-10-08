from connection import get_connection

def create_table(filename):
    with get_connection() as conn:
        if conn is None:
            print('Failed to connect to the database')
            return

        with open(filename, 'r') as file:
            sql_file = file.read()

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql_file)
                conn.commit()
                print('Table created successfully')
        except Exception as e:
            conn.rollback()
            print(e)



