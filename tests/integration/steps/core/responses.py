from behave import then


@then("I should get a status {status_code}")
def then_step_get_status_code(context, status_code):
    context.test.assertEqual(context.response.status_code, int(status_code))
    return context
