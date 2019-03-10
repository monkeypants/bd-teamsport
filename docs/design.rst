System Design
=============

The system is a combination of:
 * GitHub
 * BD Teamsport

BD Teamsport is a logical concept.

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


To begin with, it may be a collection of spreadsheets
in that horrible acursed Microsoft website thing
that keeps locking me out
(may the devil damn it's eyes).
Eventually, it may be entirely consumed by django features.

In between, a team responsible for business development
in a real software development agency will improve it
iteratively based on their needs. 
Pull requests also welcome :)

MVP
---


The BD Teamsport has these features:
 * <BD> register opportunity, request proposal, etc
 * <DA> list tickets that should be raised
 * <DA> update proposal status per: github activity

GitHub is used as-is,
using tickets and kanban boards.
The artefacts will be spreadsheets
that live in a place where the team can access them.

TODO:
 * <epic> document preciecly how to configure GitHub
 * <epic> show by example spreadsheet artefacts
 * <epic> build the minimum viable django features required for orchestration


MVP +1
------

In the MVP, we have peon-work
raising tickets, updating things when tickets change, etc.
This should be automated
The focus of administrative activity
should be shifted "up the stack" 
towards management
(orchestrating and communicating with humans,
not responding to system events
with other system activities).


Beyond MVP
----------

Replace excel stuff with database stuff, so we can link planned with actuals (etc).
