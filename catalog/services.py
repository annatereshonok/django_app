from .models import Category


class ProductService:
    @staticmethod
    def get_products_by_category(category_id):
        category = Category.objects.get(pk=category_id)
        products = category.products.all()
        return products
