===== dannyscrumy =====

dannyscrumy is a simple Django app to conduct Web-based tasks tracking.
For each goal, visitors can create a task, edit and even add more tasks
to it.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "dannyscrumy" to your INSTALLED\_APPS setting like this::

   INSTALLED\_APPS = [ ... 'dannyscrumy', ]

2. Include the dannyscrumy URLconf in your project urls.py like this::
   be mindful of your django version :)

   path('dannyscrumy/', include('dannyscrumy.urls')),

3. Run ``python manage.py migrate`` to create the dannyscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a scrumy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/dannyscrumy/ to participate in the poll.


