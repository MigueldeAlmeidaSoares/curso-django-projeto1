from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase

class RecipeCategoryViewsTest(RecipeTestBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id':1000})
        ) 
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id':1000})
        ) 
        self.assertEqual(response.status_code, 404)
   
    def test_recipe_category_template_dont_load_recipes_not_published(self): 

        recipe = self.make_recipe(is_published=False) 

        response = self.client.get(reverse('recipes:category', kwargs={'category_id' : recipe.category.id})) 

        self.assertEqual(response.status_code, 404)
    
    def test_recipe_category_template_loads_recipes(self): 
        #ESSE TEST NÃO FOI FEITO PELO PROFESSOR
        recipe = self.make_recipe()

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': recipe.category.id}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'recipes/pages/category.html'
        )







        