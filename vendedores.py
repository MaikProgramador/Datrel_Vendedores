import json

# Dados de várias empresas organizados em uma lista de dicionários
dados = [
    {
        "Nome": "Lucas Bernardes",
        "Telefone": "(14) 99683-1109",
        "Empresa:": "DATREL PERIFÉRICOS"
    },
        {
        "Nome": "Fábio Ramos",
        "Telefone": "(14) 99656-8637",
        "Empresa:": "DATREL PERIFÉRICOS"
    },
    

]

# Converter a lista de dicionários para uma string JSON
json_dados = json.dumps(dados, ensure_ascii=False, indent=4)

# Exibir o resultado
print(json_dados)

# Salvar em um arquivo JSON
with open("dados.json", "w", encoding="utf-8") as f:
    f.write(json_dados)

print("Dados exportados com sucesso para 'dados.json'")
