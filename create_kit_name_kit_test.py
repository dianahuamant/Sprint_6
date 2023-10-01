import sender_stand_request

def test_positive_assert():
    test_cases = [
        {"name": "Test 1", "kit_body": {"name": "a"}, "expected_status": 201, "expected_name": "a"},
        {"name": "Test 2", "kit_body": {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}, "expected_status": 201, "expected_name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"},
        {"name": "Test 5", "kit_body": {"name": "%@,"}, "expected_status": 201, "expected_name": "%@,"},
        {"name": "Test 6", "kit_body": {"name": " A Aaa "}, "expected_status": 201, "expected_name": " A Aaa "},
        {"name": "Test 7", "kit_body": {"name": "123"}, "expected_status": 201, "expected_name": "123"},
    ]

    for test_case in test_cases:
        sender_stand_request.run_test(test_case["name"], test_case["kit_body"], test_case["expected_status"], test_case.get("expected_name"))

def test_negative_assert_code_400():
    test_cases = [
        {"name": "Test 3", "kit_body": {"name": ""}, "expected_status": 400},
        {"name": "Test 4", "kit_body": {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}, "expected_status": 400},
        {"name": "Test 8", "kit_body": {"name": {}}, "expected_status": 400},
        {"name": "Test 9", "kit_body": {"name": 123}, "expected_status": 400},
    ]

    for test_case in test_cases:
        sender_stand_request.run_test(test_case["name"], test_case["kit_body"], test_case["expected_status"])
