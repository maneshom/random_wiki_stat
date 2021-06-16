import requests
import wikipedia
from .models import Wiki
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def get_wiki():
    response = requests.get(url="https://en.wikipedia.org/wiki/Special:Random",)
    print(response.url)
    print(response.url.split('/')[-1])
    wiki_title = requests.utils.unquote(response.url).split('/')[-1].replace('_', ' ')
    wiki = wikipedia.page(wiki_title)
    wiki_content = wiki.content
    try:
        Wiki.objects.create(title=wiki_title, content=wiki_content,
         link=wiki.url, no_of_image=len(wiki.images), no_of_link=len(wiki.links))  
    except Exception as e:
        logger.info("Creation failed")