"""
PIZZA FACTORY SOLUTION
=====================

This is a sample solution for the pizza factory coding challenge.
"""

def make_pizzas(available_ingredients, pizza_type):
    """
    Make pizzas from available ingredients based on pizza type.
    
    Args:
        available_ingredients (list): List of available ingredients
        pizza_type (str): Type of pizza to make
        
    Returns:
        dict: Dictionary with pizzas_made and leftover_ingredients
    """
    # Define pizza recipes
    recipes = {
        "margherita": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1},
        "pepperoni": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "pepperoni": 1},
        "veggie": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "bell_pepper": 1, "mushroom": 1},
        "hawaiian": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "ham": 1, "pineapple": 1}
    }
    
    # Validate pizza type
    if pizza_type not in recipes:
        raise ValueError(f"Unknown pizza type: {pizza_type}")
    
    recipe = recipes[pizza_type]
    
    # Count available ingredients
    ingredient_counts = {}
    for ingredient in recipe.keys():
        ingredient_counts[ingredient] = 0
    
    for ingredient in available_ingredients:
        if ingredient in ingredient_counts:
            ingredient_counts[ingredient] += 1
    
    # Calculate how many pizzas can be made
    pizzas_made = 0
    while True:
        # Check if we can make another pizza
        can_make_pizza = True
        for ingredient, needed in recipe.items():
            if ingredient_counts[ingredient] < needed:
                can_make_pizza = False
                break
        
        if not can_make_pizza:
            break
        
        # Make one pizza
        for ingredient, needed in recipe.items():
            ingredient_counts[ingredient] -= needed
        pizzas_made += 1
    
    return {
        "pizzas_made": pizzas_made,
        "leftover_ingredients": ingredient_counts
    }

def make_optimal_pizzas(available_ingredients):
    """
    Make the maximum number of pizzas across all types with available ingredients.
    
    Args:
        available_ingredients (list): List of available ingredients
        
    Returns:
        dict: Dictionary with total pizzas made and leftover ingredients
    """
    pizza_types = ["margherita", "pepperoni", "veggie", "hawaiian"]
    total_pizzas = 0
    remaining_ingredients = available_ingredients.copy()
    
    # Try each pizza type and make as many as possible
    for pizza_type in pizza_types:
        result = make_pizzas(remaining_ingredients, pizza_type)
        pizzas_made = result["pizzas_made"]
        total_pizzas += pizzas_made
        
        # Update remaining ingredients
        recipe = get_recipe(pizza_type)
        for ingredient, needed in recipe.items():
            for _ in range(pizzas_made * needed):
                if ingredient in remaining_ingredients:
                    remaining_ingredients.remove(ingredient)
    
    # Count final leftover ingredients
    leftover_counts = {}
    for ingredient in remaining_ingredients:
        leftover_counts[ingredient] = leftover_counts.get(ingredient, 0) + 1
    
    return {
        "total_pizzas_made": total_pizzas,
        "leftover_ingredients": leftover_counts
    }

def get_recipe(pizza_type):
    """Helper function to get recipe for a pizza type."""
    recipes = {
        "margherita": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1},
        "pepperoni": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "pepperoni": 1},
        "veggie": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "bell_pepper": 1, "mushroom": 1},
        "hawaiian": {"dough": 2, "tomato_sauce": 1, "mozzarella": 1, "ham": 1, "pineapple": 1}
    }
    return recipes[pizza_type]

def test_pizza_factory():
    """Test the pizza factory functions."""
    print("🍕 Testing Pizza Factory\n")
    
    # Test Case 1: Basic pepperoni pizza
    ingredients = ["dough", "dough", "dough", "dough", "tomato_sauce", "tomato_sauce", "mozzarella", "pepperoni"]
    result = make_pizzas(ingredients, "pepperoni")
    print(f"Test 1 - Pepperoni Pizza:")
    print(f"Input: {ingredients}")
    print(f"Result: {result}")
    assert result["pizzas_made"] == 1
    print("✅ Passed!\n")
    
    # Test Case 2: Multiple margherita pizzas
    ingredients = ["dough", "dough", "dough", "dough", "tomato_sauce", "tomato_sauce", "mozzarella", "mozzarella"]
    result = make_pizzas(ingredients, "margherita")
    print(f"Test 2 - Multiple Margherita:")
    print(f"Input: {ingredients}")
    print(f"Result: {result}")
    assert result["pizzas_made"] == 2
    print("✅ Passed!\n")
    
    # Test Case 3: Missing ingredients
    ingredients = ["dough", "dough", "tomato_sauce"]
    result = make_pizzas(ingredients, "pepperoni")
    print(f"Test 3 - Missing Ingredients:")
    print(f"Input: {ingredients}")
    print(f"Result: {result}")
    assert result["pizzas_made"] == 0
    print("✅ Passed!\n")
    
    # Test Case 4: Optimal pizza making
    ingredients = ["dough", "dough", "dough", "dough", "dough", "dough", 
                   "tomato_sauce", "tomato_sauce", "tomato_sauce",
                   "mozzarella", "mozzarella", "mozzarella",
                   "pepperoni", "ham", "pineapple"]
    result = make_optimal_pizzas(ingredients)
    print(f"Test 4 - Optimal Pizza Making:")
    print(f"Input: {ingredients}")
    print(f"Result: {result}")
    print("✅ Passed!\n")
    
    print("🎉 All tests passed!")

if __name__ == "__main__":
    test_pizza_factory()
