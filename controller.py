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
    cmd = "SELECT nidn FROM admin WHERE username=%s AND BINARY password=%s"
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


def add_bimbingan(npm, nama, judul_skripsi, nidn, file_skripsi_path, tanggal):
    cmd = """
    INSERT INTO bimbingan_mahasiswa (
        npm, nama_mahasiswa, judul_skripsi, nidn, file_skripsi, tanggal
    ) 
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    try:
        # Execute the command with parameters
        connection =getdbconn()
        cursor = connection.cursor(buffered=True)

        cursor.execute(cmd, (
            npm, nama, judul_skripsi, nidn, file_skripsi_path, tanggal
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

def view_bimbingan(npm):
    cmd = """
    SELECT 
        dbm.id_detail,
        dbm.npm,
        mp.tanggal,
        mp.konsultasi_pembimbing,
        mp.status_validasi,
        bm.file_skripsi
    FROM 
        detail_bimbingan_mahasiswa dbm
    JOIN 
        management_pembimbing mp ON dbm.id_mng_pembimbing = mp.id
    JOIN 
        bimbingan_mahasiswa bm ON mp.id_bimbingan_mahasiswa = bm.id
    WHERE 
        dbm.npm = %s;
    """
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

def view_mng(nidn):
    cmd = "SELECT id, nidn, npm, nama_mahasiswa, id_bimbingan_mahasiswa, tanggal, konsultasi_pembimbing, status_validasi FROM management_pembimbing WHERE nidn = %s"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd, (nidn,))
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()        

def view_pengajuan_bmbg(nidn):
    cmd = "SELECT id, npm, nama_mahasiswa, judul_skripsi, nidn, file_skripsi, tanggal FROM bimbingan_mahasiswa WHERE nidn = %s"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd, (nidn,))
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def add_bimbingan_dosen(nidn, npm, id_bimbingan_mahasiswa, tanggal, konsultasi_pembimbing, status_validasi):
    cmd = "CALL insert_management_pembimbing(%s, %s, %s, %s, %s, %s);"

    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd, (
            nidn, npm, id_bimbingan_mahasiswa, tanggal, konsultasi_pembimbing, status_validasi
        ))
        connection.commit()
        result = cursor.rowcount > 0
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        result = False
    finally:
        cursor.close()
        connection.close()

    return result

def fltr_apr():
    cmd = "SELECT * FROM detail_bimbingan_mahasiswa WHERE id_mng_pembimbing IN (SELECT id FROM management_pembimbing WHERE status_validasi = 'approved');"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd)
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def fltr_rjct():
    cmd = "SELECT * FROM detail_bimbingan_mahasiswa WHERE id_mng_pembimbing IN (SELECT id FROM management_pembimbing WHERE status_validasi = 'rejected');"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd)
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()

def fltr_pdng():
    cmd = "SELECT * FROM detail_bimbingan_mahasiswa WHERE id_mng_pembimbing IN (SELECT id FROM management_pembimbing WHERE status_validasi = 'pending');"
    try:
        connection = getdbconn()
        cursor = connection.cursor(buffered=True)
        cursor.execute(cmd)
        result = cursor.fetchall()
        return result if cursor.rowcount > 0 else []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        connection.close()        