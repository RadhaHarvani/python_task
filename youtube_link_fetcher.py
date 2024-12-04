from googleapiclient.discovery import build

def get_youtube_links(query, api_key, max_results=5):
    """
    Fetches YouTube video links for a given search query.

    Args:
        query (str): The search string.
        api_key (str): Your YouTube Data API key.
        max_results (int): Number of results to return.

    Returns:
        list: A list of YouTube video links.
    """
    youtube = build("youtube", "v3", developerKey=api_key)
    
    # Perform the search
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",  # Fetch only video results
        maxResults=max_results
    )
    response = request.execute()
    
    # Extract video links
    video_links = [
        f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        for item in response.get("items", [])
    ]
    
    return video_links

# Example usage:
api_key = "AIzaSyDXq5cxyLL2TWE6hnvU7bGb6ilCIbkTn-A " # Replace with your API key
search_query = "Python programming tutorials"
links = get_youtube_links(search_query, api_key)
print("YouTube Links:", links)
