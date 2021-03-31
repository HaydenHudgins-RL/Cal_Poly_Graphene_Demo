import graphene
from graphene_django import DjangoObjectType
from .models import Island
from django.db.models import Q
import json
from tree.schema import Query as TreeQuery
from tree.schema import TreeType


class IslandType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    trees = graphene.List(TreeType)


# Query to get data from the server
class Query(graphene.ObjectType):
    island = graphene.Field(IslandType, name=graphene.String())
    islands = graphene.List(IslandType)

    def resolve_island(self, info, name=None):
        qs = Island.objects.all()

        # Search records which partially matches name and url
        filter = (
            Q(name=name)
        )
        qs = qs.filter(filter)

        island = qs[0]

        tree_names = json.loads(island.trees)

        trees = []

        for tree_name in tree_names:
            trees.append(TreeQuery().resolve_tree({}, tree_name))

        return IslandType(**{
            "id": island.id,
            "name": island.name,
            "trees": trees,
        })

    def resolve_islands(self, info):
        qs = Island.objects.all()

        islands = []

        for island in qs:
            tree_names = json.loads(island.trees)

            trees = []

            for tree_name in tree_names:
                trees.append(TreeQuery().resolve_tree({}, tree_name))

            islands.append(IslandType(**{
                "id": island.id,
                "name": island.name,
                "trees": trees,
            }))

        return islands


# Create new Event
class CreateIsland(graphene.Mutation):
    name = graphene.String()
    trees = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String()
        trees = graphene.List(graphene.String)

    def mutate(self, info, name, trees):
        trees = json.dumps(trees)
        event = Island(name=name, trees=trees)
        event.save()

        return CreateIsland(
            name=name, trees=trees
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_island = CreateIsland.Field()
