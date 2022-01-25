from behave import then

from apps.post.models import Post


@then('I should get the post with UUID "{uuid}" data')
def then_step_get_post_with_uuid_data(context, uuid):
    response_data = context.response.json()
    context.instance = Post.objects.get(uuid=uuid)
    expected_return_data = {
        "uuid": str(context.instance.uuid),
        "created": response_data["created"],
        "content": context.instance.content,
    }
    context.test.assertEqual(response_data, expected_return_data)
