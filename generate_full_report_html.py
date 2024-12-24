def generate_full_report_html(trending_pairs_html_markput, top_gaining_pairs_html_markput, newest_pairs_html_markput, chain):
    """
    Generate a full report HTML file for a given chain.

    Args:
        trending_pairs_html_markput (str): HTML markup for trending pairs table.
        top_gaining_pairs_html_markput (str): HTML markup for top gaining pairs table.
        newest_pairs_html_markput (str): HTML markup for newest pairs table.
        chain (str): Name of the chain.

    Returns:
        None
    """
    trending_pairs_html_markput = trending_pairs_html_markput.to_html()
    top_gaining_pairs_html_markput = top_gaining_pairs_html_markput.to_html()
    newest_pairs_html_markput = newest_pairs_html_markput.to_html()

    all_pairs_table_html = f"""
    <h1>Trending Pairs</h1>
    {trending_pairs_html_markput}
    <h1>Top Gaining Pairs</h1>
    {top_gaining_pairs_html_markput}
    <h1>Newest Pairs</h1>{newest_pairs_html_markput}
    """

    with open(f"./templates/pairs_template.html", "r") as pairs_template_file:
        template = pairs_template_file.read()
        template = template.replace("<!-- %PUT_TABLE_HTML_HERE% -->", all_pairs_table_html)
        chain_title = chain.capitalize()
        template = template.replace("<!-- %TITLE% -->", chain_title)
        with open(f"./reports/{chain}_all_pairs.html", "w") as chain_report_file:
            chain_report_file.write(template)