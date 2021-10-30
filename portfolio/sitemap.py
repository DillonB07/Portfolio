from flask import Blueprint, render_template, make_response, current_app
sitemap = Blueprint('sitemap', __name__)
app = current_app


@sitemap.route('/')
def index():
    try:
        """Generate sitemap.xml. Makes a list of urls."""
        pages = []
        for rule in app.url_map.iter_rules():
            if "GET" in rule.methods and len(rule.arguments) == 0:
                pages.append(
                    "https://dillonb07.is-a.dev" +
                    str(rule.rule)
                )

        sitemap_xml = render_template('public/sitemap.xml', pages=pages)
        response = make_response(sitemap_xml)
        response.headers["Content-Type"] = "application/xml"

        return response
    except Exception as e:
        return(str(e))
