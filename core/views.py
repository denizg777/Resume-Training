from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, Skill, Work, About, Document


# Create your views here.


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_about = GeneralSetting.objects.get(name='home_about').parameter
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    skill_main_title = Skill.objects.get(name='skill_main_title').parameter

    cv_tr = Document.objects.get(slug='cv_tr').parameter
    cv_en = Document.objects.get(slug='cv_en').parameter



    skill_1 = Skill.objects.get(name='skill_1').parameter
    skill_1_1 = Skill.objects.get(name='skill_1_1').parameter
    skill_1_2 = Skill.objects.get(name='skill_1_2').parameter

    skill_2 = Skill.objects.get(name='skill_2').parameter
    skill_2_1 = Skill.objects.get(name='skill_2_1').parameter
    skill_2_2 = Skill.objects.get(name='skill_2_2').parameter

    skill_3 = Skill.objects.get(name='skill_3').parameter
    skill_3_1 = Skill.objects.get(name='skill_3_1').parameter
    skill_3_2 = Skill.objects.get(name='skill_3_2').parameter
    skill_3_3 = Skill.objects.get(name='skill_3_3').parameter

    skill_4 = Skill.objects.get(name='skill_4').parameter
    skill_4_1 = Skill.objects.get(name='skill_4_1').parameter
    skill_4_2 = Skill.objects.get(name='skill_4_2').parameter
    skill_4_3 = Skill.objects.get(name='skill_4_3').parameter

    project_title = Work.objects.get(name='project_title').parameter
    project_1 = Work.objects.get(name='project_1').parameter
    project_2 = Work.objects.get(name='project_2').parameter
    project_3 = Work.objects.get(name='project_3').parameter
    project_4 = Work.objects.get(name='project_4').parameter

    project_1_short_explain = Work.objects.get(name='project_1_short_explain').parameter
    project_2_short_explain = Work.objects.get(name='project_2_short_explain').parameter
    project_3_short_explain = Work.objects.get(name='project_3_short_explain').parameter
    project_4_short_explain = Work.objects.get(name='project_4_short_explain').parameter

    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter

    sentence_1 = GeneralSetting.objects.get(name='sentence_1').parameter
    sentence_1_writer = GeneralSetting.objects.get(name='sentence_1_writer').parameter
    sentence_2 = GeneralSetting.objects.get(name='sentence_2').parameter
    sentence_2_writer = GeneralSetting.objects.get(name='sentence_2_writer').parameter
    sentence_3 = GeneralSetting.objects.get(name='sentence_3').parameter
    sentence_3_writer = GeneralSetting.objects.get(name='sentence_3_writer').parameter

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_about': home_about,
        'footer_about': footer_about,
        'skill_main_title': skill_main_title,

        'cv_tr': cv_tr,
        'cv_en': cv_en,


        'skill_1': skill_1,
        'skill_1_1': skill_1_1,
        'skill_1_2': skill_1_2,

        'skill_2': skill_2,
        'skill_2_1': skill_2_1,
        'skill_2_2': skill_2_2,

        'skill_3': skill_3,
        'skill_3_1': skill_3_1,
        'skill_3_2': skill_3_2,
        'skill_3_3': skill_3_3,

        'skill_4': skill_4,
        'skill_4_1': skill_4_1,
        'skill_4_2': skill_4_2,
        'skill_4_3': skill_4_3,

        'project_title': project_title,
        'project_1': project_1,
        'project_2': project_2,
        'project_3': project_3,
        'project_4': project_4,

        'project_1_short_explain': project_1_short_explain,
        'project_2_short_explain': project_2_short_explain,
        'project_3_short_explain': project_3_short_explain,
        'project_4_short_explain': project_4_short_explain,

        'sentence_1': sentence_1,
        'sentence_1_writer': sentence_1_writer,

        'sentence_2': sentence_2,
        'sentence_2_writer': sentence_2_writer,

        'sentence_3': sentence_3,
        'sentence_3_writer': sentence_3_writer,

        'contact_mail': contact_mail,
        'contact_phone': contact_phone,

    }
    return render(request, 'index.html', context=context)


def contact(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_address = GeneralSetting.objects.get(name='contact_address').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    context = {
        'footer_about': footer_about,
        'contact_phone': contact_phone,
        'contact_mail': contact_mail,
        'contact_address': contact_address,
        'site_title': site_title,
    }

    return render(request, 'contact.html', context=context)


def services(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    skill_main_title = Skill.objects.get(name='skill_main_title').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    skill_1 = Skill.objects.get(name='skill_1').parameter
    skill_1_1 = Skill.objects.get(name='skill_1_1').parameter
    skill_1_2 = Skill.objects.get(name='skill_1_2').parameter

    skill_2 = Skill.objects.get(name='skill_2').parameter
    skill_2_1 = Skill.objects.get(name='skill_2_1').parameter
    skill_2_2 = Skill.objects.get(name='skill_2_2').parameter

    skill_3 = Skill.objects.get(name='skill_3').parameter
    skill_3_1 = Skill.objects.get(name='skill_3_1').parameter
    skill_3_2 = Skill.objects.get(name='skill_3_2').parameter
    skill_3_3 = Skill.objects.get(name='skill_3_3').parameter

    skill_4 = Skill.objects.get(name='skill_4').parameter
    skill_4_1 = Skill.objects.get(name='skill_4_1').parameter
    skill_4_2 = Skill.objects.get(name='skill_4_2').parameter
    skill_4_3 = Skill.objects.get(name='skill_4_3').parameter

    soft_skill_1 = Skill.objects.get(name='soft_skill_1').parameter
    soft_skill_2 = Skill.objects.get(name='soft_skill_2').parameter
    soft_skill_3 = Skill.objects.get(name='soft_skill_3').parameter
    soft_skill_4 = Skill.objects.get(name='soft_skill_4').parameter

    sentence_1 = GeneralSetting.objects.get(name='sentence_1').parameter
    sentence_1_writer = GeneralSetting.objects.get(name='sentence_1_writer').parameter
    sentence_2 = GeneralSetting.objects.get(name='sentence_2').parameter
    sentence_2_writer = GeneralSetting.objects.get(name='sentence_2_writer').parameter
    sentence_3 = GeneralSetting.objects.get(name='sentence_3').parameter
    sentence_3_writer = GeneralSetting.objects.get(name='sentence_3_writer').parameter

    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'skill_main_title': skill_main_title,
        'site_title': site_title,

        'skill_1': skill_1,
        'skill_1_1': skill_1_1,
        'skill_1_2': skill_1_2,
        'skill_2': skill_2,
        'skill_2_1': skill_2_1,
        'skill_2_2': skill_2_2,
        'skill_3': skill_3,
        'skill_3_1': skill_3_1,
        'skill_3_2': skill_3_2,
        'skill_3_3': skill_3_3,
        'skill_4': skill_4,
        'skill_4_1': skill_4_1,
        'skill_4_2': skill_4_2,
        'skill_4_3': skill_4_3,

        'soft_skill_1': soft_skill_1,
        'soft_skill_2': soft_skill_2,
        'soft_skill_3': soft_skill_3,
        'soft_skill_4': soft_skill_4,

        'sentence_1': sentence_1,
        'sentence_1_writer': sentence_1_writer,
        'sentence_2': sentence_2,
        'sentence_2_writer': sentence_2_writer,
        'sentence_3': sentence_3,
        'sentence_3_writer': sentence_3_writer,

        'contact_phone': contact_phone,

    }

    return render(request, 'services.html', context=context)


def about(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    home_about = GeneralSetting.objects.get(name='home_about').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    about_1 = About.objects.get(name='about_1').parameter
    about_2 = About.objects.get(name='about_2').parameter
    about_3 = About.objects.get(name='about_3').parameter

    goals_intro = About.objects.get(name='goals_intro').parameter
    goals_1 = About.objects.get(name='goals_1').parameter
    goals_2 = About.objects.get(name='goals_2').parameter
    goals_3 = About.objects.get(name='goals_3').parameter
    goals_1_title = About.objects.get(name='goals_1_title').parameter
    goals_2_title = About.objects.get(name='goals_2_title').parameter
    goals_3_title = About.objects.get(name='goals_3_title').parameter

    sentence_1 = GeneralSetting.objects.get(name='sentence_1').parameter
    sentence_1_writer = GeneralSetting.objects.get(name='sentence_1_writer').parameter
    sentence_2 = GeneralSetting.objects.get(name='sentence_2').parameter
    sentence_2_writer = GeneralSetting.objects.get(name='sentence_2_writer').parameter
    sentence_3 = GeneralSetting.objects.get(name='sentence_3').parameter
    sentence_3_writer = GeneralSetting.objects.get(name='sentence_3_writer').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'home_about': home_about,
        'site_title': site_title,

        'about_1': about_1,
        'about_2': about_2,
        'about_3': about_3,
        'goals_intro': goals_intro,
        'goals_1': goals_1,
        'goals_2': goals_2,
        'goals_3': goals_3,
        'goals_1_title': goals_1_title,
        'goals_2_title': goals_2_title,
        'goals_3_title': goals_3_title,

        'sentence_1': sentence_1,
        'sentence_1_writer': sentence_1_writer,
        'sentence_2': sentence_2,
        'sentence_2_writer': sentence_2_writer,
        'sentence_3': sentence_3,
        'sentence_3_writer': sentence_3_writer,

        'contact_phone': contact_phone,

    }

    return render(request, 'about.html', context=context)


def work(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_title = Work.objects.get(name='project_title').parameter
    project_1 = Work.objects.get(name='project_1').parameter
    project_2 = Work.objects.get(name='project_2').parameter
    project_3 = Work.objects.get(name='project_3').parameter
    project_4 = Work.objects.get(name='project_4').parameter
    project_5 = Work.objects.get(name='project_5').parameter
    project_6 = Work.objects.get(name='project_6').parameter
    project_7 = Work.objects.get(name='project_7').parameter

    project_1_short_explain = Work.objects.get(name='project_1_short_explain').parameter
    project_2_short_explain = Work.objects.get(name='project_2_short_explain').parameter
    project_3_short_explain = Work.objects.get(name='project_3_short_explain').parameter
    project_4_short_explain = Work.objects.get(name='project_4_short_explain').parameter
    project_5_short_explain = Work.objects.get(name='project_5_short_explain').parameter
    project_6_short_explain = Work.objects.get(name='project_6_short_explain').parameter
    project_7_short_explain = Work.objects.get(name='project_7_short_explain').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,

        'project_title': project_title,
        'project_1': project_1,
        'project_2': project_2,
        'project_3': project_3,
        'project_4': project_4,
        'project_5': project_5,
        'project_6': project_6,
        'project_7': project_7,

        'project_1_short_explain': project_1_short_explain,
        'project_2_short_explain': project_2_short_explain,
        'project_3_short_explain': project_3_short_explain,
        'project_4_short_explain': project_4_short_explain,
        'project_5_short_explain': project_5_short_explain,
        'project_6_short_explain': project_6_short_explain,
        'project_7_short_explain': project_7_short_explain,
    }

    return render(request, 'work.html', context=context)


def work_single(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_1 = Work.objects.get(name='project_1').parameter
    project_1_short_explain = Work.objects.get(name='project_1_short_explain').parameter
    project_1_short_explain_2 = Work.objects.get(name='project_1_short_explain_2').parameter
    project_1_short_explain_3 = Work.objects.get(name='project_1_short_explain_3').parameter


    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_1': project_1,
        'project_1_short_explain': project_1_short_explain,
        'project_1_short_explain_2': project_1_short_explain_2,
        'project_1_short_explain_3': project_1_short_explain_3,
    }




    return render(request, 'work-single.html', context=context)







def work_single_2(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_2 = Work.objects.get(name='project_2').parameter
    project_2_short_explain = Work.objects.get(name='project_2_short_explain').parameter
    project_2_short_explain_2 = Work.objects.get(name='project_2_short_explain_2').parameter
    project_2_short_explain_3 = Work.objects.get(name='project_2_short_explain_3').parameter



    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_2': project_2,
        'project_2_short_explain': project_2_short_explain,
        'project_2_short_explain_2': project_2_short_explain_2,
        'project_2_short_explain_3': project_2_short_explain_3,


    }




    return render(request, 'work-single-2.html', context=context)

def work_single_3(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_3 = Work.objects.get(name='project_3').parameter
    project_3_short_explain = Work.objects.get(name='project_3_short_explain').parameter
    project_3_short_explain_2 = Work.objects.get(name='project_3_short_explain_2').parameter
    project_3_short_explain_3 = Work.objects.get(name='project_3_short_explain_3').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_3': project_3,
        'project_3_short_explain': project_3_short_explain,
        'project_3_short_explain_2': project_3_short_explain_2,
        'project_3_short_explain_3': project_3_short_explain_3,

    }




    return render(request, 'work-single-3.html', context=context)

def work_single_4(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_4 = Work.objects.get(name='project_4').parameter
    project_4_short_explain = Work.objects.get(name='project_4_short_explain').parameter
    project_4_short_explain_2 = Work.objects.get(name='project_4_short_explain_2').parameter
    project_4_short_explain_3 = Work.objects.get(name='project_4_short_explain_3').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_4': project_4,
        'project_4_short_explain': project_4_short_explain,
        'project_4_short_explain_2': project_4_short_explain_2,
        'project_4_short_explain_3': project_4_short_explain_3,

    }


    return render(request, 'work-single-4.html', context=context)

def work_single_5(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_5 = Work.objects.get(name='project_5').parameter
    project_5_short_explain = Work.objects.get(name='project_5_short_explain').parameter
    project_5_short_explain_2 = Work.objects.get(name='project_5_short_explain_2').parameter
    project_5_short_explain_3 = Work.objects.get(name='project_5_short_explain_3').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_5': project_5,
        'project_5_short_explain': project_5_short_explain,
        'project_5_short_explain_2': project_5_short_explain_2,
        'project_5_short_explain_3': project_5_short_explain_3,

    }

    return render(request, 'work-single-5.html', context=context)


def work_single_6(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_6 = Work.objects.get(name='project_6').parameter
    project_6_short_explain = Work.objects.get(name='project_6_short_explain').parameter
    project_6_short_explain_2 = Work.objects.get(name='project_6_short_explain_2').parameter
    project_6_short_explain_3 = Work.objects.get(name='project_6_short_explain_3').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_6': project_6,
        'project_6_short_explain': project_6_short_explain,
        'project_6_short_explain_2': project_6_short_explain_2,
        'project_6_short_explain_3': project_6_short_explain_3,

    }

    return render(request, 'work-single-6.html', context=context)

def work_single_7(request):
    footer_about = GeneralSetting.objects.get(name='footer_about').parameter
    contact_mail = GeneralSetting.objects.get(name='contact_mail').parameter
    contact_phone = GeneralSetting.objects.get(name='contact_phone').parameter
    site_title = GeneralSetting.objects.get(name='site_title').parameter

    project_7 = Work.objects.get(name='project_7').parameter
    project_7_short_explain = Work.objects.get(name='project_7_short_explain').parameter
    project_7_short_explain_2 = Work.objects.get(name='project_7_short_explain_2').parameter
    project_7_short_explain_3 = Work.objects.get(name='project_7_short_explain_3').parameter

    context = {
        'footer_about': footer_about,
        'contact_mail': contact_mail,
        'contact_phone': contact_phone,
        'site_title': site_title,
        'project_7': project_7,
        'project_7_short_explain': project_7_short_explain,
        'project_7_short_explain_2': project_7_short_explain_2,
        'project_7_short_explain_3': project_7_short_explain_3,

    }

    return render(request, 'work-single-7.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document ,slug=slug)
    return redirect(doc.file.url)
