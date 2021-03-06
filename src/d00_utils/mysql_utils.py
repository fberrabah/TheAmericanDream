import sqlalchemy
import mysql.connector


def mysql_connect():
    """ Method allowing connexion with database and took pseudo amd mdp who are in gitignore files conf"""

    from conf.conf import mysql_pseudo, mysql_mdp
    mysql_username = mysql_pseudo
    mysql_password = mysql_mdp
    database_name = 'Americabdd'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()
    return database_connection

def save_to_mysql(db_connect,df_to_save,df_name):
    """ Method to save my database """
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')