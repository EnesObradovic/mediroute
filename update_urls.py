import os
import re

directory = "/Users/enesyildiz/estetik app"

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    original_content = content

    # 1. treatment.html?type=hair-transplant -> /treatment/hair-transplant
    def repl_treatment(m):
        t_type = m.group(1)
        rest = m.group(2)
        if rest:
            rest = "?" + rest[1:]
        return f"href=\"/treatment/{t_type}{rest}\""

    content = re.sub(r"href=\"treatment\.html\?type=([^&\"'\s]+)(.*?)\"", repl_treatment, content)

    # 2. blog-detail.html?slug=SOMETHING -> /blog/SOMETHING
    def repl_blog(m):
        slug = m.group(1)
        rest = m.group(2)
        if rest:
            rest = "?" + rest[1:]
        return f"href=\"/blog/{slug}{rest}\""

    content = re.sub(r"href=\"blog-detail\.html\?slug=([^&\"'\s]+)(.*?)\"", repl_blog, content)

    # 3. index.html -> /
    content = re.sub(r"href=\"index\.html\"", r"href=\"/\"", content)

    # 4. XYZ.html -> /XYZ
    content = re.sub(r"href=\"([a-zA-Z0-9_-]+)\.html(\?[^\"]*)?\"", r"href=\"/\1\2\"", content)

    # 5. Fix JS location changes
    content = content.replace("window.location.href = 'index.html'", "window.location.href = '/'")
    content = content.replace("window.location.href='index.html'", "window.location.href='/'")
    content = content.replace("window.location.href = 'auth.html'", "window.location.href = '/auth'")

    if content != original_content:
        with open(filepath, "w") as f:
            f.write(content)
        return True
    return False

count = 0
for file in os.listdir(directory):
    if file.endswith(".html") or file.endswith(".js"):
        if process_file(os.path.join(directory, file)):
            count += 1

print(f"Updated {count} files.")
