def md_esc(markdownv2_str: str) -> str:
    chars = "_*[]()~`>#+-=|{}.!"
    for char in chars:
        markdownv2_str = markdownv2_str.replace(char, "\\"+char)
    return markdownv2_str

def html_esc(html_str: str) -> str:
    html_str.replace("<", "&lt;").replace(">","&gt;").replace("&","&amp;")
    return html_str