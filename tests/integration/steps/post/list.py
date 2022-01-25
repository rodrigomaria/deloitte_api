from behave import then


@then("I should get both posts in a list")
def then_step_get_post_list(context):
    response_data = context.response.json()
    expected_response_data = [{
        "uuid": "f177c4e6-d12b-4bef-94b1-d8d524b88d4d",
        "created": response_data[0]["created"],
        "content": "Nam quis nulla. Integer malesuada. In in enim a arcu imperdiet malesuada. Sed vel lectus. \
            Donec odio urna, tempus molestie, porttitor ut, iaculis quis, sem. Phasellus rhoncus. Aenean id metus id \
            velit ullamcorper pulvinar. Vestibulum fermentum tortor id mi"
    }, {
        "uuid": "f188c4e6-d12b-4bef-94b1-d8d524b88d4d",
        "created": response_data[1]["created"],
        "content": "Nam quis nulla. Integer malesuada. In in enim a arcu imperdiet malesuada. Sed vel lectus. \
            Donec odio urna, tempus molestie, porttitor ut, iaculis quis, sem. Phasellus rhoncus. Aenean id metus id \
            velit ullamcorper pulvinar. Vestibulum fermentum tortor id mi"
    }
    ]
    context.test.assertEqual(response_data, expected_response_data)
