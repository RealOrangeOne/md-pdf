from md_pdf.consts import CSL_DOWNLOAD_LINK, ASSET_DIR, CSL_DIR
from md_pdf.exceptions import PrematureExit
import os
import urllib
import zipfile
import tempfile
import shutil
from md_pdf.utils import remove_dir
from progressbar import ProgressBar
import logging

logger = logging.getLogger(__file__)


CSL_TEMP_DIR = os.path.join(ASSET_DIR, 'styles-master')


def check_csl():
    if not os.path.isdir(CSL_DIR) or os.listdir(CSL_DIR) == []:
        raise PrematureExit("No CSL files found! Run again with --update-csl")


def download_csl():
    bar = ProgressBar()

    remove_dir(CSL_DIR)

    def download_handle(count, block_size, total_size):
        if total_size < 1:  # only update the bar if we have a size
            return
        bar.update(int(count * block_size * 100 / total_size))

    _, download_location = tempfile.mkstemp()
    logger.info("Downloading CSL...")
    bar.start()
    urllib.request.urlretrieve(CSL_DOWNLOAD_LINK, download_location, reporthook=download_handle)  # nosec
    bar.finish()

    with open(download_location, 'rb') as downloaded_file:
        with zipfile.ZipFile(downloaded_file) as csl_zip:
            member_list = csl_zip.namelist()
            logger.info("Extracting CSL...")
            bar.start(max_value=len(member_list))

            for i, member in enumerate(member_list):
                csl_zip.extract(member, path=ASSET_DIR)
                bar.update(i)

            bar.finish()

    logger.info("Cleaning Up...")
    os.close(_)
    shutil.copytree(CSL_TEMP_DIR, CSL_DIR)
    os.remove(download_location)
    remove_dir(CSL_TEMP_DIR)
    urllib.request.urlcleanup()
