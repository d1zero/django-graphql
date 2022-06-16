import graphene
from quiz.models import Category
from quiz.types import CategoryType

# create
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)


# update
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name, id):
#         category = Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return CategoryMutation(category=category)


# delete
class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return CategoryMutation(category=category)
