from django.contrib.syndication.views import Feed
from your_snippets.api.models import Snippet

class RSSFeed(Feed):
    title = "Fuzzy's Snippets"
    link = "https://snippets.fuzzyslogic.com"
    description = "Snippets Fuzzy has collected from the internets"

    def items(self):
        return Snippet.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        content = item.content.replace('\n', '<br />')
        for img in item.images.all():
            content = '{}<br /><br /><img src="https://snippets.fuzzyslogic.com{}">'.format(content, img.image.url)
        return content

    def item_categories(self, item):
        categories = []
        for tag in item.tags.split(','):
            categories.append(tag.strip())
        return categories

    def item_link(self, item):
        return item.url
