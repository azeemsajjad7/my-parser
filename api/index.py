import requests
import json
from http.server import BaseHTTPRequestHandler
from datetime import datetime

def parse_bm():

    url = "https://in.bookmyshow.com/pwa/api/uapi/movies"

    payload = json.dumps({
        "regionCode": "BANG",
        "subRegionCode": "",
        "bmsId": "1.688718106.1643434285164",
        "isSuperStar": "N"
    })
    headers = {
        'authority': 'in.bookmyshow.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'accept': 'application/json',
        'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://in.bookmyshow.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://in.bookmyshow.com/explore/home/bengaluru',
        'accept-language': 'en-US,en;q=0.9'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data=response.json()
    return [(el["EventTitle"],el["formatArr"]) for el in data["nowShowing"]["arrEvents"]]



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    resp = parse_bm()
    self.wfile.write((
        json.dumps(resp)
    ).encode())
    return