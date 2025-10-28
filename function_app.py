import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTriggerFunction", methods=["GET", "POST"])
def HttpTriggerFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}! 🎉 Auto-deployment from GitHub is working perfectly!",  # ← CHANGED THIS LINE
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body to test auto-deployment!",  # ← CHANGED THIS LINE
            status_code=400
        )