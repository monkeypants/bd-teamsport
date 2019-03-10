Domain Model
============


.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      label="logical model for work costing";

      subgraph cluster_MVP {
         label="MVP"
	 Client -> Opportunity -> Proposal
      }

      subgraph cluster_artefacts {
         label="Artefacts";
	 Proposal -> CostComponent;
	 subgraph cluster_time_plan {
            label="Time Plan";
	    Phase -> SprintWindow;
	 }
	 cm [label="Cost Matrix" shape=folder];
	 CostComponent -> cm;
	 SprintWindow -> cm;
      }
   }


MVP Model
---------

.. autoclass:: bd_teamsport.models.Client

.. autoclass:: bd_teamsport.models.Opportunity

.. autoclass:: bd_teamsport.models.Proposal


Post-MVP model
--------------

The "time plan" is a collection
of **SprintWindows**
(non-overlapping time boxes).
These are organised in **Phases**
(every sprint window belongs to one phase).

We have standardised phases:
 1. Discovery:
 2. ALPHA:
 3. BETA:
 4. LIVE, which may be furthe divided into:
 
    * 4a) Transition to Business As Usual (TBAU); then
    * 4b) Sustainment

In addition to the time plan model,
each proposal also has a cost matrix model.
This is not given to the client specifically,
but is used to calculate
the less detailed cost plan
that the client sees.

The cost martix should also be maintained
each sprint to perform "planned vs. actual" analysis.

Two cost matrix models are proposed.

The both:
 * include a **Role** entity
   (from which the rate card is derived).
 * have dependancy on SprintWindow,
   because the costs are modeled
   at the per-sprint granularity
 * have a dependency on the CostComponent,
   because we need to partition costs
   by component.

This model is probably better.
It starts by linking
the types of resource
that would be requited
for each CostComponent.
These links are **ComponentRoles**.

Then, each ComponentRole
is linked to the SprintWindows
in which that Role
would be required to work
on that component.
These links are **ResourceUnits**,
although "ResourceSchedulePlanningAtom"
might have be a more accurate name.

The ResourceUnits is the level at which
resource allocation is made, in hours.

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      CostComponent;
      SprintWindow;
      subgraph cluster_cost_matrix {
         Role;
	 ComponentRole;
	 Role -> ComponentRole;
	 ResourceUnit
	 ComponentRole -> ResourceUnit
      }
      CostComponent -> ComponentRole;
      SprintWindow -> ResourceUnit;
   }

Alternatively, the CostComponent
can be linked to SprintWindow first,
using a **ResourcePage** model.

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];
      label="logical model for work costing";

      CostComponent;
      SprintWindow;
      subgraph cluster_cost_matrix {
         label="Cost Matrix";
	 ResourcePage;
	 Role;
	 RoleResourcePage [shape=diamond];
	 ResourcePage -> RoleResourcePage;
	 Role -> RoleResourcePage;
      }
      CostComponent -> ResourcePage;
      SprintWindow -> ResourcePage
   }


The ResourcePage means
"If you include this CostComponent,
then any associated work done on it
in this sprint window
needs to be counted here"

The **RoleResourcePage** is
the assertion that we need
a certain quantity
(e.g. 40 hours)
of that Role (e.g. Tech Lead)
for that ResourcePage
(for that CostComponent in that SprintWindow).


Domain Views
------------

TODO elaborate on:

 * The RateCard (filtered for relevant roles)
 * Phase/Sprint Plan(s).
   Potentially multiple,
   if some cost components are optional.
   Dependencies between CostComponents may mean that
   not all permutations are viable.
 * Proposal Outline,
   indicating high-level timeline
   and cost components.
 * planned cost matrix,
   used for planned vs. actuals internal analysis.
