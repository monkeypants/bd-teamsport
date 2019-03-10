Process Model
=============

.. uml::

   actor BD
   boundary BDHelper
   boundary GitHubTickets
   boundary GitHubProjects

   BD -> BDHelper: register opportunity
   BD -> BDHelper: launch presales effort
   BDHelper -> GitHubTickets: ensure appropriate milestone exists
   BDHelper -> GitHubTickets: raise opportunity ticket
   BDHelper -> GitHubProjects: add opportunity ticket to Sales WIP
   BDHelper -> GitHubTickets: raise presales engineering (pse) ticket
   BDHelper -> GitHubProjects: add pse ticket to Presales Backlog
   BDHelper -> GitHubTickets: raise (blocked) estimation ticket
   BDHelper -> GitHubProjects: add estimation ticket to Presales Backlog
   BDHelper -> GitHubTickets: raise (blocked) salescraft ticket
   BDHelper -> GitHubProjects: add salescraft ticket to Presales Backlog


Every opportunity has a close date.
The "appropriate milestone"
is the last Friday
before the close date
of the opportunity.

Opportunity, presales engineering,
estimation and salescraft
are all ticket labels
used in a mutually exclusive way.

The opportunity ticket is like an epic,
it links to the other tickets
and is closed when the bid is submitted.

We should probably use
a dedicated kanban board for sales,
with columns for "WIP",
"waiting", "won" and "lost".
Then clean out
the "won" and "lost" columns
each quarter (with ceremony).


.. uml::

   actor BD
   boundary BDHelper
   boundary GitHub
   actor Architect

   BDHelper -> GitHub: raise presales engineering ticket
   activate GitHub
   GitHub <- Architect: move ticket from "Backlog" to "WIP"
   GitHub <- Architect: whiteboard conversation
   BDHelper <- Architect: formalise solution (CostComponents, Time Plan)
   GitHub <- Architect: move ticket to "BD Review"
   BD -> BDHelper: review solution
   BD -> GitHub: finalise ticket
   deactivate GitHub


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
