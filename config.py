import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')  # Rastgele güvenlik anahtarı
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://@DILARA\\SQLEXPRESS/ihale_db?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
