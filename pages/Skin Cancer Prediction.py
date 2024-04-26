import streamlit as st
import fitz

def extract_info(pdf_file):
  doc = fitz.open(pdf_file)
  images = []
  text = ""

  for page in doc:
    for img_xref, _, img_bytes in page.getImageList():
      filename = f"image_{img_xref}.jpg"
      with open(filename, "wb") as f:
        f.write(img_bytes)
      images.append(filename)
    text += page.get_text("text")  # Basic text extraction

  return {"images": images, "text": text}

st.title("Medical Report Data Extractor")

uploaded_file = st.file_uploader("Upload your Medical Report (PDF)", type="pdf")

if uploaded_file is not None:
  data = extract_info(uploaded_file)

  # Display extracted text
  st.subheader("Extracted Text")
  st.text_area("Text", data["text"], height=300)

  # Display extracted images (if any)
  if data["images"]:
    st.subheader("Extracted Images")
    for image in data["images"]:
      st.image(image, width=250)
  else:
    st.info("No images found in this PDF.")

