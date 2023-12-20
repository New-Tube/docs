from os import listdir, system

IGNORE = [
    "generate.py",
    "Dockerfile",
    "README.md",
    ".git",
    "static",
    "index.html"
]

links = []

for service in listdir():
    if service in IGNORE:
        continue

    print("WORKING ON ", service)
    system(f"mkdir static/{service}")
    system(f"jsight doc html {service}/api.jst > static/{service}/index.html")
    links.append(service)


link_html = ""
for link in links:
    link_html += f'<a href="/{link}/">{link}</a>'

with open("index.html") as template_file, open("static/index.html", 'w') as result_file:
    content = template_file.read()
    content = content.replace("{{REPLACE_WITH_LINKS}}", link_html)
    result_file.write(content)
