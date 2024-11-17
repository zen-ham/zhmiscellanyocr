`zhmiscellanyocr`,
===


A collection of OCR (image text recognition) functions.
---

[Introduction](https://github.com/zen-ham/zhmiscellanyocr/tree/master#Introduction) \
[Usage examples](https://github.com/zen-ham/zhmiscellanyocr/tree/master#Usage-examples) \
[Documentation](https://github.com/zen-ham/zhmiscellanyocr/tree/master#Documentation)

---

Introduction
===

Can be installed with `pip install zhmiscellanyocr`

The main point of this package is to allow Google's Tesseract OCR engine to be used from within a pyinstaller executable. This is not possible with packages like `pytesseract` for example.

The git repository for this package can be found [here](https://github.com/zen-ham/zhmiscellanyocr). The docs also look nicer on github.

If you want to reach out, you may add my on discord at @z_h_ or join [my server](https://discord.gg/ThBBAuueVJ).

---

Documentation:
===

---
`zhmiscellanyocr.ocr()`
---

`zhmiscellanyocr.ocr(image, config=None)`

Takes an image path or a PIL image object and runs local image text recognition and returns the text in the image. Does not use the internet to function.

#

`zhmiscellanyocr.batch_ocr()`
---

`zhmiscellanyocr.batch_ocr(images, threads=10, config=None)`

Takes a list of image paths or PIL image objects and concurrently runs local image text recognition and returns the text in the image. Does not use the internet to function.

#