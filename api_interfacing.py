
import requests

#TARGET_URL = "https://jsonplaceholder.typicode.com/posts"
TARGET_URL = "https://jsonplaceholder.typicode.com/invalid-route"


class HTTPStatusError(Exception):
    pass


def fetch_posts(url):
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code

        print(f"HTTP Status Code: {status_code}")

        if 200 <= status_code < 300:
            print(f"Success: HTTP {status_code}")

            payload = response.json()

            if not isinstance(payload, list):
                raise ValueError("Expected a list of posts")

            for post in payload[:3]:
                title = str(
                    post.get("title", "Default Token")
                ).strip()

                body = str(
                    post.get("body", "Default Token")
                ).strip()

                print(
                    f"Title length: {len(title)}, "
                    f"Body length: {len(body)}"
                )

            return payload

        elif 400 <= status_code < 500:
            raise HTTPStatusError(
                f"Client error: HTTP {status_code}"
            )

        elif 500 <= status_code < 600:
            raise HTTPStatusError(
                f"Server error: HTTP {status_code}"
            )

        else:
            raise HTTPStatusError(
                f"Unexpected HTTP status: {status_code}"
            )

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")

    except HTTPStatusError as error:
        print(f"API error handled safely: {error}")

    except ValueError as error:
        print(f"Data parsing error: {error}")

    return None


if __name__ == "__main__":
    fetch_posts(TARGET_URL)
