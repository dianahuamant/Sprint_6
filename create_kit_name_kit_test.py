import sender_stand_request
import pytest

def run_test(test_name, kit_body, expected_status, expected_name=None):
    response = sender_stand_request.send_post_request(kit_body)
    print(f"Test {test_name}:")
    print(response.json())

    assert response.status_code == expected_status

    if expected_status == 201 and expected_name is not None:
        assert response.json()["name"] == expected_name

# Prueba positiva 1
def test_positive_assert_1():
    kit_body = {"name": "a"}
    run_test("Test 1", kit_body, 201, "a")

# Prueba positiva 2
def test_positive_assert_2():
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    run_test("Test 2", kit_body, 201, "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba positiva 3
def test_positive_assert_3():
    kit_body = {"name": "%@,"}
    run_test("Test 5", kit_body, 201, "%@,")

# Prueba positiva 4
def test_positive_assert_4():
    kit_body = {"name": " A Aaa "}
    run_test("Test 6", kit_body, 201, " A Aaa ")

# Prueba positiva 5
def test_positive_assert_5():
    kit_body = {"name": "123"}
    run_test("Test 7", kit_body, 201, "123")

# Prueba negativa 1 (código 400)
def test_negative_assert_code_400_1():
    kit_body = {"name": ""}
    run_test("Test 3", kit_body, 400)

# Prueba negativa 2 (código 400)
def test_negative_assert_code_400_2():
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    run_test("Test 4", kit_body, 400)

# Prueba negativa 3 (código 400)
def test_negative_assert_code_400_3():
    kit_body = {"name": {}}
    run_test("Test 8", kit_body, 400)

# Prueba negativa 4 (código 400)
def test_negative_assert_code_400_4():
    kit_body = {"name": 123}
    run_test("Test 9", kit_body, 400)
