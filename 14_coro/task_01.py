import asyncio
import aiohttp
import json

async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str
    async with aiohttp.request('GET', url) as resp:
        return await resp.text()

async def get_reddit_top(subreddit):
    # use request_data coroutine to get reddit top
    # url pattern - f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    # then unpack data to json:
    # %reddit_name%: {
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     },
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     }
    # }

    url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'

    raw_text = await request_data(url)
    raw_json = json.loads(raw_text)
    raw_news = raw_json['data']['children']
    list_news = list()

    for raw_newsline in raw_news:
        newsline = dict()
        line_data = raw_newsline['data']
        newsline[line_data['title']] = [line_data['score'], line_data['permalink']]
        list_news.append(newsline)

    subreddit_news = dict()
    subreddit_news[subreddit] = list_news

    return subreddit_news

async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {"python", "compsci", "microbork"}
    all_dicts = await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))
    return json.dumps(all_dicts)

common_dict = asyncio.run(main())
print(common_dict)
