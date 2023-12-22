import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def find_identical_files(folders):
    matrix_with_comments = {auteur: {andere_auteur: [] for andere_auteur in auteurs} for auteur in auteurs}
    
    for i, auteurs in enumerate(auteurs):
        auteurs_dir = os.path.join(folders, auteurs)
        if not os.path.exists(auteurs_dir):
            print(f"Error: Directory for auteurs '{auteurs}' not found.")
            continue

        auteur_bestanden = os.listdir(auteurs_dir)
        
        for other_author in auteurs[i+1:]:
            andere_auteurs = os.path.join(folders, other_author)
            if not os.path.exists(andere_auteurs):
                print(f"Error: Directory for auteurs '{other_author}' not found.")
                continue

            for file in auteur_bestanden:
                bestand_pad = os.path.join(auteurs_dir, file)
                other_file_path = os.path.join(andere_auteurs, file)

                if os.path.isfile(bestand_pad) and os.path.isfile(other_file_path):
                    content = open(bestand_pad, 'r').read()
                    other_content = open(other_file_path, 'r').read()

                    if content == other_content:
                        matrix_with_comments[auteurs][other_author].append(f"Files '{file}' are identical.")

    return matrix_with_comments

auteurs = ["Auteur1", "Auteur2", "Auteur3", "Auteur4"]
base_directory = input("Enter the path to the folders for analysis: ")

matrix_met_opmerkingen = find_identical_files(base_directory)

alias_mapping = {auteur: f"student_{i + 1}" for i, auteur in enumerate(auteurs)}

env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "")),
    autoescape=select_autoescape()
)

output_file_name = input("Enter the desired output filename (without extension): ")

template = env.get_template("outputtemplate.html")

html_output = template.render(matrix=matrix_met_opmerkingen, auteurs=auteurs, aliases=alias_mapping)

output_file_path = f"{output_file_name}.html"
with open(output_file_path, "w") as output_file:
    output_file.write(html_output)

print(f"HTML report generated and saved as '{output_file_path}'.")
