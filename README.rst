============
bd-teamsport
============

Business Development is a Team Sport.

The code in this repository is a "django app".
It is designed/intended to be included in a django project
as a module of functionality.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "bd_teamsport" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bd_teamsport',
    ]

2. Include the bd_teamsport URLconf in your project urls.py like this::

    path('bd_teamsport/', include('bd_teamsport.urls')),

3. Run `python manage.py migrate` to create the bd_teamsport models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to configure BD (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to take it for a spin.
