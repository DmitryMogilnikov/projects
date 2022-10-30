from gtts import gTTS
import pdfplumber
from pathlib import Path

from decorator import print_text

def pdf_to_mp3(file_path, language='en', start_page=0):
    if not Path(file_path).is_file():
        raise FileNotFoundError("Incorrect path to file")
    if not Path(file_path).suffix == '.pdf':
        raise Exception("File has incorrect type")
    
    file_name = Path(file_path).stem
    
    print_text(f"{file_name}.pdf is start to convert")

    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        if end_page == 0:
            end_page = len(pdf.pages)
        pages = [page.extract_text() for page in pdf.pages[int(start_page) - 1:]]
        
    text = ''.join(pages)
    text = text.replace('\n', '')
    text = text.replace('-', '')

    #with open("file.txt", mode='w') as file:
    #    file.write(text)

    audio = gTTS(text=text, lang=language, slow=False)
    audio.save(f"{file_name}.mp3")
    print_text(f"{file_name}.mp3 is ready to listening")



def main():
    file_path = input("Path to file: ")
    language = input("Chose the language ('en', 'ru'): ")
    start_page = input("Page with start convert: ")
    try:
        pdf_to_mp3(file_path=file_path, language=language, start_page=start_page)
    except Exception as err:
        print(f'Exception raised with message: "{err}"')


if __name__ == '__main__':
    main()