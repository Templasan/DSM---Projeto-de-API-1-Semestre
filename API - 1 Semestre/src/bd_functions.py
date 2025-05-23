import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        database="df_banco",
        port=3306,
        user="root",
        password="fatec",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def executar_consulta(query, params=None, dict_cursor=True):
    conn = get_db_connection()
    cursor_class = pymysql.cursors.DictCursor if dict_cursor else None
    cursor = conn.cursor(cursor_class) if cursor_class else conn.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        resultado = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return resultado
