def food_database(filename: str):
    with open(filename) as recipe_file:
        database = []
        per_recipe = []
        for line in recipe_file:
            word = line.replace("\n", "")
            if word == "":
                database.append(per_recipe)
                per_recipe = []
                continue

            per_recipe.append(word)

        if per_recipe:      #check if it still has a value inside 
            database.append(per_recipe)

    return database

def search_by_name(filename: str, search_word: str):
    recipe_title = []
    database = food_database(filename)
    for food in database:
        if search_word.lower() in food[0].lower():
            recipe_title.append(food[0])

    return recipe_title

def search_by_time(filename: str, prep_time: int):
    recipe_time = []
    time_txt = ""
    database = food_database(filename)
    for food in database:
        if prep_time >= int(food[1]):
            time_txt = f"{food[0]}, preparation time {food[1]} min"
            recipe_time.append(time_txt)
    
    return recipe_time

def search_by_ingredient(filename: str, ingredient: str):
    recipe_ingredient = []
    database = food_database(filename)
    for food in database:
        if ingredient.lower() in food[2:]:
            ingredient_txt = f"{food[0]}, preparation time {food[1]} min"
            recipe_ingredient.append(ingredient_txt)

    return recipe_ingredient

if __name__ == "__main__":
    if False:
        recipe = input("recipe file:")
        search_word = input("search word: ")
        search_time = input("search time: ")
        search_ingredient = input("search ingredient: ")
    else:
        recipe = "recipes1.txt"
        search_word = "cake"
        prep_time = 20
        search_ingredient ="eggs"
    
    print(search_by_ingredient(recipe, search_ingredient))