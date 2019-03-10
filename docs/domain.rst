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
   }


Logical model for better quotes:

* a Proposal is the strong entity (anchor of the model)
* One proposal has one or more CostComponents. These are the "buyable" chunks that form the basis of our offer (if more than one, it's not an "all or nothing" proposal)
* Each proposal has a "time plan" model, comprising Phase (Disco, Alpha, Beta, TBAU/Live) and SprintWindow (typically specific fortnights with nominated start and end date).
* SprintWindows are non-overlapping, and always belong to a Phase.
* In addition to the time plan model, each proposal also has a cost matrix model. This is the thing we use in "planned vs. actual analysis" at the per-sprint level.
* The cost matrix model is comprised a SprintComponentResourcePlan (actually, let's call it ResourcePage for short), Role and RoleResourcePage.
* The ResourcePage links a SprintWindow to a CostComponent. It means "If you include this CostComponent, then any associated work done on it in this sprint window needs to be counted here"
* The Role is the same as our rate card (Senior FE Dev, etc)
* The RoleResourcePage is the assertion that we need a certain quantity (e.g. 40 hours) of that Role (e.g. Tech Lead) for that ResourcePage (for that CostComponent in that SprintWindow).
