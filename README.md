# Python Web Crawler
This sample is meant to show how to crawl a website via a Python Azure Function using BeautifulSoup4 and extract specific pieces of information for manipulation/storage.

## Getting Started

### Prerequisites
- Download Python 3.10 or higher.
    - https://www.python.org/downloads/
- Download Azure Function Core Tools.
    - https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local
- An Azure Subscription.
    - https://azure.microsoft.com/en-us/free
- Visual Studio Code
    - https://code.visualstudio.com/download

- For Local Testing:
    - Azurite Extension on VS Code for testing locally.
        - https://marketplace.visualstudio.com/items?itemName=Azurite.azurite
    - Postman
        - https://www.postman.com/downloads/


### Quickstart
1. git clone https://github.com/Azure-Samples/functions-python-web-crawler.git
2. Open the project folder from Visual Studio Code.

Local Testing:
1. If not created, create local.settings.json.
2. In local.settings.json, add the following:
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "UseDevelopmentStorage=true",
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AzureWebJobsFeatureFlags": "EnableWorkerIndexing"
        }
    }
3. If not installed, download the "Azurite" extension on Visual Studio Code.
    Info: Azurite is an open-source emulator providing a free local environment for testing Azure storage applications.
4. At the top of the Visual Studio Code menu, select:
    View -> Command Palette... -> Azurite: Start
5. At the top of the Visual Studio Code menu, select:
    Run -> Start Debugging OR Start Without Debugging
6. If not installed, download Postman.
7. On Postman:
    a. Set the request type to "POST"
    b. Paste the following to the URL Request: http://localhost:7071/api/search_site
    c. Select "Body" -> "raw"
    d. Paste the following to the JSON body:
        {
           "url": "{ANY_URL_YOU_WANT_TO_TRY}"
        }

    Sample URLs to try:
        1. https://azure.microsoft.com/en-US
        2. https://www.pluralsight.com/
        3. https://www.linkedin.com/

Azure Testing:
Azure:
1. If not installed, download the "Azure" extension on Visual Studio Code.
2. Click the "Azure" extension and authenticate using your Azure credentials.
3. Hover the mouse over "WORKSPACE Local", and click on the Azure Function icon (a yellow Lightning bolt between blue arrows) and select "Create Function App in Azure..."
4. Follow the prompts: Select your Azure Subscription, name your Function App, select a runtime (ex. Python 3.11).
5. When the Function App is provisioned, hover the mouse over "WORKSPACE Local", and click "Deploy to Function App..." -> Select your Subscription and Function App resource.
6. After your code is deployed, navigate to the Function App.
7. Select the function name "search_site" under "Functions" in the main Azure Function blade.
8. Select "Get Function URL" and copy the link.
9. On Postman:
    a. Set the request type to "POST"
    b. Paste the link you copied to the URL Request
    c. Select "Body" -> "raw"
    d. Paste the following to the JSON body:
        {
           "url": "{ANY_URL_YOU_WANT_TO_TRY}"
        }

    Sample URLs to try:
        1. https://azure.microsoft.com/en-US
        2. https://www.pluralsight.com/
        3. https://www.linkedin.com/


## Resources

Additional information on Python, Azure Functions, and BeautifulSoup4 can be found below:

- https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators
- https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators
- https://beautiful-soup-4.readthedocs.io/en/latest/