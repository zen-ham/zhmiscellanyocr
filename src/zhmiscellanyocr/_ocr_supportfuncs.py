import sys
import time
import zhmiscellany
import os
import threading
from PIL import Image
import pytesseract
from concurrent.futures import ThreadPoolExecutor, as_completed


def set_tesseract_path():
    anyway = False
    if getattr(sys, 'frozen', False):
        # we are running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # we are running in normal Python environment
        base_path = os.path.dirname(__file__)
        state_path = os.path.join(base_path, '_state.py')
        if os.path.exists(state_path):
            with open(state_path, 'r') as f:
                state = f.read()
            if state == '_state=0':
                with open(state_path, 'w') as f:
                    f.write('_state=1')
                anyway = True

    cwd = os.getcwd()
    if (not os.path.exists(os.path.join(base_path, 'resources'))) or anyway:
        if os.path.exists(os.path.join(base_path, 'resources')):
            zhmiscellany.fileio.remove_folder(os.path.join(base_path, 'resources'))
        os.chdir(base_path)
        from ._py_resources import gen
        gen()
        os.chdir(cwd)
    tesseract_path = os.path.join(base_path, 'resources', 'tesseract')
    pytesseract.pytesseract.tesseract_cmd = f'{tesseract_path}\\tesseract.exe'
    return pytesseract.pytesseract.tesseract_cmd


def ocr(image, config=None):
    if config is None:
        config = ''
    if type(image) == str:
        try:
            if '.ico' in image:
                ico_file = Image.open(image)
                png_file = ico_file.convert("RGBA")
                text = pytesseract.image_to_string(png_file, config=config)
            else:
                text = pytesseract.image_to_string(Image.open(image), config=config)
            return text
        except Exception as e:
            raise Exception(f'\nFailed to run OCR on file {image}\n\n{e}\n')
    else:
        return pytesseract.image_to_string(image, config=config)


ptpath = set_tesseract_path()


def batch_ocr(images, threads=10, config=None):
    results = [None] * len(images)  # Pre-allocate results list to maintain order

    # Function to capture results and maintain order
    def wrapper(idx, item):
        results[idx] = ocr(item, config)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        # Launch threads, assigning each item with its index to preserve order
        futures = [executor.submit(wrapper, idx, item) for idx, item in enumerate(images)]

        # Wait for all threads to complete
        for future in as_completed(futures):
            future.result()  # Trigger any exceptions if they occur

    return results
