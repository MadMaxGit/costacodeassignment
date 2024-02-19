from graphene import Schema, ObjectType, String, Int, Field, List, Mutation
import requests

class UserType(ObjectType):
    id = Int()
    name= String()
    age=Int()
    place= String()

class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    #user_by_min_age = List(UserType, min_age=Int())

    #dummy data store
    users = [
        {"id":1, "name": "Man", "age": 33},
        {"id":2, "name": "Shi", "age": 31},
        {"id":3, "name": "Tri", "age": 3, "place": "Bang"},
        {"id":4, "name": "Ok", "age": 29}
    ]

    @staticmethod
    def resolve_user(root, info, user_id):
        matched_users = [user for user in Query.users if user["id"] == user_id]
        return matched_users[0] if matched_users else None
    
    @staticmethod
    def resolve_user_by_min_age(root, info, min_age):
        return [user for user in Query.users if user["age"] >= min_age]

gpl_query='''
query{
    user(userId: 1){
        id
        name
        age
        place
    }
}
'''

schema = Schema(query=Query)

if __name__ == "__main__":
    result = schema.execute(gpl_query)