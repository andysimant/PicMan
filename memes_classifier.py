import os
import cv2
import pytesseract
import shutil

pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract'  # your path may be different


# Test Folder
# folder = 'C:\\Users\\Simant\\PycharmProjects\\PicMan-mark1\\img'
def MemeClassifier(folder):
    images = []
    count = 0
    meme_count = 0
    try:
        for filename in os.listdir(folder):
            if os.path.isdir(filename):
                continue
            img = cv2.imread(os.path.join(folder, filename))
            #print('Reading File:', filename)
            count += 1
            if img is not None:
                text = pytesseract.image_to_string(img, lang='eng')
                if not text.isspace():
                    old = folder + '\\' + filename
                    path = os.path.join(folder, "Memes")
                    if os.path.isdir(path) == False:
                        os.mkdir(path)
                    new = folder + '\\Memes\\new_' + filename
                    shutil.copyfile(old, new)
                    meme_count += 1
                else:
                    old = folder + '\\' + filename
                    path = os.path.join(folder, "Photos")
                    if os.path.isdir(path) == False:
                        os.mkdir(path)
                    new = folder + '\\Photos\\new_' + filename
                    shutil.copyfile(old, new)

        return count - 1, meme_count
    except:
        print("Unexpected error")
        return -1
