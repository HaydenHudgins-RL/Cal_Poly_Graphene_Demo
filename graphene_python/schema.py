import graphene
import graphql_jwt
import player.schema
import island.schema
import pet.schema
import tree.schema


# Query for getting the data from the server.
class Query(
    player.schema.Query,
    island.schema.Query,
    pet.schema.Query,
    tree.schema.Query,
    graphene.ObjectType
):
    pass


# Mutation for sending the data to the server.
class Mutation(
    player.schema.Mutation,
    island.schema.Mutation,
    pet.schema.Mutation,
    tree.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)
