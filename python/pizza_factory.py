"""
PIZZA FACTORY CODING CHALLENGE
==============================

You are working at a pizza factory that needs to optimize pizza production.
The factory receives orders and must determine how many pizzas can be made
with the available ingredients.

REQUIREMENTS:
============

1. Each pizza requires specific ingredients in specific quantities
2. You can only make complete pizzas (no partial pizzas)
3. Return the maximum number of pizzas that can be made and leftover ingredients
4. Handle different pizza types with different ingredient requirements

PIZZA RECIPES:
=============

- Margherita: 2 dough, 1 tomato_sauce, 1 mozzarella
- Pepperoni: 2 dough, 1 tomato_sauce, 1 mozzarella, 1 pepperoni
- Veggie: 2 dough, 1 tomato_sauce, 1 mozzarella, 1 bell_pepper, 1 mushroom
- Hawaiian: 2 dough, 1 tomato_sauce, 1 mozzarella, 1 ham, 1 pineapple

TASK:
=====

Implement a function `make_pizzas(available_ingredients, pizza_type)` that:

1. Takes a list of available ingredients
2. Takes a pizza type (string)
3. Returns a dictionary with:
   - "pizzas_made": number of complete pizzas made
   - "leftover_ingredients": remaining ingredients after making pizzas

EXAMPLE:
========

Input:
- available_ingredients = ["dough", "dough", "dough", "dough", "tomato_sauce", "tomato_sauce", "mozzarella", "pepperoni"]
- pizza_type = "pepperoni"

Output:
- {"pizzas_made": 1, "leftover_ingredients": {"dough": 2, "tomato_sauce": 1, "mozzarella": 0, "pepperoni": 0}}

BONUS CHALLENGES:
================

1. Implement `make_optimal_pizzas()` that tries to make the maximum total pizzas
   across all pizza types with available ingredients.

2. Add support for custom pizza recipes.

3. Implement ingredient priority system (e.g., use expensive ingredients last).

TEST CASES:
==========

You should test with various scenarios:
- Exact ingredients for one pizza
- Multiple pizzas possible
- Missing critical ingredients
- Empty ingredient list
- Invalid pizza type
- Mixed ingredient scenarios

INTERVIEW TIPS:
==============

- Think about edge cases
- Consider time and space complexity
- Write clean, readable code
- Add proper error handling
- Include comprehensive tests
- Explain your approach clearly

Good luck! 🍕
"""

# TODO: Implement your solution here
def make_pizzas(available_ingredients, pizza_type):
    """
    Make pizzas from available ingredients based on pizza type.
    
    Args:
        available_ingredients (list): List of available ingredients
        pizza_type (str): Type of pizza to make
        
    Returns:
        dict: Dictionary with pizzas_made and leftover_ingredients
    """
    pass

def make_optimal_pizzas(available_ingredients):
    """
    Make the maximum number of pizzas across all types with available ingredients.
    
    Args:
        available_ingredients (list): List of available ingredients
        
    Returns:
        dict: Dictionary with total pizzas made and leftover ingredients
    """
    pass

# Test cases - implement these
def test_pizza_factory():
    """Test the pizza factory functions."""
    pass

if __name__ == "__main__":
    test_pizza_factory()
