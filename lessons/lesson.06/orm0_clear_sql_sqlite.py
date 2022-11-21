import sqlite3


# DB_FILENAME = "lesson.db"
DB_FILENAME = "db.sqlite3"


def main():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR UNIQUE NOT NULL,
        email VARCHAR UNIQUE
    );
    """

    con = sqlite3.connect(DB_FILENAME)
    cur = con.cursor()
    cur.execute(sql_create_table)

    # username = "john"
    username = "kate2"
    email = None

    cur.execute(
        """
        INSERT INTO authors(username, email) 
        VALUES (?, ?);
        """,
        (username, email),
    )
    
    # cur.execute("""
    # UPDATE authors
    # SET email = 'kate@example.com'
    # WHERE username = 'kate';""")

    con.commit()

    cur.close()
    con.close()


if __name__ == "__main__":
    main()
