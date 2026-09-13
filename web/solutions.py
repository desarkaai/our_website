"""
Shared solution content for the homepage, the solutions page and the
solution detail pages.

Data contract
-------------
SOLUTIONS is a list of seven dicts, in display order. Each has:
    number, slug, title, description, detail, features (3),
    eyebrow, image, image_alt, headline, intro (2 paragraphs),
    outcomes (3 {title, text}), capabilities (6 {title, text}),
    process (4 {step, title, text}), related_case_studies (real slugs
    from web.case_studies), faqs (3 {q, a}).

FEATURES is the homepage carousel: one slide per solution, same order,
each {category, title, description, slug, image, alt}. Category, image and
alt are taken from the matching solution so the two never drift apart.

Keep every number, slug and title stable: URLs depend on them. Do not add
client names, metrics or claims that are not backed by a real project.
"""

SOLUTIONS = [
    {
        'number': '01',
        'slug': 'erp',
        'title': 'ERP Development',
        'description': 'One connected system for stock, purchasing, production and billing.',
        'detail': (
            'Bring inventory, purchasing, production and billing into one system built around '
            'the way your business actually runs. Replace scattered spreadsheets and registers '
            'with clear workflows, proper approvals and numbers your whole team can trust.'
        ),
        'features': [
            'Inventory lots & stock ledger',
            'Purchase orders & GST invoicing',
            'Approvals, roles & reports',
        ],
        'eyebrow': 'CONNECTED OPERATIONS',
        'image': 'images/connected-systems.webp',
        'image_alt': (
            'Brushed-aluminium frames and a ring joined by a ribbon of frosted glass, with a red '
            'sphere resting at the centre'
        ),
        'headline': 'Know where every lot, order and invoice stands, without calling anyone to ask.',
        'intro': [
            'Most growing businesses run on a mix of Excel sheets, paper registers, WhatsApp '
            'groups and an accounting package that only sees the final bill. Each part works on '
            'its own. Together they make simple questions hard: how much stock is really on hand, '
            'which order is stuck, which payment is still due.',
            'We build ERP systems around how your business actually moves goods and money. Every '
            'purchase, stock movement, production stage and invoice is recorded once, in one '
            'place, with the right people approving the steps that matter. Ready-made ERPs ask '
            'you to change how you work. A custom system starts from how you work today.',
        ],
        'outcomes': [
            {
                'title': 'Stock you can trust',
                'text': (
                    'Every inward, issue and sale is recorded as a movement, so the on-hand figure '
                    'can be traced back at any time rather than guessed at month end.'
                ),
            },
            {
                'title': 'Fewer gaps between teams',
                'text': (
                    'Purchase, production, dispatch and accounts work from the same records, so '
                    'details are not retyped from one sheet into the next.'
                ),
            },
            {
                'title': 'Answers without asking around',
                'text': (
                    'Owners and managers see pending orders, dues and stock positions on a '
                    'dashboard instead of waiting for someone to put a report together.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Inventory and lots',
                'text': (
                    'Stock tracked by lot, location and stage, including material that is out with '
                    'job workers or karigars and not yet returned.'
                ),
            },
            {
                'title': 'Purchasing and inward',
                'text': (
                    'Purchase orders, goods receipt, supplier masters and payments, linked so every '
                    'bill traces back to what actually arrived.'
                ),
            },
            {
                'title': 'Production and job work',
                'text': (
                    'Stages that match your floor, with labour and material booked when work is '
                    'delivered, which is when quantities and rates are actually known.'
                ),
            },
            {
                'title': 'Invoices and documents',
                'text': (
                    'GST invoices, packing lists and export documents from editable templates, with '
                    'invoice numbering that follows the financial year.'
                ),
            },
            {
                'title': 'Approvals and permissions',
                'text': (
                    'Role-based access, with reversals and sensitive edits sent to an approvals queue '
                    'instead of being changed quietly.'
                ),
            },
            {
                'title': 'Reports and dashboards',
                'text': (
                    'Stock, sales, dues and production reports your team can filter and export, '
                    'built on the same data everyone works from.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Map the operation',
                'text': (
                    'We sit with the people who handle stock, purchase and billing, and follow real '
                    'transactions from start to finish. The design comes from what we find, not a '
                    'generic list of modules.'
                ),
            },
            {
                'step': '02',
                'title': 'Design the flows',
                'text': (
                    'We agree screens, stages, approvals and documents with you before building, and '
                    'decide which module should go live first.'
                ),
            },
            {
                'step': '03',
                'title': 'Build and migrate',
                'text': (
                    'We build in stages you can review, and bring across masters and opening stock '
                    'from your existing sheets or old software.'
                ),
            },
            {
                'step': '04',
                'title': 'Check, switch over and support',
                'text': (
                    'We check the new figures against your existing records before switching over, '
                    'then help your team settle into daily use and stay on hand for changes.'
                ),
            },
        ],
        'related_case_studies': ['akbar-international', 'techmills'],
        'faqs': [
            {
                'q': 'Do we have to move every department at once?',
                'a': (
                    'No. Most businesses start with the area causing the most trouble, often '
                    'inventory or billing, and add modules once that is running well. The system is '
                    'planned so later modules connect to the same records.'
                ),
            },
            {
                'q': 'Can you bring across data from our old software or Excel sheets?',
                'a': (
                    'Yes. We import masters, opening stock and history where it is useful. On the '
                    'Akbar International ERP the old system’s source code had been lost, so its '
                    'pricing rules were worked out from the data it left behind and checked against '
                    'historical records.'
                ),
            },
            {
                'q': 'Will it replace our accounting software?',
                'a': (
                    'It does not have to. Many businesses keep their existing accounting software '
                    'for books and filing, and use the ERP for day-to-day operations. We agree early '
                    'on where that boundary sits and how figures move between the two.'
                ),
            },
        ],
    },
    {
        'number': '02',
        'slug': 'crm',
        'title': 'CRM Development',
        'description': 'A clear record of every enquiry, customer and follow-up.',
        'detail': (
            'Give your sales and service teams one shared view of every customer. Record enquiries '
            'from every channel, move them through the stages your business actually uses and make '
            'sure no follow-up depends on someone’s memory.'
        ),
        'features': [
            'Enquiries & sales pipeline',
            'Follow-ups & reminders',
            'Customer & service history',
        ],
        'eyebrow': 'CUSTOMER RELATIONSHIPS',
        'image': 'images/crm-relationships.webp',
        'image_alt': (
            'Two interlocking brushed-aluminium rings with a red sphere at their base and a path of '
            'frosted-glass discs leading to it'
        ),
        'headline': (
            'See every enquiry, conversation and follow-up in one place, from the first call to '
            'after-sales service.'
        ),
        'intro': [
            'In many businesses, customer information lives in a salesperson’s phone, a WhatsApp '
            'chat and a register nobody else can read. When someone is on leave or moves on, the '
            'relationship goes with them, and follow-ups slip without anyone noticing.',
            'We build CRMs shaped around the way you sell and serve. If a sale closes in a single '
            'call, the system stays simple. If a job runs through site visits, quotations, '
            'installation and years of service, the CRM follows each of those stages rather than '
            'forcing them into generic deals.',
        ],
        'outcomes': [
            {
                'title': 'Fewer missed follow-ups',
                'text': (
                    'Every enquiry has an owner and a dated next step, so leads are not lost between '
                    'a phone call and a busy week.'
                ),
            },
            {
                'title': 'Continuity across the team',
                'text': (
                    'Customer history stays with the business, so anyone picking up an account can '
                    'see what was discussed, quoted and promised.'
                ),
            },
            {
                'title': 'A pipeline you can read',
                'text': (
                    'Owners can see how many enquiries sit at each stage, what is expected to close '
                    'and where deals tend to stall.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Enquiry capture',
                'text': (
                    'Leads from website forms, calls, WhatsApp, walk-ins and referrals logged in one '
                    'place, with the source noted against each.'
                ),
            },
            {
                'title': 'Pipeline stages',
                'text': (
                    'Stages that match your real sales process, from first enquiry and site visit to '
                    'quotation, order and handover.'
                ),
            },
            {
                'title': 'Follow-ups and reminders',
                'text': (
                    'Follow-ups assigned to a named person, with reminders and a clear list of what '
                    'is due today.'
                ),
            },
            {
                'title': 'Quotations',
                'text': (
                    'Quotations prepared from your product or service list, with each revision kept '
                    'against the customer record.'
                ),
            },
            {
                'title': 'Service and after-sales',
                'text': (
                    'Installations, service calls and AMC renewals tracked after the sale, so the '
                    'relationship does not end at the invoice.'
                ),
            },
            {
                'title': 'Team views and reports',
                'text': (
                    'Separate access for sales, service and management, with reports on enquiries, '
                    'conversions by source and pending work.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Follow a real sale',
                'text': (
                    'We trace how an enquiry becomes an order today, who touches it along the way and '
                    'where it tends to stall.'
                ),
            },
            {
                'step': '02',
                'title': 'Define the stages',
                'text': (
                    'Together we settle the pipeline stages, fields and reminders your team will '
                    'actually keep up to date, and leave out the rest.'
                ),
            },
            {
                'step': '03',
                'title': 'Build and import',
                'text': (
                    'We build the CRM in stages you can review, and import existing customers and '
                    'open enquiries from your sheets and contact lists.'
                ),
            },
            {
                'step': '04',
                'title': 'Adopt and refine',
                'text': (
                    'After launch we watch how the team uses it and adjust stages and screens, '
                    'because a CRM only helps if people keep using it.'
                ),
            },
        ],
        'related_case_studies': ['securetech-av'],
        'faqs': [
            {
                'q': 'Why not use a ready-made CRM?',
                'a': (
                    'For many businesses a standard CRM is enough, and we will say so. A custom CRM '
                    'makes sense when your work runs through stages that generic deal pipelines do '
                    'not model, such as site surveys, installation and ongoing service, or when it '
                    'needs to work closely with your other systems.'
                ),
            },
            {
                'q': 'Will our sales team actually use it?',
                'a': (
                    'Adoption is mostly about keeping it simple. We keep the number of fields small, '
                    'make the next follow-up the first thing people see and make sure it works '
                    'comfortably on a phone.'
                ),
            },
            {
                'q': 'Can it connect to our website and billing?',
                'a': (
                    'Usually. Website enquiry forms can feed the CRM directly. Connecting to billing '
                    'or an ERP depends on what that system allows, and we check this during planning.'
                ),
            },
        ],
    },
    {
        'number': '03',
        'slug': 'ai-automation',
        'title': 'AI & Automation',
        'description': 'Take repetitive work off your team, with people still reviewing what matters.',
        'detail': (
            'Turn slow, repetitive tasks into dependable workflows. We connect the tools you already '
            'use, automate the routine steps and build AI systems that draft, extract and generate, '
            'with a person reviewing the output wherever the stakes are high.'
        ),
        'features': [
            'Workflow automation',
            'AI content & document processing',
            'Human review built in',
        ],
        'eyebrow': 'INTELLIGENT WORKFLOWS',
        'image': 'images/intelligent-workflows.webp',
        'image_alt': (
            'A red ribbon flowing through ivory stone arches and a frosted-glass arch, beside the sea'
        ),
        'headline': 'Hand the repetitive work to software, and keep people where judgement matters.',
        'intro': [
            'Every business has work that follows the same pattern each day: copying details from '
            'emails into sheets, preparing the same kinds of documents, sending the same reminders, '
            'drafting content from a brief. It is necessary work, but it takes time from people who '
            'could be doing something only they can do.',
            'We start with one specific task and a clear idea of what good output looks like, then '
            'decide which parts suit simple automation and which benefit from AI. For Oswaal Books, '
            'that meant a system that takes a topic and produces book content and matching images '
            'together. Wherever a mistake would be costly, the workflow keeps a person reviewing '
            'before anything goes out.',
        ],
        'outcomes': [
            {
                'title': 'Time back for your team',
                'text': (
                    'Routine steps run on their own, so people spend their hours on decisions, '
                    'customers and quality rather than retyping.'
                ),
            },
            {
                'title': 'Consistent output',
                'text': (
                    'The same task is done the same way every time, following your formats and rules, '
                    'with a record of what was produced.'
                ),
            },
            {
                'title': 'Room for busy seasons',
                'text': (
                    'When volume rises, more of the extra load is handled by the workflow rather than '
                    'by longer hours for the same people.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Content generation',
                'text': (
                    'Systems that turn a topic or brief into structured written content and matching '
                    'images, ready for editing rather than starting from a blank page.'
                ),
            },
            {
                'title': 'Document processing',
                'text': (
                    'Reading invoices, forms and PDFs to pull out the details you need and place them '
                    'in your sheets or systems for checking.'
                ),
            },
            {
                'title': 'Workflow automation',
                'text': (
                    'Connecting the tools you already use, so a new order, form or approval triggers '
                    'the next step, such as an email, a record update or a WhatsApp notification.'
                ),
            },
            {
                'title': 'Assistants and search',
                'text': (
                    'Assistants that answer questions from your own documents, product information '
                    'and policies, and show the source they relied on.'
                ),
            },
            {
                'title': 'Review and approval steps',
                'text': (
                    'Checkpoints where a person approves, edits or rejects AI output before it is '
                    'published, sent or saved.'
                ),
            },
            {
                'title': 'Logs and reporting',
                'text': (
                    'A record of what ran, what was produced and what was corrected, so the workflow '
                    'can be checked and improved over time.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Pick the right task',
                'text': (
                    'We look for work that is frequent, well defined and time-consuming, and agree '
                    'what a good result looks like before any building starts.'
                ),
            },
            {
                'step': '02',
                'title': 'Try it on real examples',
                'text': (
                    'We build a small working version and test it on your actual documents or topics, '
                    'so quality is judged on real output rather than a demo.'
                ),
            },
            {
                'step': '03',
                'title': 'Build the workflow',
                'text': (
                    'We add the connections, review steps, formats and error handling your team needs '
                    'to rely on it every day.'
                ),
            },
            {
                'step': '04',
                'title': 'Monitor and improve',
                'text': (
                    'After launch we check output quality, adjust prompts and rules as your needs '
                    'change and keep an eye on running costs.'
                ),
            },
        ],
        'related_case_studies': ['oswaal-books'],
        'faqs': [
            {
                'q': 'Will the AI make mistakes?',
                'a': (
                    'It can. AI output is not always right, which is why we design workflows with '
                    'checks and, where the result matters, a person reviewing it before it is used. '
                    'The aim is to remove the repetitive effort, not the judgement.'
                ),
            },
            {
                'q': 'What kind of work is a good fit?',
                'a': (
                    'Tasks that happen often, follow a recognisable pattern and have a clear idea of '
                    'a good result: drafting from a brief, pulling details out of documents, sorting '
                    'enquiries or producing first versions of content. Work that needs fresh '
                    'judgement every time is usually better left with people.'
                ),
            },
            {
                'q': 'What happens to our data?',
                'a': (
                    'We discuss this before building. We look at what data the workflow really needs, '
                    'which AI services it will pass through and what their terms allow, and keep '
                    'sensitive information out of the process where it is not required.'
                ),
            },
        ],
    },
    {
        'number': '04',
        'slug': 'custom-software',
        'title': 'Custom Software',
        'description': 'Portals, platforms and internal tools built around the way you work.',
        'detail': (
            'When no ready-made product fits, we build the platform, portal or internal tool your '
            'business actually needs. We take it from understanding the problem through interface '
            'design, development and launch, on a foundation that is easy to maintain and extend.'
        ),
        'features': [
            'Web platforms & portals',
            'Internal tools & dashboards',
            'Integrations & data migration',
        ],
        'eyebrow': 'TAILORED SOFTWARE',
        'image': 'images/custom-software.webp',
        'image_alt': (
            'Frosted-glass and brushed-aluminium blocks arranged like an architectural model, with '
            'one red block slotted into place'
        ),
        'headline': 'Software built for the problem you actually have, not the nearest product on the market.',
        'intro': [
            'Some work does not fit any product you can subscribe to. A faulty part that has to be '
            'tracked out to a distributor and back. A class timetable planned around members’ '
            'family routines. An old desktop program nobody can update because its source code is '
            'gone. Businesses end up bending their processes around tools built for someone else.',
            'We build software around those specifics. That might be a customer or dealer portal, a '
            'booking platform, an internal tool that replaces a tangle of sheets, or a system that '
            'takes over from software you have outgrown. We keep the first version focused, so it '
            'is useful early and can grow in the directions your business does.',
        ],
        'outcomes': [
            {
                'title': 'A tool that fits the work',
                'text': (
                    'Screens, rules and terms match how your business works, so people spend less '
                    'time working around the software.'
                ),
            },
            {
                'title': 'A way off what you have outgrown',
                'text': (
                    'Ageing software and fragile spreadsheets can be replaced step by step, with your '
                    'existing data brought across.'
                ),
            },
            {
                'title': 'Room to grow',
                'text': (
                    'Because the foundation is planned for change, new features and integrations can '
                    'be added later without starting again.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Web platforms and portals',
                'text': (
                    'Customer, dealer and vendor portals with secure logins, where people can place '
                    'orders, track requests and download documents.'
                ),
            },
            {
                'title': 'Booking and scheduling',
                'text': (
                    'Systems for booking classes, appointments or services, with plans, availability '
                    'and reminders handled in one place.'
                ),
            },
            {
                'title': 'Tracking and workflow tools',
                'text': (
                    'Internal tools that follow an item or request through every stage, such as a '
                    'hardware replacement sent out to a distributor and back.'
                ),
            },
            {
                'title': 'Integrations',
                'text': (
                    'Connections to payment gateways, SMS, email, WhatsApp messaging and the other '
                    'systems you already use, so data is not entered twice.'
                ),
            },
            {
                'title': 'Legacy replacement and migration',
                'text': (
                    'Moving off old software or spreadsheets, including working out business rules '
                    'from existing records when the original logic was never written down.'
                ),
            },
            {
                'title': 'Dashboards and reporting',
                'text': (
                    'Views that bring figures from across the system into what owners and managers '
                    'need to check each day.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Discovery',
                'text': (
                    'We learn how the work happens today, who will use the software and what would '
                    'make it worthwhile, then turn that into a written scope.'
                ),
            },
            {
                'step': '02',
                'title': 'Interface design',
                'text': (
                    'We design the key screens and flows first, so you can see and question how the '
                    'software will work before development begins.'
                ),
            },
            {
                'step': '03',
                'title': 'Development in stages',
                'text': (
                    'We build in short stages with regular reviews, putting working software in front '
                    'of you early rather than at the very end.'
                ),
            },
            {
                'step': '04',
                'title': 'Launch and grow',
                'text': (
                    'We launch, help your team settle in and then extend the software as priorities '
                    'become clearer from real use.'
                ),
            },
        ],
        'related_case_studies': ['akbar-international', 'techmills', 'yogher'],
        'faqs': [
            {
                'q': 'How do we know what to build first?',
                'a': (
                    'Discovery answers that. We identify the smallest version that solves a real '
                    'problem for your team, launch it, and plan further work from what people '
                    'actually use.'
                ),
            },
            {
                'q': 'Can you replace software we already use?',
                'a': (
                    'Yes. We start by understanding what the current system does, including rules '
                    'that may never have been written down, and bring your data across. The Akbar '
                    'International ERP replaced a legacy desktop application whose source code had '
                    'been lost.'
                ),
            },
            {
                'q': 'How much does custom software cost?',
                'a': (
                    'It depends on scope, which is why we begin with discovery. Once the first '
                    'version is defined, we share a clear estimate and a phased plan, so you can '
                    'decide what to build now and what can wait.'
                ),
            },
        ],
    },
    {
        'number': '05',
        'slug': 'web-commerce',
        'title': 'Websites & E-commerce',
        'description': 'Websites, catalogues and online stores that turn interest into enquiries and orders.',
        'detail': (
            'Create a fast, clear home for your brand online. From a focused company website or '
            'product catalogue to a complete online store, we bring content, product discovery and '
            'ordering together in a way that suits how your customers buy.'
        ),
        'features': [
            'Brand websites & catalogues',
            'Online stores & payments',
            'Content you can update',
        ],
        'eyebrow': 'DIGITAL EXPERIENCES',
        'image': 'images/digital-experiences.webp',
        'image_alt': (
            'A dark glass panel, a frosted-glass slab and a red disc with a steel sphere on a stone '
            'plinth in soft sunlight'
        ),
        'headline': 'A website that explains what you do, earns trust quickly and makes the next step obvious.',
        'intro': [
            'Your website is often the first place a customer, dealer or tender committee looks '
            'before getting in touch. If it is slow, dated or vague about what you sell, they move '
            'on quietly, and you never hear about the enquiry you lost.',
            'We design and build websites around how your customers actually buy. An installer '
            'choosing cables needs specifications and an enquiry form, not a cart. Someone buying '
            'jewellery online needs guides and a clear view of pricing before checkout. A wellness '
            'brand needs plans and a simple way to join a class. The structure follows the sale.',
        ],
        'outcomes': [
            {
                'title': 'Clearer first impressions',
                'text': (
                    'Visitors understand what you offer and who it is for from the first screen, on a '
                    'phone as well as a desktop.'
                ),
            },
            {
                'title': 'Better-informed enquiries',
                'text': (
                    'Product pages, specifications and guides answer common questions up front, so '
                    'the people who get in touch already know what they are asking for.'
                ),
            },
            {
                'title': 'A site your team can run',
                'text': (
                    'Products, prices, pages and banners can be updated by your own team without '
                    'waiting on a developer for every change.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Brand and company websites',
                'text': (
                    'Focused sites that set out who you are, what you make and why buyers should '
                    'trust you, with provenance and credentials given proper space.'
                ),
            },
            {
                'title': 'Product catalogues',
                'text': (
                    'Catalogues with a separate route for each product family, clear specifications '
                    'and enquiry forms suited to B2B buying.'
                ),
            },
            {
                'title': 'Online stores',
                'text': (
                    'Category browsing, product pages, cart, checkout, customer accounts and order '
                    'status, with an admin area for managing the catalogue.'
                ),
            },
            {
                'title': 'Buying guides and tools',
                'text': (
                    'Guides and calculators that help a first-time buyer decide, such as a live gold '
                    'rate calculator beside a jewellery range.'
                ),
            },
            {
                'title': 'Plans and bookings',
                'text': (
                    'Plan selection, sign-up and booking flows for services and classes, connected to '
                    'the way you deliver them.'
                ),
            },
            {
                'title': 'Content management',
                'text': (
                    'An admin area for updating pages and products, on a site with fast pages, a '
                    'clean structure and the on-page basics search engines look for.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Understand the buyer',
                'text': (
                    'We look at who visits, what they need to know before they buy or enquire, and '
                    'how others in your market present themselves.'
                ),
            },
            {
                'step': '02',
                'title': 'Structure and design',
                'text': (
                    'We plan the pages, product structure and content first, then design the look of '
                    'the site to suit your brand.'
                ),
            },
            {
                'step': '03',
                'title': 'Build and load content',
                'text': (
                    'We build the site, load products and content, and test it on phones, tablets and '
                    'desktops before it goes live.'
                ),
            },
            {
                'step': '04',
                'title': 'Launch and look after',
                'text': (
                    'We handle the launch, show your team how to make updates and stay available for '
                    'changes as your range and campaigns evolve.'
                ),
            },
        ],
        'related_case_studies': ['amaarah', 'yogher', 'netmas', 'ampluxe'],
        'faqs': [
            {
                'q': 'Do we need an online store, or just a website?',
                'a': (
                    'It depends on how your customers buy. Many B2B products are sold through '
                    'quotations, so a catalogue with enquiry forms works better than a cart. Retail '
                    'products with fixed prices usually suit a full store. We help you choose before '
                    'anything is built.'
                ),
            },
            {
                'q': 'Can we update products and content ourselves?',
                'a': (
                    'Yes. We include an admin area for products, prices, pages and images, and walk '
                    'your team through it at launch.'
                ),
            },
            {
                'q': 'Can you redesign our existing website?',
                'a': (
                    'Yes. We review what your current site does well, keep the content and page '
                    'addresses that still bring in visitors, and rebuild the rest so nothing useful '
                    'is lost in the move.'
                ),
            },
        ],
    },
    {
        'number': '06',
        'slug': 'mobile-apps',
        'title': 'Mobile Apps',
        'description': 'Apps for your customers and field teams, connected to the systems you already run.',
        'detail': (
            'Put your service in your customers’ hands, or give your field team what they need on '
            'the move. We design clear journeys and build apps that connect to your existing '
            'systems, from the first prototype through release and ongoing improvements.'
        ),
        'features': [
            'Android & iOS apps',
            'Connected to your systems',
            'Notifications & offline sync',
        ],
        'eyebrow': 'MOBILE EXPERIENCES',
        'image': 'images/mobile-apps.webp',
        'image_alt': (
            'A slim frosted-glass slab standing on a stone plinth, with a red disc behind it and a '
            'small steel sphere'
        ),
        'headline': 'An app that makes one everyday task quicker for your customers or your team.',
        'intro': [
            'An app earns its place on a phone by doing one job well. For customers that might be '
            'reordering, booking or tracking a request. For your own staff it might be taking '
            'orders at a dealer’s counter, logging a site visit with photos or checking stock from '
            'the warehouse floor.',
            'We start from that job and the conditions around it, including patchy mobile networks, '
            'shared devices and people who are busy with something else. Then we design the journey, '
            'build the app and connect it to the systems that already hold your data, so the app and '
            'the office work from the same records.',
        ],
        'outcomes': [
            {
                'title': 'Work recorded where it happens',
                'text': (
                    'Orders, visits and photos are recorded on the spot instead of being noted down '
                    'and entered later.'
                ),
            },
            {
                'title': 'Customers who can help themselves',
                'text': (
                    'Customers can book, reorder or check a status on their own, which means fewer '
                    'routine calls for your team to answer.'
                ),
            },
            {
                'title': 'One set of records',
                'text': (
                    'What is entered in the app reaches your ERP, CRM or admin panel, so the office '
                    'sees the same picture as the field.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Customer apps',
                'text': (
                    'Apps for booking, reordering and order tracking, designed so a first-time user '
                    'can finish the main task without help.'
                ),
            },
            {
                'title': 'Field and sales team apps',
                'text': (
                    'Order taking, site visits with photos and location, attendance and daily reports '
                    'for staff who work away from the office.'
                ),
            },
            {
                'title': 'Offline sync',
                'text': (
                    'Apps that keep working when the network drops and sync their records once a '
                    'connection returns.'
                ),
            },
            {
                'title': 'Notifications',
                'text': (
                    'Push notifications for order updates, reminders and approvals, sent when they are '
                    'useful rather than all the time.'
                ),
            },
            {
                'title': 'Backend and admin panel',
                'text': (
                    'The server, APIs and web admin panel behind the app, or a connection to the '
                    'system you already use.'
                ),
            },
            {
                'title': 'Release and updates',
                'text': (
                    'Store listings, Play Store and App Store submission, and regular updates after '
                    'the first release.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Define the core job',
                'text': (
                    'We identify who the app is for, the one or two tasks it must do well and the '
                    'conditions it will be used in.'
                ),
            },
            {
                'step': '02',
                'title': 'Prototype the journey',
                'text': (
                    'We design the key screens as a clickable prototype and try it with people who '
                    'will use the app before development starts.'
                ),
            },
            {
                'step': '03',
                'title': 'Build and test on devices',
                'text': (
                    'We build the app and its backend together and test on real phones, including the '
                    'budget Android handsets many field teams carry.'
                ),
            },
            {
                'step': '04',
                'title': 'Release and improve',
                'text': (
                    'We handle store submission, watch for issues after release and plan updates '
                    'around how people actually use the app.'
                ),
            },
        ],
        'related_case_studies': [],
        'faqs': [
            {
                'q': 'Do we need an app, or would a mobile website do?',
                'a': (
                    'Often a well-built mobile website is enough, and we will tell you if that is the '
                    'case. An app makes more sense when people use it regularly, need notifications '
                    'or offline access, or rely on the camera or location.'
                ),
            },
            {
                'q': 'Android, iOS or both?',
                'a': (
                    'It depends on who will use it. An app for your own staff may only need Android, '
                    'while customer apps usually need both. We plan for this at the start, so adding '
                    'a second platform later does not mean starting again.'
                ),
            },
            {
                'q': 'Can the app connect to our existing software?',
                'a': (
                    'Usually. If your ERP, CRM or website can share data safely, the app can read and '
                    'update the same records. We check what your current system allows during '
                    'planning.'
                ),
            },
        ],
    },
    {
        'number': '07',
        'slug': 'iot',
        'title': 'Embedded Systems & IoT',
        'description': 'Sensor and device data turned into dashboards and alerts people can act on.',
        'detail': (
            'Bring devices, sensors and software together. We turn readings from machines, rooms and '
            'sites into practical dashboards, alerts and controls, with careful attention to device '
            'communication, reliability and the people using the system.'
        ),
        'features': [
            'Device & sensor integration',
            'Monitoring dashboards & alerts',
            'Firmware & connectivity',
        ],
        'eyebrow': 'CONNECTED DEVICES',
        'image': 'images/embedded-iot.webp',
        'image_alt': (
            'An aluminium plate with a grid of small pins, thin rods rising to a suspended red sphere '
            'and a glass dome over one node'
        ),
        'headline': 'Know what is happening at your machines and sites without having to be there.',
        'intro': [
            'Many problems are only noticed when someone happens to walk past: a cold room drifting '
            'out of temperature, a water tank running low, a generator left on overnight, a machine '
            'that has quietly stopped. The information exists at the device. It just never reaches '
            'the people who could act on it.',
            'We connect sensors and equipment to software that records their readings, shows them '
            'clearly and raises an alert when something needs attention. We start with a small '
            'pilot on a few devices, so the value is proven on your own site before it is rolled out '
            'more widely.',
        ],
        'outcomes': [
            {
                'title': 'Problems noticed earlier',
                'text': (
                    'Alerts reach the right person when a reading crosses a limit, instead of the '
                    'issue being found on the next round.'
                ),
            },
            {
                'title': 'Records kept automatically',
                'text': (
                    'Readings are logged with the date and time, replacing handwritten logs and giving '
                    'you a history to look back on.'
                ),
            },
            {
                'title': 'Oversight across locations',
                'text': (
                    'Owners and supervisors can check several sites or machines from one dashboard, on '
                    'a laptop or a phone.'
                ),
            },
        ],
        'capabilities': [
            {
                'title': 'Sensor and device integration',
                'text': (
                    'Reading temperature, humidity, power, levels or machine status from sensors and '
                    'equipment, including devices you already own where they allow it.'
                ),
            },
            {
                'title': 'Firmware',
                'text': (
                    'Code for small microcontroller-based devices that take readings, cope with an '
                    'unreliable network and report in at sensible intervals.'
                ),
            },
            {
                'title': 'Connectivity',
                'text': (
                    'Getting data from the device to the server over Wi-Fi, Ethernet or a mobile '
                    'network, with readings held on the device while the connection is down.'
                ),
            },
            {
                'title': 'Monitoring dashboards',
                'text': (
                    'Live and historical views of sensor data, organised by site, machine or room, '
                    'that work on a phone as well as a desktop.'
                ),
            },
            {
                'title': 'Alerts and notifications',
                'text': (
                    'Threshold and device-offline alerts by email, SMS or WhatsApp, sent to the people '
                    'responsible and escalated if nobody responds.'
                ),
            },
            {
                'title': 'Remote control and reports',
                'text': (
                    'Switching equipment or changing settings from the dashboard where it is safe to '
                    'do so, with reports for audits and maintenance.'
                ),
            },
        ],
        'process': [
            {
                'step': '01',
                'title': 'Survey the site',
                'text': (
                    'We look at the equipment, what needs to be measured, where power and network are '
                    'available and who should respond to what.'
                ),
            },
            {
                'step': '02',
                'title': 'Pilot on a few devices',
                'text': (
                    'We connect a small number of sensors or machines first, so readings, alerts and '
                    'connectivity are tested in your real conditions.'
                ),
            },
            {
                'step': '03',
                'title': 'Build the platform',
                'text': (
                    'We build the dashboards, alert rules, user roles and reports around what the '
                    'pilot showed you actually need.'
                ),
            },
            {
                'step': '04',
                'title': 'Roll out and maintain',
                'text': (
                    'We extend to more devices or locations in stages, and keep watching device '
                    'health, connectivity and data quality after rollout.'
                ),
            },
        ],
        'related_case_studies': [],
        'faqs': [
            {
                'q': 'Can you work with equipment we already have?',
                'a': (
                    'Often, yes. Many machines and controllers can already share their readings, and '
                    'we start there. Where they cannot, we look at adding sensors or a small '
                    'controller alongside the existing equipment.'
                ),
            },
            {
                'q': 'What happens when the internet goes down?',
                'a': (
                    'Devices can store readings locally and send them once the connection returns. '
                    'The system can also alert you when a device stops reporting, so a gap in the data '
                    'is noticed rather than hidden.'
                ),
            },
            {
                'q': 'Do we need to cover every machine at once?',
                'a': (
                    'No. We suggest starting with a pilot on the equipment where a problem is most '
                    'costly, then expanding once the readings and alerts have proved useful.'
                ),
            },
        ],
    },
]

SOLUTIONS_BY_SLUG = {solution['slug']: solution for solution in SOLUTIONS}


def _slide(slug, title, description):
    """Build a carousel slide whose category, image and alt match its solution."""
    solution = SOLUTIONS_BY_SLUG[slug]
    return {
        'category': solution['eyebrow'],
        'title': title,
        'description': description,
        'slug': slug,
        'image': solution['image'],
        'alt': solution['image_alt'],
    }


FEATURES = [
    _slide(
        'erp',
        'Everything working. Together.',
        'ERP systems that bring stock, purchasing, production and billing into one clear view.',
    ),
    _slide(
        'crm',
        'Every customer. Remembered.',
        'A CRM that keeps enquiries, follow-ups and customer history in one place.',
    ),
    _slide(
        'ai-automation',
        'Make space for better work.',
        'Practical AI and automation that take the repetition out of your day.',
    ),
    _slide(
        'custom-software',
        'Shaped around your work.',
        'Portals, platforms and internal tools for problems no ready-made product solves.',
    ),
    _slide(
        'web-commerce',
        'Good ideas. Beautifully built.',
        'Websites, catalogues and online stores with your customers at the centre.',
    ),
    _slide(
        'mobile-apps',
        'Simple things. Close at hand.',
        'Android and iOS apps for your customers and field teams, connected to your systems.',
    ),
    _slide(
        'iot',
        'Quiet signals. Clear answers.',
        'Sensors and devices connected to dashboards and alerts your team can act on.',
    ),
]
