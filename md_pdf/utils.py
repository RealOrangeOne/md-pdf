import shutil
import os
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__file__)


def remove_dir(dir):
    logger.debug("Removing directory {}.".format(dir))
    try:
        shutil.rmtree(dir)
        os.rmdir(dir)
    except FileNotFoundError:
        pass


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default


def get_plain_text(content):
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.find('body')
    if body is None:
        return content
    try:
        body.find('h1', class_='references-title').extract()
        body.find('div', class_='references').extract()
    except AttributeError:
        pass
    return body.text
