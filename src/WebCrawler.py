# from scrapegraph_py import Client
# from scrapegraph_py.logger import sgai_logger
# import os
# from dotenv import load_dotenv
# load_dotenv()
 
 
# # Configure logging
# sgai_logger.set_logging(level="INFO")
 
# # Initialize client with your API key
# sgai_client = Client(api_key=os.getenv("scrape_graph_api_key"))
 
# try:
#     # Make SmartScraper request
#     response = sgai_client.smartscraper(
#         website_url="https://stackoverflow.com/questions/78338083/how-to-bypass-a-timeout-when-webscraping",
#         user_prompt="Extract webpage information. extract only the main question nothing else"
#     )
 
#     # Process and print results
#     print(f"Request ID: {response['request_id']}")
#     print(f"Result: {response['result']}")
#     if response.get('reference_urls'):
#         print(f"Reference URLs: {response['reference_urls']}")
 
# finally:
#     # Always close the client
#     sgai_client.close()

from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("openai_api_key")

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-3.5-turbo",
    },
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the articles",
    # also accepts a string with the already downloaded HTML code
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)