# utils.py
def glossary_term(term, definition):
    """툴팁이 있는 용어를 반환하는 HTML."""
    tooltip_html = f"""
    <span class="tooltip">{term}
        <span class="tooltiptext">{definition}</span>
    </span>
    """
    return tooltip_html
