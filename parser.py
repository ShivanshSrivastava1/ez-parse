import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import getopt

TAGS = {
    "Contact",
    "Top Skills",
    "Certifications",
    "Honors-Awards",
    "Publications",
    "Summary",
    "Languages",
    "Experience",
    "Education",
}


def get_contact(result_list, i):
    contact = []
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            contact.append(result_list[j].strip())
        else:
            return contact, j + 1


def get_skills(result_list, i):
    skills = []
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            skills.append(result_list[j].strip())
        else:
            return skills, j + 1


def get_certifications(result_list, i):
    certifications = []
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            certifications.append(result_list[j].strip())
        else:
            return certifications, j + 1


def get_honors(result_list, i):
    honors = []
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            honors.append(result_list[j].strip())
        else:
            return honors, j + 1


def get_summary(result_list, i):
    summary = []
    summ = ""
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            summ += result_list[j].strip() + " "
        else:
            summary.append(summ.strip())
            return summary, j + 1


def get_languages(result_list, i):
    languages = []
    for j in range(i + 1, len(result_list)):
        if len(result_list[j]) == 0:
            continue
        elif "Page" in result_list[j]:
            continue
        elif result_list[j] not in TAGS:
            languages.append(result_list[j].strip())
        else:
            return languages, j + 1


def main(argv):
    name = argv[1] + " " + argv[2]
    TAGS.add(name)
    (opts, args) = getopt.getopt(argv[3:], "dP:o:t:O:c:s:R:Y:p:m:SCnAVM:W:L:F:")
    imagewriter = None
    caching = True
    laparams = LAParams()
    retstr = io.StringIO()
    rsrcmgr = PDFResourceManager(caching=caching)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams, imagewriter=imagewriter)
    data = []

    for fname in args:
        with open(fname, "rb") as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(fp, caching=caching, check_extractable=True):
                interpreter.process_page(page)
                data = retstr.getvalue()

    weird = [
        "\u00b7",
        "\xa0",
        "\uf0da",
        "\x0c",
        "• ",
        "* ",
        "(LinkedIn)",
        " (LinkedIn)",
        "\uf0a7",
        "(Mobile)",
        "-       ",
        "●",
    ]
    for i in weird:
        data = data.replace(i, "")

    result_list = data.split("\n")

    skills = []
    languages = []
    summary = []
    certifications = []
    honors = []
    contact = []

    res = {}

    for i in range(len(result_list)):
        if result_list[i] == "Contact":
            contact, i = get_contact(result_list, i)
        if result_list[i] == "Top Skills":
            skills, i = get_skills(result_list, i)
        if result_list[i] == "Certifications":
            certifications, i = get_certifications(result_list, i)
        if result_list[i] == "Honors-Awards":
            honors, i = get_honors(result_list, i)
        if result_list[i] == "Summary":
            summary, i = get_summary(result_list, i)
        if result_list[i] == "Languages":
            languages, i = get_languages(result_list, i)

    res["contact"] = contact
    res["skills"] = skills
    res["languages"] = languages
    res["certifications"] = certifications
    res["honors"] = honors
    res["summary"] = summary

    return res


if __name__ == "__main__":
    sys.exit(main(sys.argv))
