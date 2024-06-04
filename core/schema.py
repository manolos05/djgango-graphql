import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from books.models import Author, Book
from django.contrib.auth.models import User


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(mutation=Mutation)


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author')


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('name', 'year', 'created_at', 'updated_at')


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, title, description):
        book = Book(title=title, description=description)
        book.save()
        return CreateBookMutation(book=book)


class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBokMutation(message="Libro eliminado")


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
    book = graphene.Field(BookType)

    def mutate(self, info, id, title, description):
        book = Book.objects.get(pk=id)
        book.title = title
        book.description = description
        book.save()
        return UpdateBookMutation(book=book)


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello!")
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.String())

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    # Auth user
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
