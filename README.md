# 🍽️ Nutrition Tracker

This CLI app uses the CalorieNinjas API to track food nutrition info.



## ✨ Features

- OOP `FoodItem` class
- Input validation with regex
- API integration
- Nutritional total calculation



## 📦 Installation

Before running the program, make sure to install the required Python packages:
```bash
pip install -r requirements.txt
```
Or install individually:
```bash
pip install requests
pip install pdoc
```


## 🔧 Usage

```bash
python nutrition_tracker/tracker.py
```


#### 🧾 Example Input
```
100g of chicken
20g of almonds
```


## 📖 API Docs 
**Module:** `nutrition_tracker.tracker.py`



## 🔑 Variables

```python
API_KEY     # Your CalorieNinjas API key
API_URL     # https://api.calorieninjas.com/v1/nutrition?query=
```

## 🧠 Functions

### `get_items()` 

Collects user input in the form of food and weight descriptions.

**Returns:**

| Type | Description |
|---|---|
| list | a list of valid food query strings |


### `calculate_total()`

Sums a list of FoodItem objects into a single total.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| food_objects | list | List of food item objects | None |

**Returns:**

| Type | Description |
|---|---|
| FoodItem | A new FoodItem with total values or None if empty. |

    
### `main()`

Main program loop. Collects input, queries API, prints totals


## 🧱 Class: ```FoodItem```

Represents a food item with nutritional information.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| name | str | Name of food item. | None |
| calories | float | Caloric content in kcal. | None |
| protein | float | Protein content in grams. | None |
| fat | float | Fat content in grams. | None |
| carbs | float | Carbohydrate content in grams. | None |


------
### `__str__(self)`

Returns a formatted string representation of the food item.

**Returns:** 

`str:` A human-readable summary of the food item's nutritional information.

---
### `__add__(self, other: FoodItem) -> FoodItem`

Adds two FoodItem instances together to produce a new one with summed nutritional values.

**Parameters:**

| Name | Type | Description |
|---|---|---|
| other | FoodItem | name, calories, protein, fat and carbs of food item. 

**Returns:**

`FoodItem:` A new instance with combined values.

---
### `from_api_response(self, query: str) -> FoodItem | None`

Creates a FoodItem from an API response.

**Parameters:**

| Name | Type | Description |
|---|---|---|
| query | str | (eg., `"100g of chicken"`) 

**Returns:**

A `FoodItem` if successful, or `None` if no match found or API error.


## 🔐 API Key Management
Set your API key in the `API_KEY` variable inside the code, or better:
- Store it in a `.env` file
- Load with python-dotenv

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.getenv("CALORIE_API_KEY")
```

## 🧪 Example Output
```makefile
===TOTAL NUTRITION===

Calories: 220.00 kcal
Protein: 25.00 g
Fat: 10.00 g
Carbs: 5.00 g
```
