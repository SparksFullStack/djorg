from graphene_django import DjangoObjectType
import graphene_django
from .models import Notes as NoteModel


class NoteGraphs(DjangoObjectType):
    pass