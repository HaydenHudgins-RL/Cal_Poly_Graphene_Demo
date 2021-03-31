import graphene
from .models import Tree
from django.db.models import Q


class TreeTypeEnum(graphene.Enum):
    PINE = "Pine"
    PALM = "Palm"
    WILLOW = "Willow"


class TreeType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    treetype = graphene.String()


# Query to get data from the server
class Query(graphene.ObjectType):
    tree = graphene.Field(TreeType, name=graphene.String())
    trees = graphene.List(TreeType)

    def resolve_tree(self, info, name=None):
        qs = Tree.objects.all()

        # Search records which partially matches name and url
        filter = (
            Q(name=name)
        )
        qs = qs.filter(filter)

        tree = qs[0]

        return TreeType(**{
            "id": tree.id,
            "name": tree.name,
            "age": tree.age,
            "treetype": tree.treetype
        })

    def resolve_trees(self, info, name=None):
        qs = Tree.objects.all()

        return qs


# Create new Event
class CreateTree(graphene.Mutation):
    name = graphene.String()
    age = graphene.Int()
    treeType = graphene.String()

    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        treeType = graphene.Argument(TreeTypeEnum)

    def mutate(self, info, name, age, treeType):
        print(treeType)
        event = Tree(name=name, age=age, treetype=treeType)
        event.save()

        return CreateTree(
            name=name,
            age=age,
            treeType=treeType
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_tree = CreateTree.Field()
