#!/usr/bin/python
# -*- coding: utf-8 -*-

from utilities.google_api_client_factory import get_authenticated_client
from utilities.common_utilities import get_youtube_video_url

SERVICE_NAME = "youtube"
VERSION = "v3"
API_KEY_FILE = "apiKey.json"

youtube_client = get_authenticated_client(SERVICE_NAME, VERSION, API_KEY_FILE)

def get_top_video_id(query):
    response = youtube_client.search().list(
        part="id", type="video", q=query, maxResults=1
    ).execute()
    result = response["items"][0]
    return result["id"]["videoId"]

def get_video_urls(queries):
    results = []
    for query in queries:
        video_id = get_top_video_id(query)
        video_url = get_youtube_video_url(video_id)
        res = {
            "title": query,
            "url": video_url
        }
        results.append(res)
    return results
