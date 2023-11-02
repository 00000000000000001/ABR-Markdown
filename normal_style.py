import config
from docx.shared import Pt

def apply(doc):
    # apply standard style
    style = doc.styles['Normal']
    # font
    font = style.font
    font.name = config.NORMAL_FONT_NAME
    font.size = config.NORMAL_FONT_SIZE
    # paragraph
    paragraph_format = style.paragraph_format
    paragraph_format.space_before = config.NORMAL_PARAGRAPH_SPACE_BEFORE
    paragraph_format.space_after = config.NORMAL_PARAGRAPH_SPACE_AFTER