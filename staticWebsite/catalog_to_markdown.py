import pandas as pd

from src.schemas import DataCatalog


OUTPUT_MARKDOWN_FILE  = "content/data_catalog.md"


DATASET_COLUMN_MAPPING = {
    "name" : "Name",
    "description" : "Description",
    "source" : "Source URL",
    "website" : "Website URL",
    "file_used" : "File used",
    }

MARKDOWN_TEMPLATE = f"""
Title: Data Catalog\n\n
Date: {current_datetime}
Modified: {current_datetime}
Category: Python
Tags: catalog, data, nhs-england, ons, population, scenarios
Slug: data-catalog
Authors: Andrew Jarman, Ibrahim Khan
Summary: Data Catalogue for the SNEE-ICS Demand and Capacity Modelling project.

## NHS England Datasets\n
<!-- START TABLE 1-->\n
{table1}
<!-- END TABLE 1-->\n
## ONS Population Scenarios\n
<!-- START TABLE 2-->\n
{table2}
<!-- END TABLE 2-->\n
"""

def create_link(url:str, text:str='Source')->str:
    """Creates html tags for a url 
    with the text provided as the displayed text.

    Parameters
    ----------
    url : str
        url used in link
    text : str, optional
        Text displayed, by default 'Source'

    Returns
    -------
    str
        HTML chunk for a link
    """
    return f"<a href='{url}'>{text}</a>"



if __name__ == '__main__':  
    # note that this should be run from this directory (staticWebsite)
    catalog = DataCatalog.load_from_yaml("data_catalog.yaml")

    # create a dataframe for each table and rename the columns
    single_source_df = pd.DataFrame(
        [entry.table_data for entry in  catalog.single_data_sources]
        ).rename(columns=DATASET_COLUMN_MAPPING)
    ons_df = pd.DataFrame(
        [entry.table_data for entry in  catalog.scenario_data_sources[0].scenarios]
        ).rename(columns=DATASET_COLUMN_MAPPING)
    
    # loop through both tables and create links for the source and website columns
    for table in single_source_df, ons_df:
        for column in table.columns:
            if column in ["Source URL", "Website URL"]:
                # table only the first word of the column name as the link text
                link_text = column.split(" ")[0]
                # create the link
                table[column] = table[column].map(lambda x: create_link(x, link_text))

    # create a dictionary of the tables to be inserted into the markdown template
    tables = {
        "table1": single_source_df.to_html(index=False,escape=False),
        "table2": ons_df.to_html(index=False,escape=False)}

    # write to file
    with open(OUTPUT_MARKDOWN_FILE, "w") as md_file:
        md_file.write(MARKDOWN_TEMPLATE.format(**tables))





    
        



