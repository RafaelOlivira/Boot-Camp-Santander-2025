import csv

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"

# 📥 EXTRAÇÃO
def extract_data(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# 🔄 TRANSFORMAÇÃO
def transform_data(rows):
    transformed = []

    for row in rows:
        transformed.append({
            "nome": row["Nome"].strip().title(),
            "conta": row["Conta"].replace(" ", ""),
            "cartao_mascarado": mask_card(row["Cartão"])
        })

    return transformed

def mask_card(card_number):
    digits = "".join(filter(str.isdigit, card_number))
    return "**** **** **** " + digits[-4:]

# 📤 CARREGAMENTO
def load_data(rows, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["nome", "conta", "cartao_mascarado"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

# 🚀 PIPELINE
def run_etl():
    data = extract_data(INPUT_FILE)
    transformed_data = transform_data(data)
    load_data(transformed_data, OUTPUT_FILE)
    print("✅ ETL concluído com sucesso!")

if __name__ == "__main__":
    run_etl()
