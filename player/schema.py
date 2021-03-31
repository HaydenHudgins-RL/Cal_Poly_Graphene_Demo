import graphene
from graphene_django import DjangoObjectType
from .models import Player
from django.db.models import Q
import json
from island.schema import Query as IslandQuery
from island.schema import IslandType
from pet.schema import Query as PetQuery
from pet.schema import PetType


class PlayerType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    islands = graphene.List(IslandType)
    pets = graphene.List(PetType)


# Query to get data from the server
class Query(graphene.ObjectType):
    player = graphene.Field(PlayerType, name=graphene.String())
    players = graphene.List(PlayerType)

    def resolve_player(self, info, name=None):
        qs = Player.objects.all()

        # Search records which partially matches name and url
        filter = (
            Q(name=name)
        )
        qs = qs.filter(filter)

        player = qs[0]

        island_names = json.loads(player.islands)

        islands = []

        for island_name in island_names:
            islands.append(IslandQuery().resolve_island({}, island_name))

        pet_names = json.loads(player.pets)

        pets = []

        for pet_name in pet_names:
            pets.append(PetQuery().resolve_pet({}, pet_name))

        return PlayerType(**{
            "id": player.id,
            "name": player.name,
            "age": player.age,
            "islands": islands,
            "pets": pets,
        })

    def resolve_players(self, info):
        qs = Player.objects.all()

        players = []

        for player in qs:
            island_names = json.loads(player.islands)

            islands = []

            for island_name in island_names:
                islands.append(IslandQuery().resolve_island({}, island_name))

            pet_names = json.loads(player.pets)

            pets = []

            for pet_name in pet_names:
                pets.append(PetQuery().resolve_pet({}, pet_name))

            players.append(PlayerType(**{
                "id": player.id,
                "name": player.name,
                "age": player.age,
                "islands": islands,
                "pets": pets,
            }))

        return players


# Create new Event
class CreatePlayer(graphene.Mutation):
    name = graphene.String()
    age = graphene.Int()
    islands = graphene.List(graphene.String)
    pets = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        islands = graphene.List(graphene.String)
        pets = graphene.List(graphene.String)

    def mutate(self, info, name, age, islands, pets):
        islands = json.dumps(islands)
        pets = json.dumps(pets)
        event = Player(name=name, age=age, islands=islands, pets=pets)
        event.save()

        return CreatePlayer(
            name=event.name,
            age=age, islands=islands, pets=pets
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_player = CreatePlayer.Field()
