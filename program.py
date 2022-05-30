import httpx
from colorama import Fore

global loop


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}",flush=True)
    url = f'https://talkpython.fm/{episode_number}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        return resp.text
