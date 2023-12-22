from os import listdir, system

IGNORE = [
    "generate.py",
    "Dockerfile",
    "README.md",
    ".git",
    ".github",
    "static",
    "index.html",
    "LICENSE",
]

links = []

for service in listdir():
    if service in IGNORE:
        continue

    print("WORKING ON ", service)
    system(f"mkdir static/{service}")
    retcode = system(
        f"jsight doc html {service}/api.jst > static/{service}/index.html")

    f = open(f"static/{service}/index.html", 'r')
    generated_content = f.read()
    f.close()
    f = open(f"static/{service}/index.html", 'w')
    f.write(generated_content.replace("<title>JSight Online Editor</title>",
            "<title>NewTube API docs</title>"))
    f.close()

    if retcode != 0:
        print("jsight exited with non-zero code")
        exit(-1)

    links.append(service)


link_html = ""
for link in links:
    link_html += f'<a href="/{link}/">{link}</a>'

with open("index.html") as template_file, open("static/index.html", 'w') as result_file:
    content = template_file.read()
    content = content.replace("{{REPLACE_WITH_LINKS}}", link_html)
    result_file.write(content)
