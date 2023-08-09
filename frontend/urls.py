from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact-us', views.contact_us, name='contact-us'),
    #path('programs', views.programs, name='programs'),
    #path('results', views.results, name='results'),
    path('committee-members/login', views.committee_members_login, name='committee-members-login'),
    path('committee-members/register', views.committee_members_register, name='committee-members-register'),
    path('committee-members/contact-us', views.committee_members_contact_us, name='committee-members-contact-us'),

    path('candidates/login', views.candidates_login, name='candidates-login'),
    path('candidates/register', views.candidates_register, name='candidates-register'),
    path('judges/login', views.judges_login, name='judge-login'),
    path('judges/register', views.judges_register, name='judge-register'),

    path('committee-members/dashboard', views.committee_members_dashboard, name='cm-dashboard'),

    path('committee-members/candidates/view', views.candidates_view, name='cm-dashboard'),
    path('committee-members/candidates/status/<int:user_id>/<slug:slug>', views.candidates_view_status, name='candidates-view-status'),
    path('committee-members/candidates/delete/<int:user_id>', views.candidates_delete,
         name='dashboard'),

    path('committee-members/judges/view', views.judges_view, name='cm-dashboard'),
    path('committee-members/judges/status/<int:user_id>/<slug:slug>', views.judges_status, name='judges-status'),
    path('committee-members/judges/delete/<int:user_id>', views.judges_delete,
         name='dashboard'),

    path('committee-members/programs/view', views.cm_view_programs, name='cm_view_programs'),
    path('committee-members/programs/add', views.cm_add_programs, name='cm_programs_add'),
    path('committee-members/programs/delete/<int:id>', views.cm_delete_programs, name='cm_programs_delete'),
    path('committee-members/programs/view-candidates/<int:id>', views.cm_view_programs_candidates,
         name='cm_view_programs_candidates'),
    path('committee-members/programs/view-candidates/delete/<int:id>', views.cm_view_programs_candidates_delete,
         name='cm_view_programs_candidates_delete'),

    path('candidates/dashboard', views.candidates_dashboard, name='cm-dashboard'),
    path('candidates/programs/view', views.c_view_programs, name='view-programs'),
    path('candidates/programs/action/<int:id>/<slug:slug>', views.c_actions_programs, name='action-programs'),


    path('judges/dashboard', views.judges_dashboard, name='cm-dashboard'),
    path('judges/programs/view', views.j_view_programs, name='cm_view_programs'),
    path('judges/programs/view-candidates/<int:id>', views.j_view_programs_candidates,
         name='j_view_programs_candidates'),
    path('judges/programs/view-candidates-ajax', views.j_view_programs_candidates_ajax,
         name='j_view_programs_candidates_ajax'),
    path('judges/programs/publish-results/<int:id>', views.j_publish_results,
         name='j_publish_results'),
    path('programs/view-results/<int:id>', views.view_results,
         name='view_results'),

    path('logout', views.logout, name='logout'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)