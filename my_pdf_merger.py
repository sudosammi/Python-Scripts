from pypdf import PdfWriter

print("📄 Start PDF Merger Script...!")

merger = PdfWriter()

# file list
pdf_files = ['file1.pdf', 'file2.pdf'] 

for pdf in pdf_files:
    try:
        merger.append(pdf)
        print(f"✅ {pdf} Added ")
    except FileNotFoundError:
        print(f"❌ Error: {pdf} file not found!")

# Final judi hui file ko naye naam se save karna
merger.write("merged_final.pdf")
merger.close()

print("\n🎉 Boom! PDF Successfully Merged as merged_final.pdf")