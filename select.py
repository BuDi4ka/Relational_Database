from connection import get_connection

def select_data(filename):
    with get_connection() as conn:
        if conn is None:
            print('Failed to connect to the database')
            return

        with open(filename, 'r') as file:
            sql_file = file.read()
            rows = None
            cur = conn.cursor()
            try:
                cur.execute(sql_file)
                rows = cur.fetchall()
                print(rows)
            except Exception as e:
                print(e)
            finally:
                cur.close()
            return rows

