import sys
import os.path
import subprocess
import warnings

from cStringIO import StringIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def pdfinfo(filename):
    """
    Wraps command line utility pdfinfo to extract the PDF meta information.
    > sudo apt install poppler-utils
    """

    cmd = "pdfinfo"
    output = {}

    cmd_out = subprocess.check_output([cmd, filename])

    for line in cmd_out.splitlines():
        k, v = (r.strip() for r in line.split(':', 1))
        output[k] = v

    return output['Title']


def parse_toc(filename):
    """
    Parses the structure of a pdf file.

    Yields the title of a document then the structure (table of contents) of
    the document.
    """
    infile = open(filename, 'rb')
    parser = PDFParser(infile)
    document = PDFDocument(parser)

    yield document.info[0]['Title']

    for (level, title, _, _, _) in document.get_outlines():
        if level == 1 and len(title) > 5:
            yield title


def parse_text(filename):
    """
    Parses the text of a pdf file.

    Yields each line of the first page of a document.
    """
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(filename, 'rb')
    for page in PDFPage.get_pages(infile, {0}):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text.split('\n')


def workflow(filename):
    try:
        text = pdfinfo(filename)
        if len(text) > 5:
            yield text
    except:
        warnings.warn("pdfinfo (from poppler-utils) unfound", RuntimeWarning)
        pass
    try:
        for text in parse_toc(filename):
            if len(text) > 5:
                yield text
    except:
        warnings.warn("Error when parsing the structure of the document",
                      RuntimeWarning)
        pass
    for text in parse_text(filename):
        if len(text) > 5:
            yield text


def validate(old_name, new_name, prefix):
    msg = "Rename '{}' to '{}.pdf'? [y/n/j/s/a] > "
    cont = raw_input(msg.format(old_name, prefix + new_name))
    while cont.lower() not in ("y", "n", "j", "s", "a"):
        cont = raw_input("Choose among y(es)/n(o)/j(oin)/s(kip)/a(bort) > ")
    if cont == "y":
        os.rename(old_name, "{}.pdf".format(prefix + new_name))
        return True
    if cont == "s":
        return True
    if cont == "n":
        return False
    if cont == "j":
        return prefix + new_name + " "
    if cont == "a":
        sys.exit(2)


def main():
    for filename in sys.argv[1:]:
        prefix = os.path.dirname(filename) + "/"
        for text in workflow(filename):
            output = validate(filename, text, prefix)
            if isinstance(output, str):
                prefix = output
                continue
            if output:
                break


if __name__ == '__main__':
    main()
