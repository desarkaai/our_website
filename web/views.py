"""
Views for the Desarka web application.
"""
from django.shortcuts import render
from django.http import Http404

from .case_studies import CASE_STUDIES, CASE_STUDIES_BY_SLUG


def index_view(request):
    """Homepage view with all main sections."""
    context = {
        'page_title': 'Desarka | Leading Technology & Software Solutions Agency',
        'current_page': 'home',
        'solutions': [
            {'number': '01', 'title': 'ERP Development'},
            {'number': '02', 'title': 'CRM Development'},
            {'number': '03', 'title': 'AI & Automation Solutions'},
            {'number': '04', 'title': 'Custom Software Development'},
            {'number': '05', 'title': 'Website & E-commerce Development'},
            {'number': '06', 'title': 'Mobile App Development'},
            {'number': '07', 'title': 'Embedded Systems & IoT'},
        ],
        'projects': [
            {
                'title': 'Full ERP — inventory, karigar workflow and export documentation',
                'image': 'images/akbar_work.png',
                'logo': 'images/akbar.png',
                'client': 'Akbar',
                'slug': 'akbar-international'
            },
            {
                'title': 'Custom CRM system tailored for business operations',
                'image': 'images/secure_work.png',
                'logo': 'images/securetechav.png',
                'client': 'SecureTech AV',
                'slug': 'securetech-av'
            },
            {
                'title': 'Full-stack e-commerce platform for luxury jewelry',
                'image': 'images/amaarah_work.png',
                'logo': 'images/amaarah.png',
                'client': 'Amaarah',
                'slug': 'amaarah'
            },
            {
                'title': 'Inventory management and replacement tracking system',
                'image': 'images/techmiles_work.png',
                'logo': 'images/techmiles.png',
                'client': 'TechMiles',
                'slug': 'techmills'
            },
            {
                'title': 'Modern brand identity and digital presence',
                'image': 'images/ampluxe_work.png',
                'logo': 'images/ampluxlogo.png',
                'client': 'Ampluxe',
                'slug': 'ampluxe'
            },
            {
                'title': 'Enterprise networking and IT solutions',
                'image': 'images/netmas_work.png',
                'logo': 'images/netmas logo.png',
                'client': 'Netmas',
                'slug': 'netmas'
            },
            {
                'title': 'Live-class booking platform and wellness brand experience',
                'image': 'images/yogher_work.png',
                'logo': 'images/yogher.png',
                'client': 'YogHer',
                'slug': 'yogher'
            },
            {
                'title': 'AI automation that generates book content and images from a topic',
                'image': 'images/oswaal_work.png',
                'logo': 'images/oswaal.png',
                'client': 'Oswaal Books',
                'slug': 'oswaal-books'
            },
        ],
        'companies': [
            {
                'title': 'MediaX OOH:',
                'description': 'At MediaX, we specialize in Out-of-Home (OOH) advertising, delivering innovative campaigns that captivate audiences and leave a lasting impression. Through strategic placements and creative concepts.',
                'image': 'https://api.builder.io/api/v1/image/assets/TEMP/1abcfd1e1a0b5ed19e057d9ee5cfb2d1c97ebb5a?width=1110',
            },
            {
                'title': 'Happening In:',
                'description': 'Happening in offers a premier city and entertainment guide featuring carefully selected recommendations for exploring your city, uncovering hidden gems, and staying informed with the latest buzz.',
                'image': 'https://api.builder.io/api/v1/image/assets/TEMP/79994b933ec6d8a73b2c9f455646f4dcc9d3d402?width=1110',
            },
            {
                'title': 'MediaX Click:',
                'description': 'MediaX CLICK is a dynamic production house specializing in crafting compelling visual narratives. With a keen eye for detail and creativity, we bring stories to life through film, photography, and design.',
                'image': 'https://api.builder.io/api/v1/image/assets/TEMP/edc24c2ff1f06d3ff801781ebedadf1d5d29b52d?width=1110',
            },
        ],
    }
    return render(request, 'index.html', context)


def projects_view(request):
    """Index of client case studies."""
    context = {
        'page_title': 'Our Work | Desarka',
        'current_page': 'projects',
        'case_studies': CASE_STUDIES,
    }
    return render(request, 'projects.html', context)


def case_study_view(request, slug):
    """A single client case study."""
    study = CASE_STUDIES_BY_SLUG.get(slug)
    if study is None:
        raise Http404('No case study matches that address.')

    index = CASE_STUDIES.index(study)
    context = {
        'page_title': f"{study['client']} | Desarka Case Study",
        'current_page': 'projects',
        'study': study,
        'next_study': CASE_STUDIES[(index + 1) % len(CASE_STUDIES)],
    }
    return render(request, 'case_study.html', context)


def placeholder_view(request):
    """Placeholder view for unfinished pages."""
    # Get the current page name from the URL path
    page_name = request.path.strip('/').replace('-', ' ').title()
    if not page_name:
        page_name = 'Page'
    
    context = {
        'page_title': f'{page_name} | Desarka',
        'page_name': page_name,
        'current_page': request.path.strip('/').replace('/', '_'),
    }
    return render(request, 'placeholder.html', context)


def about_view(request):
    """About Us page."""
    context = {
        'page_title': 'About Us | Desarka',
        'current_page': 'about_us',
    }
    return render(request, 'about.html', context)


def connect_view(request):
    """Connect page with contact information."""
    context = {
        'page_title': 'Connect | Desarka',
        'current_page': 'connect',
    }
    return render(request, 'connect.html', context)


def not_found_view(request, exception=None):
    """Custom 404 error page."""
    context = {
        'page_title': 'Page Not Found | Desarka',
    }
    return render(request, '404.html', context, status=404)
