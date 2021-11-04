import gpyocr


def get_ocr_text(file_path):
    text_result = gpyocr.tesseract_ocr(file_path, lang='eng', psm=7,
                                       config='tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-+%^')
    if type(text_result) is tuple:
        return text_result[0]
    if text_result is None:
        return ""
    else:
        return text_result