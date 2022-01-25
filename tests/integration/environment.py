from fixtures.utils import use_fixture_by_tag

from tests.integration.fixtures.post.data import fixture_create_post_data

fixture_registry = {
    "fixture.create_post_data": fixture_create_post_data
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


def before_scenario(context, scenario):
    context.patchers = []


def after_scenario(context, scenario):
    for patcher in context.patchers:
        patcher.stop()
