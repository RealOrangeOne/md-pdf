from jinja2 import Template

def render_cover(context):
    with open("cover-template.html") as f:
        template = Template(f.read())
    with open("cover.html", "w") as f:
        cover = template.render(context)
        f.write(cover)
        return cover
