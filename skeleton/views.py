from skeleton.config_app import app


@app.route("/")
def index():
    css_text = 'html { color: #ffffff; background: #101010; }'
    css_block = f'<style type="text/css">{css_text}</style>'

    greeting = "<h1><b>Skeletal Flask</h1><p>"


    image_file = 'static/dancing_skeletons.png'
    image_text = 'Two skeletons dancing together.'
    image_block = f'<p><img src="{image_file}" alt="{image_text}" /></p>'

    link = '<h3>Click here for simple database CRUD</h3><p>'
    link_block = f'<a href="/admin/">{link}</a>'

    credit_block = 'Powered by <i>Flask, SQLAlchemy,</i> and <i>Flask-Admin</i>'

    github_block = '<p>( Check out the <a href="https://github.com/therden/skeletal_flask">Github Repo</a> )</p>'

    html_page = css_block + greeting + image_block + link_block + credit_block + github_block
    return f'<html>{html_page}</html>'
