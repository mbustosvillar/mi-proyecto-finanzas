from fpdf import FPDF
import pandas as pd
from analysis import analyze_portfolio
from portfolio_optimization import optimize_portfolio
from llm_interface import ask_llm  # Importamos DeepSeek

def generate_pdf_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    pdf.cell(200, 10, "📊 Reporte de Análisis Financiero", ln=True, align="C")
    pdf.ln(10)

    # Análisis de portafolio
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "📌 Resumen del Portafolio:", ln=True)
    pdf.ln(5)

    sharpe_ratio, correlation_matrix = analyze_portfolio()
    optimized_weights = optimize_portfolio()
    
    resultado_ia = ask_llm(f"Genera un análisis detallado de este portafolio:\n{sharpe_ratio.to_dict()}")

    pdf.cell(200, 10, resultado_ia, ln=True)
    pdf.output("data/report.pdf")

    print("✅ Reporte generado con IA en data/report.pdf")

if __name__ == "__main__":
    generate_pdf_report()
