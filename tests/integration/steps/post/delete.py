from behave import then

from apps.post.models import Post


@then('I do not have the post with UUID "{uuid}"')
def then_step_not_have_post_with_uuid(context, uuid):
    context.test.assertEqual(Post.objects.filter(uuid=uuid).count(), 0)
