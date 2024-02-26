class Recipe:
    def __init__(self, name, ingredients, recipe_type):
        self.name = name
        self.ingredients = ingredients
        self.recipe_type = recipe_type

# Beispiel-Rezepte
recipes = [
    Recipe("Auflauf", ["Kartoffel", "Tomate"], "vegetarian"),
    Recipe("Auflauf", ["Kartoffel", "Tomate"], "vegan"),
    Recipe("Steak mit Pommes", ["Kartoffel", "Fleisch"], "meat"),
]

def filter_recipes(ingredients, recipe_type):
    filtered_recipes = []

    for recipe in recipes:
        if all(ingredient in recipe.ingredients for ingredient in ingredients.split(',')):
            if not recipe_type or recipe.recipe_type == recipe_type:
                filtered_recipes.append(recipe.name)

    return filtered_recipes

def main():
    ingredients = input("Geben Sie die Zutaten ein (durch Komma getrennt): ")
    recipe_type = input("Geben Sie den Rezepttyp ein (vegetarian, vegan, meat oder leer für alle): ")

    filtered_recipes = filter_recipes(ingredients, recipe_type)

    if filtered_recipes:
        print("Gefundene Rezepte:")
        for recipe in filtered_recipes:
            print("- " + recipe)
    else:
        print("Keine passenden Rezepte gefunden.")

if __name__ == "__main__":
    main()
