import mysql.connector
import os
#import matplotlib.pyplot as pt

# Configurations
from config import config
from dotenv import load_dotenv

load_dotenv()  # Imports environemnt variables from the '.env' file

# ===================SQL Connectivity=================

# SQL Connection
def getdbconn():
    connection = mysql.connector.connect(
        host=config.get("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=config.get("DB_NAME"),
        port="3306",
        autocommit=config.get("DB_AUTOCOMMIT"),
    )
    return connection

def add_logbook(nama, npm, tanggal, nama_dosen, tugas, tujuan, permasalahan_skripsi, solusi, tugas_minggu_depan, progress_skripsi_path, status_validasi):
    cmd = """
    INSERT INTO logbook (
        nama, npm, tanggal, nama_dosen, tugas, tujuan, permasalahan_skripsi, 
        solusi, tugas_minggu_depan, progress_skripsi, status_validasi
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        # Execute the command with parameters
        connection =getdbconn()
        cursor = connection.cursor(buffered=True)

        cursor.execute(cmd, (
            nama, npm, tanggal, nama_dosen, tugas, tujuan, 
            permasalahan_skripsi, solusi, tugas_minggu_depan, 
            progress_skripsi_path, status_validasi
        ))

        connection.commit()  # Commit the transaction

        result = cursor.rowcount > 0  # Check if the insert was successful
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        result = False
    finally:
        cursor.close()
        connection.close()

    return result

def view_logbook(npm):
    cmd = "SELECT id, nama, npm, tanggal, nama_dosen, tugas, tujuan, permasalahan_skripsi, solusi, tugas_minggu_depan, progress_skripsi, status_validasi, tanggal_submit FROM logbook WHERE npm = %s;"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd, (npm,))
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()



def checkUserMahasiswa(username, password=None):
    cmd = "SELECT npm FROM user WHERE username=%s AND BINARY password=%s"
    try:
        connection =getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd, (username, password))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
                print(f"Error: {err}")
                return False
    finally:
        cursor.close()
        connection.close()

def checkUserDosen(username, password=None):
    cmd = f"Select count(username) from admin where username='{username}' and BINARY password='{password}'"
    try:
        connection =getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    except mysql.connector.Error as err:
                print(f"Error: {err}")
                return False
    finally:
        cursor.close()
        connection.close()    

