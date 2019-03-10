from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()


class Opportunity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    notes = models.TextField()
    due_date = models.DateTimeField()

    def status(self):
        proposals = Proposal.objects.filter(opportunity_id=self.id).all()
        if len(proposals) == 0:
            return "no proposal"
        else:
            for p in proposals:
                if p.has_contract():
                    return "won"
                # the rest could be smarter
                # if we submitt one but get feedback and a chance to submit another,
                # then we create the new one but haven't submitted it yet,
                # then the status should probably be "WIP" rather than "submitted"
                if p.is_submitted():
                    return "submitted"
            return "WIP"


class Proposal(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.PROTECT)
    commenced = models.DateTimeField()  # default now()
    submitted = models.DateTimeField()  # default None
    contract_ref = models.CharField(max_length=250)

    def is_submitted(self):
        if self.submitted:
            return True
        else:
            return False

    def has_contract(self):
        if self.contract_ref:
            return True
        else:
            return False
