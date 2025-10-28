"""Create a Python script which will create a burger from elements.

For example bread, ham and cheese. Robot will pickup all elements only in case
when it can make a burger. What is left will be kept.
"""


def create_burger(elements, burger_recipe):
    """Create burgers from elements based on recipe."""
    # Initialize ingredient counts
    burger_stock = {ingredient: 0 for ingredient in burger_recipe}
    
    # Count available ingredients
    for element in elements:
        if element in burger_stock:
            burger_stock[element] += 1
    
    # Calculate how many burgers can be made (1 of each ingredient per burger)
    while True:
        # Check if we have at least 1 of each required ingredient
        can_make_burger = all(burger_stock[ingredient] > 0 for ingredient in burger_recipe)
        
        if not can_make_burger:
            break
            
        # Make one burger (use 1 of each ingredient)
        for ingredient in burger_recipe:
            burger_stock[ingredient] -= 1
    
    return burger_stock


def test_burger_robot():
    # Define burger recipe (ingredient: quantity needed)
    burger_recipe = ["bread", "ham", "cheese"]

    # create a list of elements for a burger
    test_cases = [
        {
            "name": "Basic case (multiple burgers)",
            "elements": ["bread", "bread", "bread", "bread", "ham", "cheese", "ham", "ham", "cheese"],
            "expected_leftovers": {"bread": 2, "ham": 1, "cheese": 0},
        },
        {
            "name": "Exact ingredients for one burger",
            "elements": ["bread", "ham", "cheese"],
            "expected_leftovers": {"bread": 0, "ham": 0, "cheese": 0},
        },
        {
            "name": "Missing cheese (no burgers possible)",
            "elements": ["bread", "ham", "ham", "bread"],
            "expected_leftovers": {"bread": 2, "ham": 2, "cheese": 0},
        },
        {
            "name": "Only bread",
            "elements": ["bread", "bread", "bread"],
            "expected_leftovers": {"bread": 3, "ham": 0, "cheese": 0},
        },
        {
            "name": "Ingredients arriving in random order",
            "elements": ["cheese", "bread", "ham", "ham", "bread", "cheese"],
            "expected_leftovers": {"bread": 0, "ham": 0, "cheese": 0},
        },
        {
            "name": "No elements at all",
            "elements": [],
            "expected_leftovers": {"bread": 0, "ham": 0, "cheese": 0},
        },
        {
            "name": "Extra cheese and ham",
            "elements": ["bread", "ham", "ham", "cheese", "cheese"],
            "expected_leftovers": {"bread": 0, "ham": 1, "cheese": 1},
        },
    ]

    for test in test_cases:
        result = create_burger(test["elements"], burger_recipe)
        print(f"🧪 {test['name']}")
        print(f"Input: {test['elements']}")
        print(f"Expected: {test['expected_leftovers']}, Got: {result}")
        assert result == test["expected_leftovers"], f"❌ Failed: {test['name']}"
        print("✅ Passed!\n")

def test_burger_robot_more_elements():
    burger_recipe = ["bread", "tomato", "ham", "cheese"]
    # create a list of elements for a burger
    test_cases = [
        {
            "name": "Basic case (multiple burgers)",
            
            "elements": ["bread", "tomato", "bread", "bread", "ham", "cheese", "ham", "ham", "cheese"],
            "expected_leftovers": {"bread": 2, "tomato": 0, "ham": 2, "cheese": 1},
        },
       
    ]

    for test in test_cases:
        result = create_burger(test["elements"], burger_recipe)
        print(f"🧪 {test['name']}")
        print(f"Input: {test['elements']}")
        print(f"Expected: {test['expected_leftovers']}, Got: {result}")
        assert result == test["expected_leftovers"], f"❌ Failed: {test['name']}"
        print("✅ Passed!\n")

if __name__ == "__main__":
    test_burger_robot()
    print("\n" + "="*50 + "\n")
    test_burger_robot_more_elements()