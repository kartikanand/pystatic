import sys
import os

import jinja2
import frontmatter

from markdown2 import markdown

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('layouts/')
)

def md_to_html(md):
    md_post = frontmatter.load(md)
    md_content = md_post.content

    md_html = markdown(md_content)

    layout = md_post['layout']
    layout = layout + '.html'
    template = env.get_template(layout)

    return template.render(content=md_html)


def html_to_html(html):
    template = env.get_template(layout)
    return template.render(content=md_html)


def create_site_dir():
    site_dir = 'site'
    if not os.path.exists(site_dir):
        os.mkdir(site_dir)


def write_to_site(filename, contents):
    site_dir = 'site'

    with open(os.path.join(site_dir, filename), 'w') as f:
        f.write(contents)


def create_posts():
    post_dir = './posts'
    post_files = os.listdir(post_dir)

    for post in post_files:
        postname, _ = os.path.splitext(post)
        with open(os.path.join(post_dir, post)) as md:
            post_html = md_to_html(md)

            write_to_site(postname + '.html', post_html)


def create_pages():


if __name__ == '__main__':
    create_site_dir()
    create_posts()

