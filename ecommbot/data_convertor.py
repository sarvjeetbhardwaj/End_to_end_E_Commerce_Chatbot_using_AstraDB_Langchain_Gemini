import pandas as pd
from langchain_core.documents import Document


def dataconveror():
    data_url = r'./data/flipkart_product_review.csv'
    data = pd.read_csv(data_url)

    data = data[['product_title', 'review']]

    product_list = data.to_dict(orient='records')

    docs = []
    for entry in product_list:
        metadata = {'product_name': entry['product_title']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)

    return docs


