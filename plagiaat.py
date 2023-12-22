import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

auteurs = ["Auteur1", "Auteur2", "Auteur3", "Auteur4"]

alias_mapping = {auteur: f"student_{i + 1}" for i, auteur in enumerate(auteurs)}

matrix_met_opmerkingen = {auteur: {andere_auteur: [] for andere_auteur in auteurs} for auteur in auteurs}

matrix_met_opmerkingen["Auteur1"]["Auteur2"] = ["Opmerking1", "Opmerking2"]
matrix_met_opmerkingen["Auteur3"]["Auteur1"] = ["Opmerking3"]
matrix_met_opmerkingen["Auteur4"]["Auteur2"] = ["Opmerking4", "Opmerking5"]

env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "")),
    autoescape=select_autoescape()
)

output_file_name = input("Voer de gewenste uitvoernaam in (zonder extensie): ")

template = env.get_template("outputtemplate.html")

html_output = template.render(matrix=matrix_met_opmerkingen, auteurs=auteurs, aliases=alias_mapping)

output_file_path = f"{output_file_name}.html"
with open(output_file_path, "w") as output_file:
    output_file.write(html_output)

print(f"HTML-rapport gegenereerd en opgeslagen als '{output_file_path}'.")
