import PyPDF2, os


os.chdir('D:/Downloads')

    #Lista de arquivos
files = [i for i in os.listdir() if i.endswith('.pdf')]

try:
        # Objeto WRITER
    writer = PyPDF2.PdfFileWriter()

    for file in files:
        
            # Abre o arquivo PDF
        pdf = open(file, 'rb')
            # Objeto READER
        reader = PyPDF2.PdfFileReader(pdf)
        
            # Por cada página no total de páginas do arquivo adicione ao objeto WRITER
        for page in range(reader.numPages):
            writer.addPage(reader.getPage(page))

                # Cria/abre o arquivo final
        fullFile = open('fullFile.pdf', 'ab')
                # Adiciona todas as páginas do arquivo PDF ao novo arquivo
        writer.write(fullFile)

    fullFile.close()
    pdf.close()

except Exception as exc:
    print(str(exc))