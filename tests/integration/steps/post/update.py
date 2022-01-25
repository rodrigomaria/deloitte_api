from copy import deepcopy

from behave import given, then

from apps.post.models import Post


@given(
    'I have valid post request data to "{update_operation}" the instance with UUID "{uuid}"'
)
def given_step_valid_post_update_data(context, update_operation, uuid):
    context.instance = Post.objects.get(uuid=uuid)
    context.request_data = {
        "content": "update only this field"
    }


@then("I should get the updated post data in the response")
def then_step_get_updated_post_data_response(context):
    response_data = context.response.json()
    expected_response_data = {
        "uuid": response_data["uuid"],
        "created": response_data["created"],
        "content": response_data["content"]
    }
    context.test.assertDictEqual(response_data, expected_response_data)


@then(
    'I should have the post with UUID "{uuid}" updated with request data'
)
def then_step_should_have_post_updated_with_data(context, uuid):
    context.instance.refresh_from_db()
    request_data = deepcopy(context.request_data)
    for attribute, value in request_data.items():
        if attribute == "created":
            context.test.assertEqual(str(getattr(context.instance, "created")), value)
        else:
            context.test.assertEqual(getattr(context.instance, attribute), value)
