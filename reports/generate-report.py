#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os

REPORT_PATH = "/root/clawd/reports/harry-001-report.pdf"

def create_pdf():
    c = canvas.Canvas(REPORT_PATH, pagesize=A4)
    width, height = A4
    
    # Header
    c.setFillColor(colors.HexColor("#1a1a2e"))
    c.rect(0, height-80, width, 80, fill=True)
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height-50, "Harry-001 AI Assistant")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height-70, f"Report: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # System Status
    y = height - 130
    c.setFillColor(colors.HexColor("#16213e"))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "System Status")
    y -= 25
    c.setFont("Helvetica", 11)
    c.drawString(60, y, "Status: Thinking")
    y -= 15
    c.drawString(60, y, "Model: Phi3 (2.2GB) Ollama")
    y -= 15
    c.drawString(60, y, "Dashboard: localhost:3000")
    
    # 24/7 Automation
    y -= 30
    c.setFillColor(colors.HexColor("#0f3460"))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "24/7 Automation")
    y -= 25
    c.setFont("Helvetica", 11)
    c.drawString(60, y, "GitHub Trending: Every 5 min")
    y -= 15
    c.drawString(60, y, "VOO Analysis: Daily 09:00")
    y -= 15
    c.drawString(60, y, "Market Research: Daily 12:00")
    y -= 15
    c.drawString(60, y, "Git Auto-Commit: Daily 23:00")
    
    # Learning
    y -= 30
    c.setFillColor(colors.HexColor("#1a1a2e"))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Learning Repository")
    y -= 25
    c.setFont("Helvetica", 11)
    c.drawString(60, y, "BitNet - 1-bit LLM")
    y -= 15
    c.drawString(60, y, "Firecrawl - Web scraping")
    y -= 15
    c.drawString(60, y, "Claude Code - Agent coding")
    y -= 15
    c.drawString(60, y, "arXiv Papers + Hacker News")
    
    # Footer
    c.setFillColor(colors.HexColor("#1a1a2e"))
    c.rect(0, 0, width, 30, fill=True)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 10)
    c.drawString(50, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Harry-001")
    
    c.save()
    print(f"PDF: {REPORT_PATH}")

if __name__ == "__main__":
    create_pdf()
