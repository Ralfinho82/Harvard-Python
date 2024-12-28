from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.cell(200, 40, "CS50 Shirtificate", align = "C")


def main():
    s = input("Name: ")

    # Instantiation of inherited class
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x = 30, y = 50, w = 150, h = 150)
    pdf.set_text_color(r = 255, g = 255, b = 255)
    pdf.set_font("helvetica", "", 20)
    pdf.ln(10)
    pdf.cell(0, 160, f"{s} took CS50", align = "C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

