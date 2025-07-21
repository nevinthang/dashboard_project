import pandas as pd

# Ganti nama file dan tabel di sini
csv_file = 'Product.csv'
table_name = '"Product"'

# Load CSV
df = pd.read_csv(csv_file)

# Handle NaN dan kutip
def sql_value(val):
    if pd.isna(val):
        return 'NULL'
    if isinstance(val, str):
        val = val.replace("'", "''")
        return f"'{val}'"
    return str(val)

# Buat SQL INSERT statement tunggal dengan ON CONFLICT
columns = ', '.join(df.columns)
sql_output = f"INSERT INTO {table_name} ({columns}) VALUES\n"

value_rows = []
for _, row in df.iterrows():
    values = ', '.join([sql_value(row[col]) for col in df.columns])
    value_rows.append(f"({values})")

sql_output += ",\n".join(value_rows) + "\n"
sql_output += f"ON CONFLICT ({df.columns[0]}) DO NOTHING;\n"  # Asumsikan kolom pertama adalah PK

# Save ke file .sql
output_file = f"x_insert.sql"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(sql_output)

print(f"SQL insert script saved to {output_file} (conflict ignored)")
