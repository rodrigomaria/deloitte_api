from datetime import datetime
from uuid import UUID

from behave import given, then
from django.utils import timezone

from apps.post.models import Post


@given("I have valid post data to create an instance")
def given_step_valid_post_data(context):
    created = (timezone.now()).isoformat()
    context.request_data = {
        "created": str(created),
        "content": "string"
    }


@then("I should have a new post created with provided data in database")
def then_step_validate_created_post(context):
    post_data = context.response.json()
    post_uuid = UUID(post_data.get("uuid"))
    post_data["uuid"] = post_uuid
    created_at_datetime = datetime.fromisoformat(post_data["created"].replace("Z", "+00:00"))
    post_data["created"] = created_at_datetime.astimezone()
    context.instance = Post.objects.get(uuid=post_uuid)

    for key, value in post_data.items():
        context.test.assertEqual(getattr(context.instance, key), value)


@then("I should get the created post data in the response")
def then_step_get_created_post_data_response_payload(context):
    post_data = context.response.json()
    post_uuid = UUID(post_data.get("uuid"))
    expected_return_data = {
        "uuid": str(post_uuid),
        "created": post_data.get("created"),
        "content": post_data.get("content")
    }
    context.test.assertDictEqual(post_data, expected_return_data)
