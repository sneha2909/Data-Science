import streamlit as st
from pdf_data_extraction import pdf_data as data_pdf
from io import StringIO 
st.header('Welcome to PDF Extractor')
# def pdf_conversion():
#     st.subheader('Convert your Image to PDF')
#     image=st.file_uploader('Upload an image you want to convert into pdf',['jpg','png','jpeg'])
#     pdf_path=st.text_input('Enter the path where you want to save the file','Type Here')
#     if image!=None:
#         load_img=data_pdf.img_pdf(image)
# filename=ntpath.basename("pdf_path")
# filename=filename[:-4]
#     # st.download_button(label="Download PDF",data=load_img,file_name=str(filename),mime=None,)
def pdf_img():
    st.subheader('Convert your PDF to Image')
    path=st.text_input('Enter the path of the Pdf')
    if len(path) != 0:
        data_pdf.pdf_img(path)
        st.success('PDF is successfully converted to image')
        img_path=st.text_input('Enter the path of the image the pdf was converted into')
        if img_path != None:
            if(st.button('Perform OCR')):
                amt=data_pdf.ocr(img_path)
                st.write('Total amount Successfully extracted from invoice:Rs.',amt)
    # print(os.getcwd())
    # if pdf!=None:
    #     # pdf_byte=pdf.getvalue()
    #     # st.write(pdf)
    #     with open(pdf, 'rb') as fopen:
    #         q = fopen.read()
    #         stringio = StringIO(q.decode("utf-8"))
    #         print('hello')
    #         print(stringio)
    #     # st.write(stringio)
    #     # To read file as string:
    #     string_data = stringio.read()
    #     # st.write(string_data)
    
    # filename=st.text_input('Enter the name of the image you want to save as')
    # st.download_button(label="Download Image",data=conv_img,file_name=str(filename),mime=None)
    

pdf_img()