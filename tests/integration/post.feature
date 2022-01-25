Feature: Post API
    Scenario: Create a Post
        Given I have valid post data to create an instance
        When I make a "POST" request to "/post/" endpoint with request data
        Then I should get a status 201
        And I should get the created post data in the response
        And I should have a new post created with provided data in database

    @fixture.create_post_data
    Scenario: List Posts
        When I make a "GET" request to "/post/" endpoint with request data
        Then I should get a status 200
        And I should get both posts in a list

    @fixture.create_post_data
    Scenario Outline: Retrieve a Post
        When I make a "GET" request to "/post/<uuid>" endpoint with request data
        Then I should get a status 200
        And I should get the post with UUID "<uuid>" data

        Examples: different UUIDs
            | uuid                                 |
            | f177c4e6-d12b-4bef-94b1-d8d524b88d4d |
            | f188c4e6-d12b-4bef-94b1-d8d524b88d4d |

    @fixture.create_post_data
    Scenario Outline: Update a Post
        Given I have valid post request data to "update" the instance with UUID "<uuid>"
        When I make a "PUT" request to "/post/<uuid>" endpoint with request data
        Then I should get a status 200
        And I should get the updated post data in the response
        And I should have the post with UUID "<uuid>" updated with request data

        Examples: different UUIDs
            | uuid                                 |
            | f177c4e6-d12b-4bef-94b1-d8d524b88d4d |
            | f188c4e6-d12b-4bef-94b1-d8d524b88d4d |

    @fixture.create_post_data
    Scenario Outline: Partial Update a Post
        Given I have valid post request data to "partial update" the instance with UUID "<uuid>"
        When I make a "PATCH" request to "/post/<uuid>" endpoint with request data
        Then I should get a status 200
        And I should get the updated post data in the response
        And I should have the post with UUID "<uuid>" updated with request data

        Examples: different UUIDs
            | uuid                                 |
            | f177c4e6-d12b-4bef-94b1-d8d524b88d4d |
            | f188c4e6-d12b-4bef-94b1-d8d524b88d4d |

    @fixture.create_post_data
    Scenario Outline: Delete a Post
        When I make a "DELETE" request to "/post/<uuid>" endpoint with request data
        Then I should get a status 204
        And I do not have the post with UUID "<uuid>"

        Examples: different UUIDs
            | uuid                                 |
            | f177c4e6-d12b-4bef-94b1-d8d524b88d4d |
            | f188c4e6-d12b-4bef-94b1-d8d524b88d4d |
