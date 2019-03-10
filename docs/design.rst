System Design
=============

.. graphviz::

   digraph d {
      node [shape=rectangle style=filled fillcolor=white];
   
      BD [label="<<people>>\nbusiness\ndevelopment"];
      arch [label="<<people>>\narchitecture"];
      DM [label="<<people>>\ndelivery\nmanagement"];
      DA [label="<<people>>\nadministrative\nassistants" fillcolor=lightgrey];

      GH [label="GitHub"];
      ts [label="BD Teamsport"];

      node [shape=ellipse];
      ro [label="register\nopportiunity"];
      BD -> ro -> ts;
      rt [label="raise\ntickets" fillcolor=lightgrey];
      DA -> rt -> ts;
      rt -> GH;
      ud [label="update\ndata" fillcolor=lightgrey];
      DA -> ud -> ts;
      ud -> GH;
      ua [label="update\nartefacts"];
      ua -> ts;
      pse [label="pre-sales\nengineering"];
      arch -> pse -> GH;
      pse -> ua;
      size [label="cost\nestimation"];
      DM -> size -> GH;
      size -> ua;
      sc [label="sales-craft"];
      BD -> sc -> GH;
      sc -> ua;
   }

MVP
---

the BD Teamsport has these features:
 * <BD> register opportunity, request proposal, etc
 * <DA> list tickets that should be raised
 * <DA> update proposal status per: github activity

GitHub is used as-is, and the artefacts are MS Word / Excel stuff in the Sharepoint site.

MVP +1
------

in the MVP, we have a peon raising tickets, updating things when tickets change, etc. This should be automated (the peon activity should be orchestrating and communicating with humans, not responding to system events with other system activities)

Beyond MVP
----------

replace excel stuff with database stuff, so we can link planned with actuals (etc).
