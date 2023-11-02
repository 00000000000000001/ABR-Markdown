import config

def apply(doc):
    # apply standard style
    style = doc.styles['Normal']
    font = style.font
    font.name = config.NORMAL_FONT_NAME
    font.size = config.NORMAL_FONT_SIZE