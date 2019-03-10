Pocesses
========

Register Opportunity
--------------------

Currently, when the business development manager
identifies an opportunity,
there is an ad-hoc email communication
that may or may not result in a decision
to invest in making a commercial bid.

When there is a decision
to invest in making a commercial bid,
the email conversation continues
with some friction and impedance.

The lack of contemporary structure data
about the "stocks and flows" of presales work
limits our capacity to work efficiently
when there is more work in the pipeline
than one person can hold in their head.

In the future:
 * conversations about prospects will still occur
 * pre-sales work will be intiated in a system
 * structured data will be maintained
   as a consequence of using the system
 * stocks and flows analysis will allow us
   to improve efficiency and effectiveness
   of our business development effort.
   
.. code:: gherkin

   So that teamwork orchestration occurs using the GitHub system
   As a BD Manager
   I need to launch presales effort on the BD Teamwork app


.. uml::

   actor BD
   boundary BDTeamsport
   boundary GitHubTickets
   boundary GitHubProjects

   BD -> BDTeamsport: register opportunity
   BD -> BDTeamsport: launch presales effort
   BDTeamsport -> GitHubTickets: ensure appropriate milestone exists
   BDTeamsport -> GitHubTickets: raise presales engineering (pse) ticket
   BDTeamsport -> GitHubProjects: add pse ticket to Backlog
   BDTeamsport -> GitHubTickets: raise (blocked) estimation ticket
   BDTeamsport -> GitHubProjects: add estimation ticket to Backlog
   BDTeamsport -> GitHubTickets: raise (blocked) salescraft ticket
   BDTeamsport -> GitHubProjects: add salescraft ticket to Backlog


Notes about opportunity registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 * Every opportunity has a close date.
   This is important because the timeframes are usually not negotiable
 * The "appropriate milestone"
   is the last Friday
   before the close date
   of the opportunity.
   This allows us to
   drive improvement with a weekly
   retrospective/review process.
 * Within GitHub, Opportunity,
   presales engineering, estimation and salescraft
   are all ticket labels
   used in a mutually exclusive way.
 * We should use GitHub project boards
   with columns for "WIP", "BD Review",
   "Salescraft", "Approving", "Dispatched"
   "Won :)" and "Lost :("
 * The "won" and "lost" columns
   should be cleared out periodically.
   Quarterly? (with ceremony).


Presales Engineering
--------------------

Currently, after the email conversation
results in a decision to submit a bid,
there may or may not be some investigation
into requirements and client research.

After that, the bulk of the presales
engineering work is conducted
in a single session at the whiteboard,
with one or two architects
and a tech lead with relevent expertise.

During the whiteboard session,
the board is typically photographed
and wiped/redrawn a number of times.

After that, there is
a chaotic and disorganised tranistion
into cost estimation.

In the future:
 * The whiteboard session will largely be unchanged,
   except for gradual refinement.
 * The whiteboard session will be scheduled
   in a more organised way.
 * There will be an orderly transition
   from presales engineering into cost estimation.
 * GitHub will be used to orchestrate
   the presales engineering work,
   in much the same way as
   we manage most development work.
 * The presales artefacts
   (including Cost Components,
   and Time Plane)
   will be more standardised,
   which will reduce the effort
   and communication overhead
   required for Salescraft.

   
.. code:: gherkin

   So that I can minimise the burden of context switching
   As an Architect
   I need to manage presales engineering tasks with GitHub


.. uml::

   actor BD
   boundary BDTeamsport
   boundary GitHub
   actor Architect

   BDTeamsport -> GitHub: raise presales engineering ticket
   activate GitHub
   GitHub <- Architect: move ticket from "Backlog" to "WIP"
   GitHub <- Architect: whiteboard conversation
   BDTeamsport <- Architect: formalise solution (CostComponents, Time Plan)
   GitHub <- Architect: move ticket to "BD Review"
   BD -> BDTeamsport: review solution
   BD -> GitHub: finalise ticket
   deactivate GitHub


Notes about presales engineering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 * We may introduce a "clarkitect" role
   to the whiteboard sessions.
   This would give developers and delivery managers
   an opportunity to gain experience
   with pre-sales engineering.
   The clarkitect would be responsible
   for creating/updating formal artefacts
   and associated ticket-craft.
 * We may experiment with adding new techniques
   to the whiteboard session
   such as "talk to camera" diagram explanation.
   This would increase the need for clarkitechture.



Cost Estimation
---------------

Cost estimation is the magical soothsaying process
that creates a spreadsheet saying
"these people will work
for this much time
to get the job done".

It actually works by composing team profiles
(these people)
and predicting the work that needs to be done
at a suitable granularity
so that when the chunks of work
are allocated to those teams
we believe the prediction
that the team can get them done
with 2 weeks effort.

It's an approximate and scairy process
involving judgement and experience,
as well as balanced compromise
between asking for too much money
and overestimating how much can be done.

Reviewing resource plans with different "trades"
tends to make them better.
These conversations are
time consuming (and therefor expensive),
but immensively valuable
because they reality-check the predictions
and reduce risk.

We often struggle to
to shop the cost plans around
as much as we like,
due to deadlines.

In the future:

 * We will start with standardised inputs,
   giving us the ability to be more consistent over time.
 * We will manage the cost-planning process
   with GitHub tickets, improving visability
   and opportunities for review and input


.. uml::

   actor BD
   boundary BDHelper
   boundary GitHub
   actor DeliveryManager

   BDHelper -> GitHub: raise estimation task
   activate GitHub
   GitHub <- GitHub: task unblocked
   GitHub <- DeliveryManager: move ticket from "Backlog" to "WIP"
   GitHub <- DeliveryManager: discuss scope/resourcing
   BDHelper <- DeliveryManager: formalise costings (Cost Matrix)
   GitHub <- DeliveryManager: move ticket to "BD Review"
   BD -> BDHelper: review costings
   BD -> GitHub: finalise ticket
   deactivate GitHub


Salescraft
----------

Currently, the BD
has to beg and cajole
to get the inputs they need
in a timely fashon.

Then they perform salescraft
in a "mad rush" to meet their deadlines.

The BD is usually presented with
slightly incoherent information,
or coherent information in an unfamiliar format,
so the first version of the salescraft
often misrepresents the thinking behind it.
This means there are usually multiple rounds
of review and change.

In the future:

 * Our mature development rituals,
   including Delivery Management activity
   will ensure presales engineering
   and cost estimation tasks
   are performed in an organised and timely manner
   (without the BD having to drive it)
 * Salescraft inputs will be in standardised formats
   so that we can improve iteratively.
 * Transparent and tracable ticket histories
   will reduce the BD's need
   to seek explanation.
 * There will still be review
   and improvement iterations,
   but they will be more efficient
   and enjoyable.


.. uml::

   actor BD
   boundary BDHelper
   boundary GitHub
   actor Director


   BDHelper -> GitHub: raise salescraft task
   activate GitHub
   GitHub <- GitHub: task unblocked
   BD -> GitHub: move ticket from "Backlog" to "WIP"
   BD -> BDHelper: draft pitch
   BD -> GitHub: move ticket to "Approval"
   BDHelper <- Director: review pitch
   GitHub <- Director: move ticket to "OK"
   BD -> BDHelper: send to client
   BD -> GitHub: finalise ticket
   deactivate GitHub
