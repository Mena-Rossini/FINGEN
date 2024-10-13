import ibm_db

try:
    conn = ibm_db.connect("DATABASE=Fingen;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=pain;", "", "")
    print("Connection successful!")
    ibm_db.close(conn)
except:
    print("Connection failed.")
