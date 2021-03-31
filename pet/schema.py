import graphene
from .models import Pet
from django.db.models import Q


class PetType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


# Query to get data from the server
class Query(graphene.ObjectType):
    pet = graphene.Field(PetType, name=graphene.String())
    pets = graphene.List(PetType)

    def resolve_pet(self, info, name=None):
        qs = Pet.objects.all()

        # Search records which partially matches name and url
        filter = (
            Q(name=name)
        )
        qs = qs.filter(filter)

        pet = qs[0]

        return PetType(**{
            "id": pet.id,
            "name": pet.name,
            "age": pet.age,
        })

    def resolve_pets(self, info):
        qs = Pet.objects.all()

        return qs


# Create new Event
class CreatePet(graphene.Mutation):
    name = graphene.String()
    age = graphene.Int()

    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    def mutate(self, info, name, age):
        event = Pet(name=name, age=age)
        event.save()

        return CreatePet(
            name=event.name,
            age=age,
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_pet = CreatePet.Field()
