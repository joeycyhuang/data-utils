
from sqlalchemy import create_engine, text
from dotenv import dotenv_values
from pathlib import Path

current_file = Path(__file__)
project_root = current_file.parent.parent
env_file_path = project_root / '.foxconn_env'

config = dotenv_values(env_file_path)

connection_string = f"mssql+pyodbc://{config['USERNAME']}:{config['PASSWORD']}@{config['SQL_SERVER']}:1433/{config['DATABASE']}?driver=ODBC Driver 18 for SQL Server&TrustServerCertificate=yes&Encrypt=yes&Connection+Timeout=30"

engine = create_engine(connection_string)

try:
    with engine.connect() as conn:
        print('we are in!')
except Exception as e:
    print(e)
    


