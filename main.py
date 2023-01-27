#! /usr/bin/env python
import os
import fnmatch

import click

from frontmatter.frontmatter import *


@click.group()
def main():
    pass


def reorder_frontmatter(original_content):
    frontmatter, content = extract(original_content)
    ordered_frontmatter = order(frontmatter)
    new_content = build(ordered_frontmatter, content)
    return new_content


@main.command('convert-posts')
@click.argument('path')
def convert_posts(path):
    for root, _dir, files in os.walk(path):
        for items in fnmatch.filter(files, "*.md"):
            item = root + "/" + items
            print("- ", item)
            with open(item, "r") as blog_item:
                content = blog_item.read()
                new_content = reorder_frontmatter(content)
            with open(item, "w") as blog_item:
                blog_item.writelines(new_content)


if __name__ == '__main__':
    main()
