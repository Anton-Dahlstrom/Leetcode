from collections import defaultdict


class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        n = len(recipes)
        # Keep track of how many ingredients are missing for each recipe.
        missing = {}
        # Store ingredients as keys with recipes as values.
        hmap = defaultdict(list)
        for i in range(n):
            missing[recipes[i]] = len(ingredients[i])
            for ingredient in ingredients[i]:
                hmap[ingredient].append(recipes[i])

        # Iterate over our supplies and remove them from the count of missing supplies from recipes.
        res = []
        while supplies:
            temp = []
            for supply in supplies:
                for recipe in hmap[supply]:
                    missing[recipe] -= 1
                    # When we complete a recipe we add it to our result and next list of supplies.
                    if missing[recipe] == 0:
                        res.append(recipe)
                        temp.append(recipe)
            supplies = temp

        return res


recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]
output = ["bread", "sandwich"]

obj = Solution()
res = obj.findAllRecipes(recipes, ingredients, supplies)
print(res)
print(output)
print(res == output)
