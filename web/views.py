"""
Views for the Desarka web application.
"""
from django.shortcuts import render
from django.http import Http404

from .case_studies import CASE_STUDIES, CASE_STUDIES_BY_SLUG
from . import solutions as solutions_content
from .solutions import SOLUTIONS, FEATURES


def index_view(request):
    """Homepage view with all main sections."""
    context = {
        'page_title': 'Desarka | Leading Technology & Software Solutions Agency',
        'current_page': 'home',
        'solutions': SOLUTIONS,
        'features': FEATURES,
        'projects': [
            {
                'title': 'Full ERP — inventory, karigar workflow and export documentation',
                'image': 'images/work/akbar.webp',
                'logo': 'images/akbar.png',
                'client': 'Akbar',
                'cover': 'images/work/akbar.webp',
                'tags': 'ERP · Inventory · Export documentation',
                'slug': 'akbar-international'
            },
            {
                'title': 'Custom CRM system tailored for business operations',
                'image': 'images/secure_work.png',
                'logo': 'images/securetechav.png',
                'client': 'SecureTech AV',
                'cover': 'images/work/securetech-av.webp',
                'tags': 'CRM · Custom software',
                'slug': 'securetech-av'
            },
            {
                'title': 'Full-stack e-commerce platform for luxury jewelry',
                'image': 'images/amaarah_work.png',
                'logo': 'images/amaarah.png',
                'client': 'Amaarah',
                'cover': 'images/work/amaarah.webp',
                'tags': 'E-commerce · Website',
                'slug': 'amaarah'
            },
            {
                'title': 'Inventory management and replacement tracking system',
                'image': 'images/techmiles_work.png',
                'logo': 'images/techmiles.png',
                'client': 'TechMiles',
                'cover': 'images/work/techmills.webp',
                'tags': 'Inventory · Replacement tracking',
                'slug': 'techmills'
            },
            {
                'title': 'Modern brand identity and digital presence',
                'image': 'images/ampluxe_work.png',
                'logo': 'images/ampluxlogo.png',
                'client': 'Ampluxe',
                'cover': 'images/work/ampluxe.webp',
                'tags': 'Brand identity · Website',
                'slug': 'ampluxe'
            },
            {
                'title': 'Enterprise networking and IT solutions',
                'image': 'images/netmas_work.png',
                'logo': 'images/netmas logo.png',
                'client': 'Netmas',
                'cover': 'images/work/netmas.webp',
                'tags': 'Website · Product catalogue',
                'slug': 'netmas'
            },
            {
                'title': 'Live-class booking platform and wellness brand experience',
                'image': 'images/yogher_work.png',
                'logo': 'images/yogher.png',
                'client': 'YogHer',
                'cover': 'images/work/yogher.webp',
                'tags': 'Booking platform · Website',
                'slug': 'yogher'
            },
            {
                'title': 'AI automation that generates book content and images from a topic',
                'image': 'images/oswaal_work.png',
                'logo': 'images/oswaal.png',
                'client': 'Oswaal Books',
                'cover': 'images/work/oswaal.webp',
                'tags': 'AI automation · Content generation',
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


def solutions_view(request):
    """Index of everything Desarka builds."""
    context = {
        'page_title': 'Our Solutions | Desarka',
        'current_page': 'solutions',
        'solutions': SOLUTIONS,
    }
    return render(request, 'solutions.html', context)


def solution_detail_view(request, slug):
    """A single solution, with outcomes, capabilities, process and FAQs."""
    solutions_by_slug = getattr(solutions_content, 'SOLUTIONS_BY_SLUG', None)
    if not solutions_by_slug:
        solutions_by_slug = {item['slug']: item for item in SOLUTIONS}

    solution = solutions_by_slug.get(slug)
    if solution is None:
        raise Http404('No solution matches that address.')

    slugs = [item['slug'] for item in SOLUTIONS]
    index = slugs.index(slug)
    related_case_studies = [
        CASE_STUDIES_BY_SLUG[study_slug]
        for study_slug in solution.get('related_case_studies') or []
        if study_slug in CASE_STUDIES_BY_SLUG
    ]

    context = {
        'page_title': f"{solution['title']} | Desarka",
        'current_page': 'solutions',
        'solution': solution,
        'prev_solution': SOLUTIONS[(index - 1) % len(SOLUTIONS)],
        'next_solution': SOLUTIONS[(index + 1) % len(SOLUTIONS)],
        'related_case_studies': related_case_studies,
    }
    return render(request, 'solution_detail.html', context)
