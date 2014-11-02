import PyPDF2
import sys
import os


def merge(files):
    """
    Merges multiple pdf files into a single file and output it names after "merge.pdf"

    :param files: the pathname of the PDFs
    :return: None
    """
    try:
        pdf_files = [open(pathname, mode='rb') for pathname in files]
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        output_pdf = open('merge.pdf', mode='wb')
        merger.write(output_pdf)
    except FileNotFoundError as e:
        print('File not found: {}'.format(e.filename[0]))
        sys.exit(1)
    finally:
        for pdf in pdf_files:
            pdf.close()
        if not output_pdf.closed:
            output_pdf.close()


def add_bookmarks(file, catalogue_num, first_num, last_num):
    """
    Add bookmarks to the given PDF file
    It will create a copy of the PDF in the same directory

    :param file: the path of the PDF
    :param catalogue_num: the page number of the catalogue in PDF
    :param first_num: the page number of the first page of the content in PDF
    :param last_num: the page number of the last page of the content
    :return: None
    """
    try:
        with open(file, mode='r+b') as pdf:
            #若未指定最后一页则读取原始PDF的页数作为默认的内容的最后一页
            if last_num == 'lastPage':
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                last_num = pdf_reader.getNumPages()

            #复制一个副本并把内容输出到其中
            merger = PyPDF2.PdfFileMerger()
            merger.append(pdf)
            merger.addBookmark('目录', int(catalogue_num)-1)
            bookmark_num = 1
            for page_number in range(int(first_num)-1, int(last_num)):
                merger.addBookmark(str(bookmark_num), page_number)
                bookmark_num += 1
            output_pdf_path = clone(file)
            with open(output_pdf_path, mode='wb') as output_pdf:
                merger.write(output_pdf)
    except FileNotFoundError as e:
        print('File not found: {}'.format(e.filename))
        sys.exit(1)
    except ValueError as e:
        print('Please check your page number')
        sys.exit(1)


def clone(pdf):
    """
    Clone a new pdf.
    The name of the copy will be added the prefix : 'copy_'

    :param pdf: the path of the pdf to be copied
    :return: the path of the copy
    """
    file_name = 'copy_' + os.path.basename(pdf)
    file_path = os.path.split(os.path.realpath(pdf))[0] + '\\' + file_name
    # parts = ['copy', pdf]
    # product_name = '_'.join(parts)
    with open(pdf, mode='rb') as src:
        data = src.read()
        with open(file_path, mode='wb') as output:
            output.write(data)
    return file_path