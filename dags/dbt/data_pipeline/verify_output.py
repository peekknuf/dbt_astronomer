import duckdb


conn = duckdb.connect(database="~/ecom.db")

result = conn.execute(query="SELECT * FROM econ0 LIMIT 10")
print(result.fetchdf())
