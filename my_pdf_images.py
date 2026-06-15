import fitz  # PyMuPDF module
import io

print("🖼️ PDF Image Extractor! 🖼️")


pdf_file = input("PDF file name(like sample.pdf): ")

try:
    # 1. open PDF file  
    pdf_document = fitz.open(pdf_file)
    print(f"\n✅ {pdf_file} open. Total pages: {len(pdf_document)}")
    
    image_count = 0
    
    # 2. PDF pages
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        
        # 3. img every page
        images_list = page.get_images()
        
        # 4. img Save one by one
        for img_index, img in enumerate(images_list, start=1):
            xref = img[0] # Image reference ID
            
            # Image ka actual data (bytes)
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"] # Image format (png, jpeg etc.)
            
            # Image new name (e.g., image_page1_1.png)
            image_name = f"image_page{page_number+1}_{img_index}.{image_ext}"
            
            # save img ('wb' matlab write binary)
            with open(image_name, "wb") as f:
                f.write(image_bytes)
                
            print(f"📸 Save image : {image_name}")
            image_count += 1
            
    print(f"\n🎉 Boom! Total {image_count} images successfully extrected !")

except FileNotFoundError:
    print(f"❌ Error: '{pdf_file}' name not found")
except Exception as e:
    print(f"❌ Something else : {e}")
