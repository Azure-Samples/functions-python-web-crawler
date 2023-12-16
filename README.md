---
page_type: sample
languages:
- python
products:
- azure
- azure functions
name:
- Python Web Crawler
description:
- This sample shows how to crawl a website via a Python Azure Function using BeautifulSoup4 and extract specific information for manipulation/storage.
---

# Python Web Crawler
This sample shows how to crawl a website via a Python Azure Function using BeautifulSoup4 and extract specific information for manipulation/storage.

## Getting Started

### Prerequisites
- Download Python 3.10 or higher.
    - https://www.python.org/downloads/
- Download Azure Function Core Tools.
    - https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local
- An Azure Subscription.
    - https://azure.microsoft.com/en-us/free
- Visual Studio Code.
    - https://code.visualstudio.com/download

- For Local Testing:
    - Azurite Extension on VS Code.
        - https://marketplace.visualstudio.com/items?itemName=Azurite.azurite
    - Postman.
        - https://www.postman.com/downloads/


### Quickstart
1. git clone https://github.com/Azure-Samples/functions-python-web-crawler.git
2. Open the project folder from Visual Studio Code.

Local Testing:
1. If not created, create local.settings.json.
2. In local.settings.json, add the following:
    
    ```
    {
        "IsEncrypted": false,
        "Values": {  
            "AzureWebJobsStorage": "UseDevelopmentStorage=true",
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AzureWebJobsFeatureFlags": "EnableWorkerIndexing"
        }
    }
    ```

3. If not installed, download the "Azurite" extension on Visual Studio Code.
  Info: Azurite is an open-source emulator providing a free local environment for testing Azure storage applications.
4. At the top of the Visual Studio Code menu, select:
  View -> Command Palette... -> Azurite: Start
5. At the top of the Visual Studio Code menu, select:
    Run -> Start Debugging OR Start Without Debugging
6. If not installed, download Postman.
7. On Postman:
    1. Set the request type to "POST"
    2. Paste the following to the URL Request: http://localhost:7071/api/search_site
    3. Select "Body" -> "raw"
    4. Paste the following to the JSON body:

    ```    
        {
           "url": "{ANY_URL_YOU_WANT_TO_TRY}"
        }
    ```
    
    Sample URLs to try:
    1.  https://azure.microsoft.com/en-US
    2.  https://www.pluralsight.com/
    3.  https://www.linkedin.com/

Azure Testing:
1. If not installed, download the "Azure" extension on Visual Studio Code.
2. Click the "Azure" extension and authenticate using your Azure credentials.
3. Hover the mouse over "WORKSPACE Local", and click on the Azure Function icon (a yellow Lightning bolt between blue arrows) and select "Create Function App in Azure..."
4. Follow the prompts: Select your Azure Subscription, name your Function App, select a runtime (ex. Python 3.11).
5. When the Function App is provisioned, hover the mouse over "WORKSPACE Local", and click "Deploy to Function App..." -> Select your Subscription and Function App resource.
6. After your code is deployed, navigate to the Function App.
7. Select the function name "search_site" under "Functions" in the main Azure Function blade.
8. Select "Get Function URL" and copy the link.
9. On Postman:
    1. Set the request type to "POST"
    2. Paste the link you copied to the URL Request
    3. Select "Body" -> "raw"
    4. Paste the following to the JSON body:
        
    ```
        {
           "url": "{ANY_URL_YOU_WANT_TO_TRY}"
        }
    ```

    Sample URLs to try:
    1.  https://azure.microsoft.com/en-US
    2.  https://www.pluralsight.com/
    3.  https://www.linkedin.com/


## Resources

Additional information:

- Python Azure Functions:
    - https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-decorators
- Azure Functions Python Developer Guide:
    - https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators
- BeautifulSoup4:
    - https://beautiful-soup-4.readthedocs.io/en/latest/

## Contributing
This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct. For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.