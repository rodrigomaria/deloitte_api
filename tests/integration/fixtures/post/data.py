from behave import fixture
from model_bakery import baker

from apps.post.models import Post


def create_post_data():
    post_data_1 = {
        "pk": 1,
        "uuid": "f177c4e6-d12b-4bef-94b1-d8d524b88d4d",
        "created": "2022-01-24 11:44:35.506717",
        "content": "Nam quis nulla. Integer malesuada. In in enim a arcu imperdiet malesuada. Sed vel lectus. \
            Donec odio urna, tempus molestie, porttitor ut, iaculis quis, sem. Phasellus rhoncus. Aenean id metus id \
            velit ullamcorper pulvinar. Vestibulum fermentum tortor id mi"
    }

    post_data_2 = {
        "pk": 2,
        "uuid": "f188c4e6-d12b-4bef-94b1-d8d524b88d4d",
        "created": "2022-01-24 11:44:35.506717",
        "content": "Nam quis nulla. Integer malesuada. In in enim a arcu imperdiet malesuada. Sed vel lectus. \
            Donec odio urna, tempus molestie, porttitor ut, iaculis quis, sem. Phasellus rhoncus. Aenean id metus id \
            velit ullamcorper pulvinar. Vestibulum fermentum tortor id mi"
    }

    baker.make(Post, **post_data_1)
    baker.make(Post, **post_data_2)


@fixture
def fixture_create_post_data(context, timeout=30, **kwargs):
    create_post_data()
