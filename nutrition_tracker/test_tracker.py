import unittest
from unittest.mock import patch, Mock
from nutrition_tracker.nutrition_tracker import FoodItem, get_items, calculate_total


class TestFoodItem(unittest.TestCase):
    """Unit tests for the FoodItem class."""


    def test_add_food_item(self):
        """Test addition of two FoodItem instances"""
        i1 = FoodItem("rice", 205, 4.3, 0.4, 44.5)
        i2 = FoodItem("banana", 90, 1.1, 0.3, 23)
        total = i1 + i2
        self.assertEqual(total.calories, 295)
        self.assertAlmostEqual(total.protein, 5.4)
        self.assertEqual(total.fat, 0.7)
        self.assertEqual(total.carbs, 67.5)

    def test_str(self):
        """Test string representation of a FoodItem"""
        item = FoodItem("rice", 205, 4.3, 0.4, 44.5)
        expected = (
                f"\nName: rice\n"
                f"\nCalories: 205.00kcal\n"
                f"\nProtein: 4.30g\n"
                f"\nFat: 0.40g\n"
                f"\nCarbs: 44.50g\n"
        )
        self.assertEqual(str(item), expected)

    def test_from_api_response_success(self):
        """Test API response parseing when data is returnded."""
        mock_response = {
            "items": [
                {
                    "name": "apple",
                    "calories": 52,
                    "protein_g": 0.3,
                    "fat_total_g": 0.2,
                    "carbohydrates_total_g": 14,
                }
            ]
        }

        with patch("project.requests.get") as mock_get:
            mock_get.return_value = Mock(status_code=200)
            mock_get.return_value.json.return_value = mock_response
            item = FoodItem.from_api_response("100g of apple")
            self.assertEqual(item.name, "apple")
            self.assertEqual(item.calories, 52)
            self.assertAlmostEqual(item.protein, 0.3)
            self.assertEqual(item.carbs, 14)

    def test_from_api_response_no_data(self):
        """Test API response with no data returned."""
        with patch("project.requests.get") as mock_get:
            mock_get.return_value = Mock(status_code=200)
            mock_get.return_value.json.return_value = {"items": []}
            item = FoodItem.from_api_response("nothing")
            self.assertIsNone(item)


class TestGetObjects(unittest.TestCase):
    """Unit tests for the get_items function."""


    def test_get_items_valid_then_EOF(self):
        """Test valid input then EOF."""
        user_inputs = ["100g of apples", EOFError]
        with patch("builtins.input", side_effect=user_inputs):
            objects = get_items()
            self.assertEqual(objects, ["100g of apples"])

    def test_get_items_invalid_then_EOF(self):
        """"Test invalid input then EOF."""
        user_inputs = ["apple 100g", EOFError]
        with patch("builtins.input", side_effect=user_inputs):
            objects = get_items()
            self.assertEqual(objects, [])


class TestCalculateTotal(unittest.TestCase):
    """Unit tests for the calculate_total function."""


    def test_calculate_total(self):
        """Test summing multiple FoodItem objects"""
        i1 = FoodItem("rice", 205, 4.3, 0.4, 44.5)
        i2 = FoodItem("banana", 90, 1.1, 0.3, 23)
        total = calculate_total([i1, i2])
        self.assertEqual(total.calories, 295)
        self.assertAlmostEqual(total.protein, 5.4)
        self.assertEqual(total.fat, 0.7)
        self.assertEqual(total.carbs, 67.5)

    def test_calculate_total_empty(self):
        """Test summing empty list returns None"""
        total = calculate_total(None)
        self.assertEqual(total, None)


if __name__ == "__main__":
    unittest.main()
