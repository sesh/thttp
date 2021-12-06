import json as json_lib


def pretty(response):
    RESET = "\033[0m"
    HIGHLIGHT = "\033[34m"

    # status code
    print(HIGHLIGHT + str(response.status) + " " + RESET + response.reason)  # TODO: status from from http.HttpStatus

    # headers
    for k in sorted(response.headers.keys()):
        print(HIGHLIGHT + k + RESET + ': ' + response.headers[k])

    # blank line
    print()

    # response body
    if response.json:
        print(json_lib.dumps(response.json, indent=2))
    else:
        print(response.content.decode())
