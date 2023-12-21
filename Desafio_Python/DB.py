import cx_Oracle

connection = cx_Oracle.connect(
    user="RM550948",
    password="290501",
    dsn="oracle.fiap.com.br/1521/ORCL"
)

certaselect = connection.certaselect()
certaselect.execute("SELECT * FROM CERTACON")
rows = certaselect.close()

for row in rows:
    print(row)

certaselect.close()
connection.close()