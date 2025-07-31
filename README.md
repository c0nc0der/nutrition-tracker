# Module nutrition_tracker.tracker

??? example "View Source"
        import requests

        import re

        API_KEY = "C+dj44RzZvmMYGNERhe3lQ==2isRnHWv95uecohh"

        API_URL = "https://api.calorieninjas.com/v1/nutrition?query="

        class FoodItem:

            """

            Represents a food item with nutritional information.

            Attributes:

                name (str): Name of food item.

                calories (float): Caloric content in kcal.

                protein (float): Protein content in grams.

                fat (float): Fat content in grams.

                carbs (float): Carbohydrate content in grams.

            """

            def __init__(self, name, calories, protein, fat, carbs):

                self.name = name

                self.calories = calories

                self.protein = protein

                self.fat = fat

                self.carbs = carbs

            def __str__(self):

                """Returns formatted string of the food item's nutritional content."""

                if self.name == "total":

                    return (

                     f"\nCalories: {self.calories:.2f}kcal\n"

                     f"\nProtein: {self.protein:.2f}g\n"

                     f"\nFat: {self.fat:.2f}g\n"

                     f"\nCarbs: {self.carbs:.2f}g\n"

                )

                return (

                     f"\nName: {self.name}\n"

                     f"\nCalories: {self.calories:.2f}kcal\n"

                     f"\nProtein: {self.protein:.2f}g\n"

                     f"\nFat: {self.fat:.2f}g\n"

                     f"\nCarbs: {self.carbs:.2f}g\n"

                )

            def __add__(self, other):

                """

                    Combines two FoodItem objects to return a new one with total values.

                    Attributes:

                        other (FoodItem): Another food item to combine.

                    Returns:

                        FoodITem: A new object with the combined nutritional info.

                """

                return FoodItem(

                    name = "total",

                    calories = self.calories + other.calories,

                    protein = self.protein + other.protein,

                    fat = self.fat + other.fat,

                    carbs = self.carbs + other.carbs,

                )

            @classmethod

            def from_api_response(cls, query):

                """

                    Creates a FoodItem from an API response.

                    Attributes:

                        query (str): User query (eg. 100g of chicken)

                    Returns:

                        FoodItem or None: A FoodItem object if successful, None otherwise.

                """

                url = API_URL + query

                headers = {"X-Api-Key": API_KEY}

                try:

                    response = requests.get(url, headers=headers)

                    response.raise_for_status()

                    items = response.json().get("items", [])

                    if not items:

                        print(f"No Data Found. '{query}'")

                    item = items[0]

                    return cls(

                                name=item.get("name", query),

                                calories=item.get("calories", query),

                                protein=item.get("protein_g", query),

                                fat=item.get("fat_total_g", query),

                                carbs=item.get("carbohydrates_total_g", query),

                                )

                except requests.exceptions.RequestException as err:

                    print(f"API Request Error: {err}")

                    return None

        

        def get_items():

            """

                Collects user input in the form of food and weight descriptions.

                Returns:

                    list: a list of valid food query strings

            """

            food_items = []

            pattern = r"^\d*(?: ?(?:oz|g|lbs)? of)? \w+(?: \w+)*$"

            while True:

                try:

                    user_input = input("Food and weight: ")

                    if matches := re.fullmatch(pattern, user_input , re.IGNORECASE):

                        food_items.append(user_input)

                    else:

                        print("Invalid Format. Example: '20g of almonds'")

                except EOFError:

                    break

            return food_items

        def calculate_total(food_objects):

            """

                Sums a list of FoodItem objects into a single total.

                Attributes:

                    food_objects (list): List of food item objects

                Returns:

                    FoodItem: A new FoodItem with total values or None if empty.

            """

            if not food_objects:

                return None

            total = food_objects[0]

            for item in food_objects[1:]:

                total += item

            return total

        

        def main():

            """Main program loop. Collects input, queries API, prints totals"""

            items_list = get_items()

            food_objects = []

            for item in items_list:

                food = FoodItem.from_api_response(item)

                if food:

                    food_objects.append(food)

                total = calculate_total(food_objects)

            if total:

                print(f"\n==TOTAL NUTRITION=="

                      f"{total}")

        if __name__ == "__main__":

            main()

## Variables

```python3
API_KEY
```

```python3
API_URL
```

## Functions

    
### calculate_total

```python3
def calculate_total(
    food_objects
)
```

Sums a list of FoodItem objects into a single total.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| food_objects | list | List of food item objects | None |

**Returns:**

| Type | Description |
|---|---|
| FoodItem | A new FoodItem with total values or None if empty. |

??? example "View Source"
        def calculate_total(food_objects):

            """

                Sums a list of FoodItem objects into a single total.

                Attributes:

                    food_objects (list): List of food item objects

                Returns:

                    FoodItem: A new FoodItem with total values or None if empty.

            """

            if not food_objects:

                return None

            total = food_objects[0]

            for item in food_objects[1:]:

                total += item

            return total

    
### get_items

```python3
def get_items(
    
)
```

Collects user input in the form of food and weight descriptions.

**Returns:**

| Type | Description |
|---|---|
| list | a list of valid food query strings |

??? example "View Source"
        def get_items():

            """

                Collects user input in the form of food and weight descriptions.

                Returns:

                    list: a list of valid food query strings

            """

            food_items = []

            pattern = r"^\d*(?: ?(?:oz|g|lbs)? of)? \w+(?: \w+)*$"

            while True:

                try:

                    user_input = input("Food and weight: ")

                    if matches := re.fullmatch(pattern, user_input , re.IGNORECASE):

                        food_items.append(user_input)

                    else:

                        print("Invalid Format. Example: '20g of almonds'")

                except EOFError:

                    break

            return food_items

    
### main

```python3
def main(
    
)
```

Main program loop. Collects input, queries API, prints totals

??? example "View Source"
        def main():

            """Main program loop. Collects input, queries API, prints totals"""

            items_list = get_items()

            food_objects = []

            for item in items_list:

                food = FoodItem.from_api_response(item)

                if food:

                    food_objects.append(food)

                total = calculate_total(food_objects)

            if total:

                print(f"\n==TOTAL NUTRITION=="

                      f"{total}")

## Classes

### FoodItem

```python3
class FoodItem(
    name,
    calories,
    protein,
    fat,
    carbs
)
```

Represents a food item with nutritional information.

#### Attributes

| Name | Type | Description | Default |
|---|---|---|---|
| name | str | Name of food item. | None |
| calories | float | Caloric content in kcal. | None |
| protein | float | Protein content in grams. | None |
| fat | float | Fat content in grams. | None |
| carbs | float | Carbohydrate content in grams. | None |

??? example "View Source"
        class FoodItem:

            """

            Represents a food item with nutritional information.

            Attributes:

                name (str): Name of food item.

                calories (float): Caloric content in kcal.

                protein (float): Protein content in grams.

                fat (float): Fat content in grams.

                carbs (float): Carbohydrate content in grams.

            """

            def __init__(self, name, calories, protein, fat, carbs):

                self.name = name

                self.calories = calories

                self.protein = protein

                self.fat = fat

                self.carbs = carbs

            def __str__(self):

                """Returns formatted string of the food item's nutritional content."""

                if self.name == "total":

                    return (

                     f"\nCalories: {self.calories:.2f}kcal\n"

                     f"\nProtein: {self.protein:.2f}g\n"

                     f"\nFat: {self.fat:.2f}g\n"

                     f"\nCarbs: {self.carbs:.2f}g\n"

                )

                return (

                     f"\nName: {self.name}\n"

                     f"\nCalories: {self.calories:.2f}kcal\n"

                     f"\nProtein: {self.protein:.2f}g\n"

                     f"\nFat: {self.fat:.2f}g\n"

                     f"\nCarbs: {self.carbs:.2f}g\n"

                )

            def __add__(self, other):

                """

                    Combines two FoodItem objects to return a new one with total values.

                    Attributes:

                        other (FoodItem): Another food item to combine.

                    Returns:

                        FoodITem: A new object with the combined nutritional info.

                """

                return FoodItem(

                    name = "total",

                    calories = self.calories + other.calories,

                    protein = self.protein + other.protein,

                    fat = self.fat + other.fat,

                    carbs = self.carbs + other.carbs,

                )

            @classmethod

            def from_api_response(cls, query):

                """

                    Creates a FoodItem from an API response.

                    Attributes:

                        query (str): User query (eg. 100g of chicken)

                    Returns:

                        FoodItem or None: A FoodItem object if successful, None otherwise.

                """

                url = API_URL + query

                headers = {"X-Api-Key": API_KEY}

                try:

                    response = requests.get(url, headers=headers)

                    response.raise_for_status()

                    items = response.json().get("items", [])

                    if not items:

                        print(f"No Data Found. '{query}'")

                    item = items[0]

                    return cls(

                                name=item.get("name", query),

                                calories=item.get("calories", query),

                                protein=item.get("protein_g", query),

                                fat=item.get("fat_total_g", query),

                                carbs=item.get("carbohydrates_total_g", query),

                                )

                except requests.exceptions.RequestException as err:

                    print(f"API Request Error: {err}")

                    return None

------

#### Static methods

    
#### from_api_response

```python3
def from_api_response(
    query
)
```

Creates a FoodItem from an API response.

**Parameters:**

| Name | Type | Description | Default |
|---|---|---|---|
| query | str | User query (eg. 100g of chicken) | None |

**Returns:**

| Type | Description |
|---|---|
| None | FoodItem or None: A FoodItem object if successful, None otherwise. |

??? example "View Source"
            @classmethod

            def from_api_response(cls, query):

                """

                    Creates a FoodItem from an API response.

                    Attributes:

                        query (str): User query (eg. 100g of chicken)

                    Returns:

                        FoodItem or None: A FoodItem object if successful, None otherwise.

                """

                url = API_URL + query

                headers = {"X-Api-Key": API_KEY}

                try:

                    response = requests.get(url, headers=headers)

                    response.raise_for_status()

                    items = response.json().get("items", [])

                    if not items:

                        print(f"No Data Found. '{query}'")

                    item = items[0]

                    return cls(

                                name=item.get("name", query),

                                calories=item.get("calories", query),

                                protein=item.get("protein_g", query),

                                fat=item.get("fat_total_g", query),

                                carbs=item.get("carbohydrates_total_g", query),

                                )

                except requests.exceptions.RequestException as err:

                    print(f"API Request Error: {err}")

                    return None
