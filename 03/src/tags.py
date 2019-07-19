from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as rss:
        tags = TAG_HTML.findall(rss.read())
    return [tag.replace('-', ' ').lower() for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    print(tags)
    similar_tags = set()
    for index, tag in enumerate(tags):
        for other_tag in tags[index:]:
            this_ratio = SequenceMatcher(a=tag, b=other_tag).ratio()
            if SIMILAR < this_ratio < 1 \
                    and tag not in dict(similar_tags) \
                    and other_tag not in dict(similar_tags):
                if len(tag) > len(other_tag):
                    similar_tags.add((other_tag, tag))
                else:
                    similar_tags.add((tag, other_tag))
    return similar_tags


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print(top_tags)
    print(f'* Top {TOP_NUMBER} tags:')
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
