import os
import requests

GITHUB_API = "https://api.github.com/graphql"

QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        weeks{
          contributionDays{
            contributionCount
            color
            date
          }
        }
      }
    }
  }
}
"""


def get_contributions(username: str):
    """
    Fetch GitHub contribution calendar using GraphQL.
    """

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN environment variable not found."
        )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "query": QUERY,
        "variables": {
            "login": username
        }
    }

    response = requests.post(
        GITHUB_API,
        headers=headers,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return (
        data["data"]["user"]
            ["contributionsCollection"]
            ["contributionCalendar"]
            ["weeks"]
    )