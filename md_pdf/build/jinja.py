from jinja2 import Environment


def render_content(content, context):
    env = Environment(
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=[
            'jinja2.ext.with_',
            'jinja2.ext.loopcontrols'
        ]
    )
    template = env.from_string(content)
    return template.render(**context)
