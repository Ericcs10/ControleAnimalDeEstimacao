from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_pdf_animal(animal: dict, vacinas: list) -> bytes:
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Relatório do Animal")

    p.setFont("Helvetica", 12)
    p.drawString(100, 770, f"Nome: {animal.get('nome')}")
    p.drawString(100, 750, f"Espécie: {animal.get('especie')}")
    p.drawString(100, 730, f"Raça ID: {animal.get('raca')}")
    p.drawString(100, 710, f"Sexo: {animal.get('sexo')}")
    p.drawString(100, 690, f"Nascimento: {animal.get('data_nascimento')}")

    p.drawString(100, 660, "Vacinas:")

    y = 640
    for vacina in vacinas:
        p.drawString(120, y, f"- {vacina['nome']} ({vacina['fabricante']})")
        p.drawString(120, y - 15, f"  Aplicação: {vacina['data_aplicacao']} | Próxima: {vacina['proxima_dose']}")
        y -= 40
        if y < 100:
            p.showPage()
            y = 800

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer.read()
