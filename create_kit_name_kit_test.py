import sender_stand_request
import pytest
from data import KitBodies

def run_test(test_name, kit_body, expected_status, expected_name=None):
    response = sender_stand_request.send_post_request(kit_body)
    
    assert response.status_code == expected_status

    if expected_status == 201 and expected_name is not None:
        assert response.json()["name"] == expected_name

# Prueba positiva 1
def test_positive_assert_1():
    kit_body = KitBodies.test_01
    run_test("Test 1", kit_body, 201, "a")

# Prueba positiva 2
def test_positive_assert_2():
    kit_body = KitBodies.test_02
    run_test("Test 2", kit_body, 201, "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba positiva 3
def test_positive_assert_3():
    kit_body = KitBodies.test_03
    run_test("Test 5", kit_body, 201, "%@,")

# Prueba positiva 4
def test_positive_assert_4():
    kit_body = KitBodies.test_04
    run_test("Test 6", kit_body, 201, " A Aaa ")

# Prueba positiva 5
def test_positive_assert_5():
    kit_body = KitBodies.test_05
    run_test("Test 7", kit_body, 201, "123")

# Prueba negativa 1 (código 400)
def test_negative_assert_code_400_1():
    kit_body = KitBodies.test_06
    run_test("Test 3", kit_body, 400)

# Prueba negativa 2 (código 400)
def test_negative_assert_code_400_2():
    kit_body = KitBodies.test_07
    run_test("Test 4", kit_body, 400)

# Prueba negativa 3 (código 400)
def test_negative_assert_code_400_3():
    kit_body = KitBodies.test_08
    run_test("Test 8", kit_body, 400)

# Prueba negativa 4 (código 400)
def test_negative_assert_code_400_4():
    kit_body = KitBodies.test_09
    run_test("Test 9", kit_body, 400)
