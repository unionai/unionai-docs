import json
SITEMAP = './sitemap.json'


def build_sphinx_docs():
    with open(SITEMAP, "r") as read_file:
        tree = json.load(read_file)
    print(tree)


build_sphinx_docs()
