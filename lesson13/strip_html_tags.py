import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    cleaned_text = re.sub(r"<[^>]*>", "", html)

    delet = cleaned_text.split("\n")
    delet = [line for line in delet if line.strip()]
    cleaned_text = "\n".join(delet)

    with open(result_file, "w", encoding="utf-8") as file:
        file.write(cleaned_text)


delete_html_tags("draft.html")
