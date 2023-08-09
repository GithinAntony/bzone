from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from urllib.parse import unquote

# Create your views here.
def home(request):
    results = Results.objects.all()
    programs = Programs.objects.all()
    context = {'results':results, 'programs:':programs}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact_us(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            contact = Contact_message(
            name=data_record['name'],
            email=data_record['email'],
            message=data_record['message'],
            )
            contact.save()
            messages.success(request, 'Message registered successfully!')
            return redirect('/contact-us')
    context = {'form': form}
    return render(request, 'contact.html', context)

def admin_contactus(request):
    context = { 'contactus' : Contact_message.objects.filter() }
    return render(request, 'admin-contactus.html', context )

#committee_members
def committee_members_login(request):
    form = CMLoginForm()
    if request.method == 'POST':
        form = CMLoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if CommitteeMembers.objects.filter(username=data_record['username']) and CommitteeMembers.objects.filter(
                    password=data_record['password']):
                user_details = CommitteeMembers.objects.get(username=data_record['username'], password=data_record['password'])
                request.session['is_logged_in'] = True
                request.session['email'] = user_details.email
                request.session['full_name'] = user_details.name
                request.session['user_id'] = user_details.id
                request.session['username'] = user_details.username
                request.session['usertype'] = 'committee_members'
                return redirect('/committee-members/dashboard')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/committee-members/login')
    context = {'form': form}
    return render(request, 'committee_members_login.html', context)

def committee_members_register(request):
    form = CMRegisterForm()
    if request.method == 'POST':
        form = CMRegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            committee_members  = CommitteeMembers(
                name=data_record['name'],
                email=data_record['email'],
                username=data_record['username'],
                password=data_record['password'],
                phone=data_record['phone'],
                address=data_record['address'],
            )
            committee_members.save()
            messages.success(request, 'Committee members registered successfully!')
            return redirect('/committee-members/login')
    context = {'form': form}
    return render(request, 'committee_members_registration.html', context)

def candidates_view(request):
    user_details = Candidates.objects.filter().all()
    context = {'user_details': user_details }
    return render(request, 'committee_members_candidates.html', context )

def candidates_delete(request, user_id):
    Candidates.objects.filter(id=user_id).delete()
    messages.error(request, 'Candidates deleted!')
    return redirect('/committee-members/candidates/view')

def candidates_view_status(request, user_id, slug):
    user = Candidates.objects.get(id=user_id)
    user.status = slug
    user.save()
    messages.error(request, 'Candidates status updated!')
    return redirect('/committee-members/candidates/view')

def judges_view(request):
    user_details = Judges.objects.filter().all()
    context = {'user_details': user_details }
    return render(request, 'committee_members_judges.html', context )

def judges_delete(request, user_id):
    Judges.objects.filter(id=user_id).delete()
    messages.error(request, 'Judges deleted!')
    return redirect('/committee-members/judges/view')

def judges_status(request, user_id, slug):
    user = Judges.objects.get(id=user_id)
    user.status = slug
    user.save()
    messages.error(request, 'Judges status updated!')
    return redirect('/committee-members/judges/view')

#candidates
def candidates_login(request):
    form = CLoginForm()
    if request.method == 'POST':
        form = CLoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if Candidates.objects.filter(username=data_record['username']) and Candidates.objects.filter(
                    password=data_record['password']):
                user_details = Candidates.objects.get(username=data_record['username'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['full_name'] = user_details.name
                    request.session['user_id'] = user_details.id
                    request.session['username'] = user_details.username
                    request.session['usertype'] = 'candidates'
                    return redirect('/candidates/dashboard')
                else:
                    messages.error(request, 'Your account is not approved. Come back again!')
                    return redirect('/candidates/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/candidates/login')
    context = {'form': form}
    return render(request, 'candidates_login.html', context)

def candidates_register(request):
    form = CRegisterForm()
    if request.method == 'POST':
        form = CRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['profile_image']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            candidates = Candidates(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            institution_name = data_record['institution_name'],
            phone=data_record['phone'],
            address=data_record['address'],
            profile_image = file_name,
            status='pending',
            )
            candidates.save()
            messages.success(request, 'Candidates registered successfully!')
            return redirect('/candidates/login')
    context = {'form': form}
    return render(request, 'candidates_registration.html', context)

#judges
def judges_login(request):
    form = JLoginForm()
    if request.method == 'POST':
        form = JLoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if Judges.objects.filter(username=data_record['username']) and Judges.objects.filter(
                    password=data_record['password']):
                user_details = Judges.objects.get(username=data_record['username'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['full_name'] = user_details.name
                    request.session['user_id'] = user_details.id
                    request.session['username'] = user_details.username
                    request.session['usertype'] = 'judges'
                    return redirect('/judges/dashboard')
                else:
                    messages.error(request, 'Your account is not approved. Come back again!')
                    return redirect('/judges/login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/judges/login')
    context = {'form': form}
    return render(request, 'judges_login.html', context)

def judges_register(request):
    form = JRegisterForm()
    if request.method == 'POST':
        form = JRegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            judges  = Judges(
                name=data_record['name'],
                email=data_record['email'],
                username=data_record['username'],
                password=data_record['password'],
                phone=data_record['phone'],
                address=data_record['address'],
                status='pending',
            )
            judges.save()
            messages.success(request, 'Judges registered successfully!')
            return redirect('/judges/login')
    context = {'form': form}
    return render(request, 'judges_registration.html', context)

def committee_members_dashboard(request):
    user_details = Candidates.objects.filter().all()
    programs = Programs.objects.filter(committee_member=request.session['user_id'])
    judges_details = Judges.objects.filter().all()
    context = {'user_details': user_details,'programs': programs,'judges_details':judges_details}
    return render(request, 'committee_members_dashboard.html', context )

def candidates_dashboard(request):
    programs = Programs.objects.filter()
    programs_applied = ProgramsApplied.objects.filter(candidate_id=request.session['user_id'])
    judges_details = Judges.objects.filter().all()
    context = {'programs': programs,'programs_applied':programs_applied,'judges_details':judges_details}
    return render(request, 'candidates_dashboard.html',context )

def judges_dashboard(request):
    programs = Programs.objects.filter()
    judges_details = Judges.objects.filter().all()
    programs_judges = Programs.objects.filter(judge=Judges.objects.get(id=request.session['user_id']))
    context = {'programs': programs, 'programs_judges': programs_judges, 'judges_details': judges_details}
    return render(request, 'judges_dashboard.html',context )

def logout(request):
    del request.session['is_logged_in']
    del request.session['email']
    del request.session['full_name']
    del request.session['user_id']
    del request.session['username']
    del request.session['usertype']
    return redirect('/home')

#committee members working
def cm_view_programs(request):
    programs = Programs.objects.filter(committee_member=request.session['user_id'])
    context = {'programs': programs }
    return render(request, 'cm_view_programs.html', context)

def cm_add_programs(request):
    form = CMAddProgram()
    if request.method == 'POST':
        form = CMAddProgram(request.POST)
        if form.is_valid():
          programs = Programs(
          program_name = request.POST['program_name'],
          committee_member = CommitteeMembers.objects.get(id=request.session['user_id']),
          details = request.POST['details'],
          date = request.POST['date'],
          time = request.POST['time'],
          venue = request.POST['venue'],
          judge = Judges.objects.get(id=request.POST['judges']),
          )
          programs.save()
          messages.success(request, 'Programs added successfully!')
          return redirect('/committee-members/programs/view')
    context = {'form': form}
    return render(request, 'cm_add_programs.html', context)

def cm_delete_programs(request,id):
    Programs.objects.filter(id=id).delete()
    messages.error(request, 'Event deleted!')
    return redirect('/committee-members/programs/view')

def cm_view_programs_candidates(request,id):
    programs = ProgramsApplied.objects.filter(program=id)
    context = {'programs': programs }
    return render(request, 'cm_view_programs_candidates.html', context)

def cm_view_programs_candidates_delete(request,id):
    ProgramsApplied.objects.filter(id=id).delete()
    messages.error(request, 'Candidate Cancelled!')
    return redirect('/committee-members/programs/view')

def c_view_programs(request):
    programs = Programs.objects.filter()
    programs_applied = ProgramsApplied.objects.filter(candidate_id=request.session['user_id'])
    context = {'programs': programs, 'programs_applied': programs_applied }
    return render(request, 'c_view_programs.html', context)

def c_actions_programs(request,id,slug):
    if slug == 'apply':
        programs = ProgramsApplied(
            program=Programs.objects.get(id=id),
            candidate=Candidates.objects.get(id=request.session['user_id']),
        )
        programs.save()
        chest_number = programs.pk
        messages.success(request, 'Program applied! Your chest number is #'+ str(chest_number) )
    else:
        ProgramsApplied.objects.filter(program_id=id,candidate_id=request.session['user_id']).delete()
        messages.error(request, 'Program application cancelled!')
    return redirect('/candidates/programs/view')


def j_view_programs(request):
    programs = Programs.objects.filter(judge=Judges.objects.get(id=request.session['user_id']))
    context = {'programs': programs }
    return render(request, 'j_view_programs.html', context)

def j_view_programs_candidates(request,id):
    programsapplied = ProgramsApplied.objects.filter(program=id)
    programs = Programs.objects.filter(id=id)
    context = {'programsapplied': programsapplied, 'programs':programs  }
    return render(request, 'j_view_programs_candidates.html', context)

def j_view_programs_candidates_ajax(request):
    applied_id = request.GET.get('applied_id', None)
    attended_marks = request.GET.get('attended_marks', None)
    attended_select = request.GET.get('attended_select', None)
    attended_remarks = unquote(unquote(request.GET.get('attended_remarks', None)))
    ProgramsApplied.objects.filter(id=applied_id).update(attended=attended_select,marks=attended_marks,remarks=attended_remarks,status='yes')
    data = {}
    data['marks_added'] = 'yes'
    return JsonResponse(data)

def j_publish_results(request,id):
    Programs.objects.filter(id=id).update(published='yes')
    messages.success(request, 'Results Published!')
    return redirect('/judges/programs/view')

def view_results(request,id):
    programsapplied = ProgramsApplied.objects.filter(program=id)
    context = {'programsapplied': programsapplied}
    return render(request, 'view_results.html', context)

def committee_members_contact_us(request):
    contact_us_messages = Contact_message.objects.filter()
    context = {'contact_us_messages': contact_us_messages}
    return render(request, 'committee_members_contact_us.html', context)