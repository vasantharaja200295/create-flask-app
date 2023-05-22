import os
import click
import requests


@click.command()
@click.argument('name', type=str)
@click.argument('path', default='.', type=click.Path(exists=True))
def main(name, path):
    os.chdir(path)
    os.makedirs(name)
    os.chdir(name)
    flask_app()


def flask_app():
    os.system("python -m venv venv")
    prev_path = os.getcwd()
    os.chdir(prev_path+"\\venv\\scripts")
    os.system("pip install flask")
    os.chdir(prev_path)
    create_app_file()
    create_style()
    os.chdir(prev_path)
    create_html()
    return


def create_style():
    path = 'https://raw.githubusercontent.com/vasantharaja200295/Templates/main/Flask-Template/static/styles/styles.css'
    contents = requests.get(path)
    new_path = "./"+path[83:97]
    file = path[97:]
    os.makedirs(new_path)
    os.chdir(new_path)
    with open(file,'wb') as f:
        f.write(contents.content)
    f.close()
    return


def create_html():
    path = 'https://raw.githubusercontent.com/vasantharaja200295/Templates/main/Flask-Template/templates/index.html'
    contents = requests.get(path).content
    new_path = "./" + path[83:93]
    file = path[93:]
    os.makedirs(new_path)
    os.chdir(new_path)
    with open(file, 'wb') as f:
        f.write(contents)
        f.close()
    return


def create_app_file():
    path = 'https://raw.githubusercontent.com/vasantharaja200295/Templates/main/Flask-Template/app.py'
    contents = requests.get(path).content
    file = "./" + path[83:]
    with open(file, 'wb') as f:
        f.write(contents)
        f.close()
    return


main()
