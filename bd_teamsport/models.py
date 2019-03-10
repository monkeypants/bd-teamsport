from django.db import models


class Client(models.Model):
    """
    Clients present Opportunities, which become interesting
    when we decide to make a Proposal.
    """
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=250)
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

    def __str__(self):
        return "%s : %s" % (self.client, self.nickname)

    class Meta:
        verbose_name_plural = "Opportunities"


class Proposal(models.Model):
    """
    Initially, Proposals are "submittable thing identies".

    Eventually, we will need a bigger model where
    a Proposal is comprised of one or more CostComponents,
    which are the things the client can actually buy.
    For example, we maye have a “core” Discovery component
    that is a pre-requisite for various (optional)
    “things that come after discovery”.
    There are no hard and fast rules though,
    the architects may propose whatever
    combination of components that they think
    will meet the client’s need.
    CostComponents are the “buyable” chunks
    that form the basis of our offer
    (if more than one,
    it’s not an “all or nothing” proposal)
    """
    opportunity = models.ForeignKey(Opportunity, on_delete=models.PROTECT)
    commenced = models.DateTimeField()  # default now()
    submitted = models.DateTimeField(blank=True, null=True)  # default None
    contract_ref = models.CharField(max_length=250, null=True, blank=True)

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

    def __str__(self):
        return "%s (proposal %s)" % (self.opportunity.nickname, self.id)
