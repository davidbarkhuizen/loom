from urllib.parse import urlencode

import httpx


async def http_get_json(url) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


async def search_duckduckgo(query):
    """
    Query DuckDuckGo Instant Answer API.
    Returns JSON data containing abstracts, answers, and related topics.
    """
    url_base: str = "https://api.duckduckgo.com/"
    p = {
        "q": query,
        "format": "json",
        "no_redirect": 1,  # Prevent redirects
        "no_html": 1,  # Disable HTML in output
        "skip_disambiguation": 1,  # Skip disambiguation pages
    }

    url: str = f"{url_base}{urlencode(p)}"
    response_json: dict = await http_get_json(url)  # Raise error for bad status codes

    return response_json


async def search_internet(query: str) -> str:
    """
    search the internet using the supplied query

    Args:
        query: the search query

    Returns:
        A string containing the search result
    """

    print(query)

    response: dict = await search_duckduckgo(query)
    print(response)

    return str(response)
