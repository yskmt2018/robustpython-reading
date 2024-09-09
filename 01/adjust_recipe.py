# 料理のレシピを取り、材料の量を調整して、提供人数を変える
# レシピ（recipe）の第1要素は、何人分かを表す数値で、その後の要素は、
# ("flour", 1.5, "cup") のように、(name, amount, unit) の形になっている
def adjust_recipe_1(recipe, servings):
    new_recipe = [servings]
    ## recipe[0] はどういう意味か。なぜ元のレシピの人数分なのか。
    old_servings = recipe[0]
    factor = servings / old_servings
    ## 何のための pop() か。
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        # 簡単に計測できる値だけを使ってください
        ## なぜ↑のコメントが必要なのか。
        new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe


def adjust_recipe_2(recipe, servings):
    old_servings = recipe.pop(0)
    factor = servings / old_servings
    # 注：辞書内包表記
    ## 最初のコードは元のレシピの中身を空にするが、新しいコードは空にしない。
    new_recipe = {
        ingredient: (amount * factor, unit)
        for ingredient, amount, unit in recipe
    }
    ## "servings" という名前の材料があった場合、名前の衝突が生じる。
    new_recipe["servings"] = servings
    ## 辞書を返すことで、重複する材料を入れられなくなった。
    return new_recipe


# https://docs.python.org/ja/3/library/fractions.html
# fractions モジュールは有理数計算のサポートを提供します。
from fractions import Fraction


def adjust_recipe3(recipe, servings):
    """
    料理のレシピを取り、材料の量を調整して、提供できる人数を変える
    :param recipe: 調整が必要なRecipe
    :param servings: 提供人数
    :return Recipe: 新しい提供人数に合わせて人数と材料の量を調整した新しいレシピ
    """
    # 材料データのコピーを作る
    new_ingredients = list(recipe.get_ingredients())
    ## 元のレシピの材料情報を消したいという意図があること。
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ## 提供人数が Recipe クラスの一部として扱われ、リストの先頭要素であるという特殊条件が不要になったこと。
        ## 材料が別のクラス（Ingredient）となり、float ではなく Fraction を代わりに使うこと。
        ingredient.adjust_proportion(Fraction(servings, recipe.servings))
        ## Recipe クラスを使っていること。
        return Recipe(servings, new_ingredients)


class Recipe: ...
class Ingredient: ...
