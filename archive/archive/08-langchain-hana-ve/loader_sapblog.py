import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

class CustomSAPBlogLoader(BaseLoader):
    """Custom LangChain Loader for SAP Community Blogs"""

    HEADERS = {"User-Agent": requests.get("https://httpbingo.org/user-agent").json()["user-agent"]}

    def __init__(self, urls):
        """Initialize with a list of URLs."""
        self.urls = urls

    def load(self):
        """Load and process all URLs into LangChain Document objects."""
        return [Document(page_content=self.fetch_and_extract(url), metadata={"source": url}) for url in self.urls]

    def fetch_and_extract(self, url):
        """Fetch HTML and extract main article content."""
        response = requests.get(url, headers=self.HEADERS)

        if response.status_code != 200:
            raise ValueError(f"❌ Failed to fetch URL: {url} due to the HTTP status code {response.status_code}")

        soup = BeautifulSoup(response.content, "html.parser")
        main_body = soup.find("div", class_="lia-message-body")

        if not main_body:
            raise ValueError(f"❌ Failed to extract article content from: {url}")

        structured_text = md(
            str(main_body),
            heading_style="ATX",
            strip=["span"]
        )

        return "\n".join([line.strip() for line in structured_text.split("\n") if line.strip()])
