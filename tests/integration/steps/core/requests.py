from behave import when


@when('I make a "{request_type}" request to "{endpoint}" endpoint with request data')
def when_step_make_request_endpoint_token(context, request_type, endpoint):
    full_path = f"/deloitte/api{endpoint}"
    request_data = getattr(context, "request_data", {})
    request_method_name = request_type.lower()
    request_method = getattr(context.test.client, request_method_name)
    context.response = request_method(full_path, request_data, content_type="application/json")
