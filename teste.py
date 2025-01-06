import fitz  # PyMuPDF

# Abrir o arquivo PDF
pdf_path = "enem2021.pdf"  # Substitua pelo caminho do seu arquivo
doc = fitz.open(pdf_path)

# Percorrer as páginas do PDF
for page_number in range(len(doc)):
    page = doc[page_number]  # Obter a página atual
    blocks = page.get_text('blocks')  # Extrair blocos de texto
    
    print(f"Página {page_number + 1}:")
    for i, block in enumerate(blocks):
        text = block[4]  # O texto está no índice 4
        print(f"Bloco {i + 1}:\n{text}\n{'-' * 50}")
