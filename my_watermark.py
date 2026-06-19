from pypdf import PdfReader, PdfWriter

print("🛡️ ---PDF Watermark Tool ---🛡️")
print("-" * 45)

base_pdf_name = input("Write PDF Name (e.g., sample.pdf): ")
watermark_pdf_name = input("Watermark PDF Name (e.g., watermark.pdf): ")
output_pdf_name = "watermarked_final.pdf"

try:
    # 1. (for read)
    base_pdf = PdfReader(base_pdf_name)
    watermark_pdf = PdfReader(watermark_pdf_name)
    
    # Watermark pdf page's extrection
    watermark_page = watermark_pdf.pages[0]

    # 2. New (blank) PDF binder 
    writer = PdfWriter()

    # 3.PDF pages
    for page_num in range(len(base_pdf.pages)):
        
        page = base_pdf.pages[page_num]
        
        # merge
        page.merge_page(watermark_page)
        
        # add binder 
        writer.add_page(page)

    # 4. Final PDF save 
    with open(output_pdf_name, "wb") as output_file:
        writer.write(output_file)

    print(f"\n✅ Boom!. File '{output_pdf_name}' Save in your system!")

except FileNotFoundError:
    print(f"\n❌ Error: File not find")
except Exception as e:
    print(f"\n❌ Somethin else : {e}")
