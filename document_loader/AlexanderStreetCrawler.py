import requests
import json
import requests
import time
import math

def get_item():
    headers = {
        'authority': 'video.alexanderstreet.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2OTIwMjMwMTYsIm5iZiI6MTY5MjAyMzAxNiwianRpIjoiNmI0YzU0YjYtNzM4NS00NGM5LWE3ZDQtYzk1MjVjNTA1YjdiIiwiZXhwIjoxNjkyMTA5NDE2LCJpZGVudGl0eSI6eyJpbnN0aXR1dGlvbklkIjoiMTgxODAiLCJpbnN0aXR1dGlvbk5hbWUiOiJaSEVKSUFORyBVTklWRVJTSVRZIExJQlJBUlkiLCJhY2NvdW50SWQiOiIxNTE5OCIsInVzYWdlR3JvdXBJZCI6Ijk0Mjc4IiwiY291bnRyeUNvZGUiOiJDTiIsImF1dG9Db3VudHJ5IjowLCJpcENvdW50cnlDb2RlIjoiSU4iLCJ0aW1lc3RhbXAiOiIxNjkyMDIzMDE2LjQyOTI1NzkifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.ZZtyL1uLmEk3HEzwoRfnqmAViGdsCARNsyxB8_oveCw',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'mwtbid=F9531668-E1FA-4A46-B546-12F6F3D489B0; mwtses=asp01; _gid=GA1.2.96728687.1692020548; _fbp=fb.1.1692020548202.986427608; mwtbid=F9531668-E1FA-4A46-B546-12F6F3D489B0; mwtsid=463E4923-DD11-4C0F-B040-6EA6C41670EA; tracking_ga=GA1.1.1767115484.1692021923; stats_ga=GA1.1.1767115484.1692021923; OptanonAlertBoxClosed=2023-08-14T14:05:46.425Z; SSESS0dee0b8a02947e9f934fac055ec1e32a=X5Ouxp4Hmff-XOxEOZD6dM1ojERCaWZJWFar-UIqj-k; _tt_enable_cookie=1; _ttp=6wMBehNQrQlqjZEoyJYDSxqjsVT; _ga=GA1.2.987518889.1692020545; _ga_39XMLGGY9Q=GS1.1.1692026728.2.0.1692026728.0.0.0; _ga_3EKLFM7VGF=GS1.1.1692025676.2.1.1692026728.0.0.0; _gat_UA-11339397-40=1; stats_ga_D53LPJMFBM=GS1.1.1692021923.1.1.1692027234.0.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Aug+14+2023+23%3A33%3A56+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202307.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fdf09abd-cfdf-4a80-a4bc-cb50678f8bf3&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=IN%3BMH&AwaitingReconsent=false; tracking_ga_2SJ4PP2F5X=GS1.1.1692021922.1.1.1692027236.0.0.0',
        'origin': 'https://video.alexanderstreet.com',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    data = '{"variables":{"objectId":"5466134","language":"en"},"query":"query ($objectId: String, $language: String!) {\\n  readTranscript(identifier: $objectId, language: $language) {\\n    transcript\\n    translated\\n    permission\\n    __typename\\n  }\\n}"}'

    response = requests.post('https://video.alexanderstreet.com/graphql', headers=headers, data=data)
    print(response.text)

    paragraphs = json.loads(json.loads(response.text)['data']['readTranscript']['transcript'])

    print(len(paragraphs))
    for paragraph in paragraphs[:20]:
        print(paragraph)

def get_list(page:int, perpage:int):
    url = 'https://video.alexanderstreet.com/graphql'

    headers = {
        'authority': 'video.alexanderstreet.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2OTIwNTg4MjcsIm5iZiI6MTY5MjA1ODgyNywianRpIjoiZWNkMjRkMjYtMmVhZi00ODQ2LTkzZWItMTNlNjhmOTJkMzY5IiwiZXhwIjoxNjkyMjMxNjI3LCJpZGVudGl0eSI6eyJpbnN0aXR1dGlvbklkIjoiNTQwIiwiaW5zdGl0dXRpb25OYW1lIjoiUHVibGljIFBhZ2VzIEN1c3RvbWVyIChQaGFyb3MpIiwiYWNjb3VudElkIjpudWxsLCJ1c2FnZUdyb3VwSWQiOm51bGwsImNvdW50cnlDb2RlIjoiSU4iLCJhdXRvQ291bnRyeSI6MSwiaXBDb3VudHJ5Q29kZSI6IklOIiwidGltZXN0YW1wIjoiMTY5MjA1ODgyNy4wOTQwNiJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.gfbOR3cqPaOV36FgBHSs1Fnmy6MdCHbUcPKq2C5gTyw',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'mwtbid=192B0074-C606-4FBD-97EC-AD9CFCD549BC; mwtses=asp01; mwtsid=D8D39EBC-A043-4F9A-869F-5EE0FF655B07; tracking_ga=GA1.1.2069634801.1692058828; stats_ga=GA1.1.2069634801.1692058828; OptanonAlertBoxClosed=2023-08-15T00:20:34.876Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Aug+15+2023+08%3A20%3A34+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202307.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d9d52553-86ff-4738-938f-6f9ebdef96d8&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1; _ga=GA1.2.2069634801.1692058828; _gid=GA1.2.1390748257.1692058870; tracking_ga_2SJ4PP2F5X=GS1.1.1692058828.1.1.1692059029.0.0.0; stats_ga_D53LPJMFBM=GS1.1.1692058386.2.1.1692059029.0.0.0',
        'origin': 'https://video.alexanderstreet.com',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    data = {
        "operationName": "readTeaserSet",
        "variables": {
            "term": "",
            "page": page,
            "filters": ["channels.slug:counseling-and-therapy-in-video"],
            "sort": "asp_release_date:desc",
            "perpage": perpage,
            "userfilters": ["format:video", "document_type:Counseling session"]
        },
        "query": "query readTeaserSet($term: String, $page: Int, $perpage: Int, $sort: String, $userfilters: [String], $filters: [String]) {\n  readTeaserSet(\n    term: $term\n    page: $page\n    userfilters: $userfilters\n    perpage: $perpage\n    sort: $sort\n    filters: $filters\n  ) {\n    numFound\n    teasers {\n      objectId\n      channelSource\n      title\n      titlesTotal\n      slug\n      duration\n      videoDuration\n      sprites\n      releaseDate\n      publisher\n      series\n      seriesNotation\n      thumbnailUrl\n      isHostedMedia\n      isVr360Media\n      vr360MediaType\n      thumbnails {\n        portrait\n        square\n        landscape\n        __typename\n      }\n      citation {\n        full\n        __typename\n      }\n      accessIndicator {\n        isOpenAccess\n        isFullAccess\n        isPreviewable\n        isPurchasable\n        isCitationAccess\n        hasInteractionAccess\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}"
    }
    num_found = 0
    vedio_objects = []
    try:
        response = requests.post(url, headers=headers, json=data)
        if response and response.text:
            response_json = json.loads(response.text)
            if 'data' in response_json and 'readTeaserSet' in response_json['data']:
                num_found = response_json['data']['readTeaserSet']['numFound']
                teasers = response_json['data']['readTeaserSet']['teasers']
                for teaser in teasers:
                    vedio_object = {
                        'objectId': teaser['objectId'],
                        'title': teaser['title'],
                        'duration': teaser['duration'],
                        'videoDuration': teaser['videoDuration'],
                        'releaseDate': teaser['releaseDate'],
                        'publisher': teaser['publisher'],
                        'series': teaser['series'],
                        'slug': teaser['slug']
                    }
                    vedio_objects.append(vedio_object)
    except:
        return num_found, vedio_objects
    return num_found, vedio_objects
    #print(response.content)

def get_objects():
    start_time = time.time()
    perpage = 20
    all_video_objects = []
    num_found,  video_objects = get_list(1, perpage)
    if len(video_objects) > 0:
        all_video_objects += video_objects
    time.sleep(20)
    if num_found > perpage:
        total_page_number = math.ceil(num_found/perpage)
        for i in range(2, total_page_number+1):
            _, video_objects = get_list(i, perpage)
            if len(video_objects) > 0:
                all_video_objects += video_objects
            time.sleep(20)
            print('page number: ' + str(i))
            print('time cost: ' + str(time.time()-start_time))
    return all_video_objects

if __name__ == '__main__':
    all_video_objects = get_objects()
    if len(all_video_objects) > 0:
        data = {'data': all_video_objects}
        with open('video_list.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)

# teasers = json.loads(get_list())['data']['readTeaserSet']['teasers']
# for teaser in teasers:
#     print('\t'.join([teaser['objectId'], teaser['title']]))
