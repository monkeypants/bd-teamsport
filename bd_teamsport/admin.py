from django.contrib import admin

from .models import (
    Client,
    Opportunity,
    Proposal
)

admin.site.register(Client)
admin.site.register(Opportunity)
admin.site.register(Proposal)
