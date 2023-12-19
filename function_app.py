import azure.functions as func
import logging
import requests
import traceback
import validators

from bs4 import BeautifulSoup

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="search_site", methods=["POST"])
def search_site(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Checks for a URL JSON property in the HTTP Request body.
    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        if validators.url(url):
            response = orchestrator_function(url)
            return func.HttpResponse(f"{response}",
                                 status_code=200)
        else:
            return func.HttpResponse(
                "The URL was invalid.",
                status_code=400
            )
    else:
        return func.HttpResponse(
            "No URL was passed. Please input a URL.",
            status_code=400
        )


# Function to orchestrate all of the function calls and store the needed data. 
def orchestrator_function(url):
    try:
        data = crawl_site(url)

        site_data = []
        site_data.append(get_page_title(data))
        site_data.append(get_all_urls(data))
        site_data.append(get_meta_tag(data))

        return site_data
    except Exception as error:
        logging.error(f"Error while making a request to the site: {error.__cause__}")
        logging.error(traceback.format_exc())


# Submits the HTTP request to the user-inputted URL.
def crawl_site(url):
    response = requests.get(url, allow_redirects=False)
    return BeautifulSoup(response.text, "lxml")


# Extracts the page title.
def get_page_title(data):
    try:
        return data.title.string
    except Exception as error:
        logging.error(f"Error retrieving the site title: {error.__cause__}")
        logging.error(traceback.format_exc())


# Gets all of the URLs from the webpage.
def get_all_urls(data):
    try:
        urls = []

        url_elements = data.select("a[href]")
        for url_element in url_elements:
            url = url_element['href']
            if "https://" in url or "http://" in url:
                urls.append(url)

        return urls
    
    except Exception as error:
        logging.error(f"Error retrieving the URLs in the site: {error.__cause__}")
        logging.error(traceback.format_exc())


# Extracts a specific meta tag from the URL.
def get_meta_tag(data):
    try:
        meta_tag = data.find("meta", attrs={'name': 'description'})
        return meta_tag["content"]
    except Exception as error:
        logging.error(f"Error retrieving the URLs in the site: {error.__cause__}")
        logging.error(traceback.format_exc())