"""
Case study content for the Our Work / Projects section.

Every factual claim here was taken from the client's own live website
(researched 31 Aug 2026) or from the engagement description already used on
the homepage. Nothing is estimated. When real delivery metrics become
available, add them to the 'facts' list of the relevant study.
"""

CASE_STUDIES = [
    {
        'slug': 'akbar-international',
        'client': 'Akbar International',
        'logo': 'images/akbar.png',
        'image': 'images/akbar_erp_dashboard.png',
        'sector': 'Stone & marble carving · manufacturing and export',
        'engagement': 'Full ERP — inventory, karigar workflow and export documentation',
        'url': '',
        'standfirst': (
            'The largest system we have built: a two-module ERP that follows a block of '
            'marble from the quarry, through the hands of the karigars who carve it, to a '
            'customs-filed invoice in another country.'
        ),
        'facts': [
            ('Engagement', 'Full ERP · inventory + export'),
            ('Screens', '8 inventory · 10 export'),
            ('Deployment', 'Web, plus a packaged Windows desktop build'),
            ('Replaces', 'A legacy desktop app whose source code was lost'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'Akbar International carves stone and marble — tableware, decor and inlay '
                    'work in traditional Pietra Dura and lattice styles — and exports it '
                    'worldwide. The business runs on two things most software does not model: '
                    'karigars, the artisans who take raw material away and return finished '
                    'work, and export paperwork that is filed with customs.',
                ],
            },
            {
                'heading': 'Why off-the-shelf inventory software fails here',
                'paras': [
                    'A slab of marble does not stay one thing. It arrives as raw material, is '
                    'issued to a karigar, comes back as carved work, and is finally a finished '
                    'piece with a SKU — and the same physical stone can be split across several '
                    'of those states at once. Standard inventory tools count what is on a shelf. '
                    'They cannot answer where a lot is when it is halfway through being carved '
                    'in someone else’s workshop.',
                    'The system is built around the lot as the unit of inventory, moving through '
                    'stages with an append-only stock ledger recording every movement, so the '
                    'on-hand figure is always reconstructable rather than merely asserted.',
                ],
            },
            {
                'heading': 'What we built',
                'bullets': [
                    'An eight-screen inventory module — dashboard, masters, inward, issue, '
                    'payments, stock, reports and a reversal-approvals queue',
                    'A ten-screen export module taking a shipment from order form through '
                    'packing, invoice and the document set customs requires',
                    'Karigar labour booked at the moment work is delivered, not when material '
                    'is issued — because that is when the quantity done and the agreed rate are '
                    'actually known',
                    'Which documents a shipment needs is derived from carrier, destination, '
                    'incoterm and cargo type, then frozen at posting, so an operator never has '
                    'to remember a rule and a filed shipment cannot change retroactively',
                    'Gapless export invoice numbering that resets each financial year, because '
                    'those serials are filed with customs and cannot have holes',
                    'Statutory validation shared by the server and the browser from a single '
                    'source — GSTIN check digit, PAN, TAN, Aadhaar, IFSC',
                    'Editable, versioned document templates that record which version printed '
                    'each issued document, so a reprint years later is faithful',
                ],
            },
            {
                'heading': 'Two details worth naming',
                'paras': [
                    'The pricing formulas were not designed, they were recovered. The legacy '
                    'system’s source code was gone, so its rules had to be derived from the data '
                    'it left behind and verified against 3,891 historical packages — including '
                    'discovering that a column labelled CBM had never held cubic metres at all, '
                    'but dimensional weight.',
                    'Foreign-currency and rupee valuations are kept strictly independent rather '
                    'than one being calculated from the other, because in the legacy records '
                    'they agreed less than a fifth of the time. Collapsing them would have '
                    'quietly corrupted every domestic tax invoice.',
                ],
            },
        ],
        'quote': None,
    },
    {
        'slug': 'securetech-av',
        'client': 'SecureTech AV',
        'logo': 'images/securetechav.png',
        'image': 'images/secure_work.png',
        'sector': 'Audio-visual integration',
        'engagement': 'Custom CRM system tailored for business operations',
        'url': 'https://www.securetechav.com/',
        'standfirst': (
            'A Noida AV integrator running long, multi-stage installations across six '
            'sectors — and a pipeline that had outgrown spreadsheets.'
        ),
        'facts': [
            ('Engagement', 'Custom CRM'),
            ('Base', 'Noida, Uttar Pradesh'),
            ('Sectors served', 'Corporate, education, healthcare, public sector, retail, residential'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'SecureTech AV Designs positions itself as a premium audio-visual integrator, '
                    'covering smart integration, AV controls and ICT infrastructure. The work ranges '
                    'from boardrooms and digital signage to stadiums and arenas, club sound systems, '
                    'cinema halls and auditoriums, delivered through partnerships with Sennheiser, '
                    'QSC, Christie, Sony, Cisco and LG.',
                    'Their published Google rating is 4.9 across 51 reviews, and reviewers '
                    'consistently name the same two things: deadlines met, and service after handover.',
                ],
            },
            {
                'heading': 'Why a generic CRM did not fit',
                'paras': [
                    'An AV integration is not a sales pipeline that closes on signature. One job moves '
                    'through site survey, acoustic design, procurement, installation, commissioning, '
                    'handover and then an open-ended service relationship — with different equipment '
                    'vendors and a different approval chain in every sector they serve.',
                    'Off-the-shelf CRMs model leads and deals. They do not model a half-installed '
                    'auditorium.',
                ],
            },
            {
                'heading': 'What we built',
                'paras': [
                    'A custom CRM shaped around AV project delivery rather than generic deal stages — '
                    'tracking an enquiry through to post-installation service in the stages an '
                    'integrator actually works in.',
                ],
            },
        ],
        'quote': {
            'text': (
                'A comprehensive AV integration project across our office premises, including '
                'conference rooms, meeting rooms, townhall setup, and auditorium — the experience '
                'was excellent.'
            ),
            'cite': 'Abhishek Mishra · Google review of SecureTech AV',
        },
    },
    {
        'slug': 'amaarah',
        'client': 'Amaarah',
        'logo': 'images/amaarah.png',
        'image': 'images/amaarah_work.png',
        'sector': 'Jewellery e-commerce',
        'engagement': 'Full-stack e-commerce platform for luxury jewellery',
        'url': 'https://amaarah.co.in/',
        'standfirst': (
            'Selling fine jewellery online means selling something people expect to hold '
            'first. The build had to close that gap.'
        ),
        'facts': [
            ('Engagement', 'Full-stack e-commerce platform'),
            ('Tagline', 'Ace the Grace'),
            ('Catalogue', 'Rings, earrings, bracelets & bangles, necklaces, solitaires, '
                          "mangalsutras, men's jewellery, gifting"),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'Amaarah is an online jewellery retailer selling across eight categories, from '
                    'everyday rings and earrings to mangalsutras, solitaires and gifting. The range '
                    "spans traditional and contemporary, with a dedicated men's line.",
                ],
            },
            {
                'heading': 'The problem with jewellery online',
                'paras': [
                    'Two things stop a jewellery sale on the web. The buyer cannot judge the piece, '
                    'and the buyer cannot judge the price — gold moves daily and a diamond’s grade '
                    'is invisible in a product photo.',
                ],
            },
            {
                'heading': 'What we built',
                'paras': [
                    'A full-stack storefront where the education sits beside the catalogue rather '
                    'than in a forgotten help section:',
                ],
                'bullets': [
                    'Category-led browsing across the full range, with separate paths for gifting '
                    "and men's jewellery",
                    'A Diamond Guide, Jewelry Guide and Gemstone Guide, so a first-time buyer can '
                    'learn the vocabulary before committing',
                    'A live gold rate calculator, addressing the pricing objection directly',
                    'Cart, accounts and order status, with an admin surface for catalogue management',
                    'Return policy and contact routes surfaced site-wide, not buried at checkout',
                ],
            },
        ],
        'quote': None,
    },
    {
        'slug': 'techmills',
        'client': 'TechMiles',
        'logo': 'images/techmiles.png',
        'image': 'images/techmiles_work.png',
        'sector': 'Computer hardware · retail & service',
        'engagement': 'Inventory management and replacement tracking system',
        'url': 'https://techmillsindia.in/login',
        'url_label': 'Open the system (login required)',
        'standfirst': (
            'The one project here with nothing to show off publicly — because the whole '
            'product sits behind a login, which is exactly the point.'
        ),
        'facts': [
            ('Engagement', 'Inventory management & replacement tracking'),
            ('Operating name', 'Maa Vaishno Computers'),
            ('Access', 'Authenticated — staff only'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'TechMills India — trading as Maa Vaishno Computers — is a computer hardware '
                    'business whose brand line reads “Technology never before”. Their operation runs '
                    'on stock that moves fast and warranty claims that must be traced to the unit.',
                ],
            },
            {
                'heading': 'The real difficulty: replacements',
                'paras': [
                    'Ordinary inventory software counts what you have. Hardware retail needs '
                    'something harder. A failed part goes back to the distributor, a replacement '
                    'comes forward, and in between the item exists in neither the shelf count nor '
                    'the sold count — while a customer waits and a warranty clock runs.',
                    'Get that wrong and stock reconciles to a number nobody trusts.',
                ],
            },
            {
                'heading': 'What we built',
                'paras': [
                    'An authenticated inventory system with replacement tracking as a first-class '
                    'flow rather than an afterthought, so a unit under RMA stays visible and '
                    'accountable for its whole journey out and back.',
                ],
            },
        ],
        'quote': None,
    },
    {
        'slug': 'netmas',
        'client': 'Netmas',
        'logo': 'images/netmas logo.png',
        'image': 'images/netmas_work.png',
        'sector': 'Pro audio accessories · manufacturing',
        'engagement': 'Brand site and product catalogue for an audio accessories manufacturer',
        'url': 'https://www.netmas.in/',
        'standfirst': (
            'An Indian cable and connector manufacturer whose entire pitch is reliability — '
            'sold to engineers who have been let down by cables before.'
        ),
        'facts': [
            ('Engagement', 'Brand site & product presence'),
            ('Base', 'A-70, Sector 33, Noida 201301'),
            ('Product lines', 'Cables, connectors, projector screens, floor boxes, racks, '
                              'cable managers'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'Netmas manufactures audio accessories in India, stating a mission to give '
                    'enthusiasts and professionals gear built for sound clarity, reliability and '
                    'performance. Their range runs from cables and connectors through to the '
                    'unglamorous infrastructure of an install — floor boxes, racks and cable '
                    'managers — and Make-in-India provenance is central to how they sell.',
                ],
            },
            {
                'heading': 'The positioning problem',
                'paras': [
                    'Cables are the definition of a commodity purchase. Buyers reach for the '
                    'cheapest option until one fails during a live event, and the site has to make '
                    'the case for quality before that failure teaches the lesson.',
                ],
            },
            {
                'heading': 'What the site does',
                'bullets': [
                    'Opens on a macro shot of a connector — the product treated as engineering, '
                    'not packaging',
                    'Runs a persistent “Based in India” marquee, making provenance a design element '
                    'rather than a footnote',
                    'Splits six product families into their own routes, so an installer lands on '
                    'the right category',
                    'Leads to an enquiry form rather than a cart, matching how B2B AV components '
                    'are actually bought',
                ],
            },
        ],
        'quote': {
            'text': 'Enhancing every connection, amplifying every note.',
            'cite': 'Netmas · site headline',
        },
    },
    {
        'slug': 'ampluxe',
        'client': 'Ampluxe',
        'logo': 'images/ampluxlogo.png',
        'image': 'images/ampluxe_work.png',
        'sector': 'Display & projection technology',
        'engagement': 'Modern brand identity and digital presence',
        'url': 'https://ampluxe.in/',
        'standfirst': (
            'Four product families, wildly different buyers, one site that had to sell a '
            '165-inch LED wall and a fixed-frame projector screen with equal conviction.'
        ),
        'facts': [
            ('Engagement', 'Brand identity & digital presence'),
            ('Tagline', 'Amplify your Luxury'),
            ('Product lines', 'Projector screens · interactive flat panels (65–98") · '
                              'active LED (P1.5–P10) · all-in-one LED (120–165")'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'Ampluxe supplies digital screens, projectors and displays to businesses of '
                    'every size, all locally produced under Make in India. The catalogue spans '
                    'motorised and fixed projector screens, interactive flat panels across four '
                    'sizes, indoor and outdoor LED cabinets at six pixel pitches, and seamless '
                    'all-in-one LED up to 165 inches.',
                ],
            },
            {
                'heading': 'The challenge',
                'paras': [
                    'A school buying an interactive panel and a stadium buying a P10 outdoor '
                    'cabinet share almost nothing — not budget, not vocabulary, not decision '
                    'timeline. A single catalogue page written for both persuades neither.',
                ],
            },
            {
                'heading': 'What the site does',
                'bullets': [
                    'Splits the four product families into distinct routes with their own '
                    'specification language',
                    'Leads with a spec strip — 4K HDR, refresh rate, eye-comfort blue-light '
                    'filtering — so technical buyers get numbers immediately',
                    'Carries five capability pillars (full-service delivery, in-house design team, '
                    'custom builds, global installation, materials) for buyers evaluating the '
                    'vendor, not the panel',
                    'Foregrounds Make in India as a procurement argument, which matters for '
                    'public-sector tenders',
                ],
            },
        ],
        'quote': None,
    },
    {
        'slug': 'yogher',
        'client': 'YogHer',
        'logo': 'images/yogher.png',
        'image': 'images/yogher_work.png',
        'sector': 'Digital wellness',
        'engagement': 'Live-class booking platform and wellness brand experience',
        'url': 'https://yogher.in/',
        'standfirst': (
            'Live online yoga built for Indian women — a product whose hardest constraint '
            'is not fitness, but scheduling around a family.'
        ),
        'facts': [
            ('Engagement', 'Live-class booking platform & brand experience'),
            ('Reach', 'India and 12+ countries'),
            ('Published scale', '5,000+ members · 25+ certified coaches · 50,000+ live classes'),
            ('Class window', '5 AM – 9 PM IST'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'YogHer runs live online yoga classes designed specifically for Indian women, '
                    'taught over video across a 5 AM to 9 PM IST window so that members in India '
                    'and a dozen other countries can find a slot that fits. Seven programmes cover '
                    'weight loss, hormonal balance, prenatal wellness, body toning, irregular '
                    'periods and perimenopause.',
                ],
            },
            {
                'heading': 'What makes it specific',
                'paras': [
                    'Generic fitness apps fail this audience twice over. They prescribe diets built '
                    'on foods nobody in the house is cooking, and they schedule as though the '
                    "member's day is her own.",
                    'The site is built to deliver on the opposite promise: diet plans based on '
                    'Indian home cooking, recorded sessions for a missed class, and 24/7 WhatsApp '
                    'access to a coach — WhatsApp because that is where this audience already is.',
                ],
            },
            {
                'heading': 'Commercial model',
                'bullets': [
                    'Trial — ₹1,199 for 30 days',
                    'Three-month plan — ₹2,399 for 90 days',
                    'Six-month plan — ₹3,599 for 180 days',
                ],
                'paras_after': [
                    'Pricing that descends steeply per day with commitment, which tells you '
                    'retention — not acquisition — is the metric the platform is built to serve.',
                ],
            },
        ],
        'quote': {
            'text': 'A diet built around your ghar ka khana, and timings that fit around family.',
            'cite': 'YogHer · site copy',
        },
    },
    {
        'slug': 'oswaal-books',
        'client': 'Oswaal Books',
        'logo': 'images/oswaal.png',
        'image': 'images/oswaal_work.png',
        'sector': 'Educational publishing',
        'engagement': 'AI automation that generates book content and images from a topic',
        'url': '',
        'standfirst': (
            'A publisher whose catalogue has to keep pace with every school board and entrance '
            'exam in the country — and an AI system that turns a topic into a book, text and '
            'images together.'
        ),
        'facts': [
            ('Engagement', 'AI book-generation automation'),
            ('Founded', '1984 · Agra, Uttar Pradesh'),
            ('Covers', 'CBSE, ICSE, ISC, IGCSE · JEE, NEET, CUET, CLAT, CAT, UPSC, SSC, Olympiads'),
            ('Published reach', '2.63 crore+ students · 48,126 schools & coachings'),
        ],
        'sections': [
            {
                'heading': 'The client',
                'paras': [
                    'Oswaal Books was founded in Agra in 1984 by Naresh Jain and is now led by CEO '
                    'Prashant Jain. It publishes question banks and study material for school '
                    'boards — CBSE, ICSE, ISC and IGCSE — and for entrance and competitive exams '
                    'from JEE and NEET to CUET, CLAT, CAT, UPSC, SSC and the Olympiads.',
                    'Its own site cites more than 2.63 crore students and aspirants, 4.79 lakh '
                    'teachers and educators, and adoption across 48,126 schools and coaching '
                    'institutes. Its CBSE and ICSE question banks were named Product of the Year '
                    '2022 in a Nielsen nationwide survey.',
                ],
            },
            {
                'heading': 'The problem',
                'paras': [
                    'Exam publishing runs on a calendar the publisher does not control. Every board '
                    'revision, every new exam pattern and every academic year means content across '
                    'a very large catalogue has to be written, illustrated and assembled again — '
                    'against a release date that does not move.',
                    'The bottleneck is not printing. It is producing the content in the first place.',
                ],
            },
            {
                'heading': 'What we built',
                'paras': [
                    'An AI automation that generates a book from a topic. Given the subject a book '
                    'should cover, it produces the written content and the images that go with it, '
                    'so a new title starts from complete book content rather than a blank page.',
                ],
            },
            {
                'heading': 'Why it fits a publisher at this scale',
                'paras': [
                    'A publisher covering this many boards and exams is, in practice, running a '
                    'content production line. At that scale the expensive step in a new title is '
                    'generating its content — and text and imagery are usually two separate '
                    'efforts. Producing both together, from a single topic, is where the time '
                    'comes back.',
                ],
            },
        ],
        'quote': None,
    },
]

CASE_STUDIES_BY_SLUG = {study['slug']: study for study in CASE_STUDIES}
