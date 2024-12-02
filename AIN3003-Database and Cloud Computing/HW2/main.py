import pymysql

def get_connection():
    """This function connects to the database and returns the connection."""
    return pymysql.connect(
        host="localhost",
        user="root",
        password="my_computer_password",  # Parolanın doğru olduğundan emin olun
        database="banking"
    )
