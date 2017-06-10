import shutil
import os
import logging
from bs4 import BeautifulSoup
from typing import List


logger = logging.getLogger(__file__)


def remove_dir(dir: str):
    logger.debug("Removing directory {}.".format(dir))
    try:
        shutil.rmtree(dir)
        os.rmdir(dir)
    except FileNotFoundError:
        pass


def safe_list_get(l: List, idx: int, default):
    try:
        return l[idx]
    except IndexError:
        return default


def get_plain_text(content: str) -> str:
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
