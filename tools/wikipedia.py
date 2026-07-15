import requests

SEARCH_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"


def execute(arguments: dict) -> str:
    query = arguments.get("query")

    if not query:
        return "Wikipedia search error: query required"

    try:
        response = requests.get(SEARCH_URL.format(title=query.replace(" ", "_")), timeout=10)

        if response.status_code == 404:
            return f"No Wikipedia page found for '{query}'"

        response.raise_for_status()
        data = response.json()

        title = data.get("title", query)
        extract = data.get("extract", "No summary available")

        return f"{title}:\n{extract}"

    except Exception as e:
        return f"Wikipedia search error: {e}"
def execute(arguments: dict) -> str:
    query = arguments.get("query") or arguments.get("topic") or arguments.get("search")

    if not query:
        return "Wikipedia search error: query required"
    ...


if __name__ == "__main__":
    print(execute({"query": "Python programming language"}))