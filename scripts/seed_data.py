"""
Populate the database with sample data.
Run from the project root: python scripts/seed_data.py
"""
import os
import sys

# Allow running from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indataai_clone.settings')

import django
django.setup()

from website.models import Testimonial, Service, FAQ, Event

# --- Testimonials ---
testimonials = [
    {'name': 'Rohit Shetty',     'designation': 'Real Estate Developer', 'message': "InDataAI provided us with an exceptional real estate software solution. Our team's productivity increased, and customer follow-ups became fully automated.", 'rating': 5},
    {'name': 'Ananya Deshmukh',  'designation': 'Business Owner',        'message': "The InDataAI team delivered a custom web application exactly as we required. Support and service are excellent—highly reliable and professional.", 'rating': 5},
    {'name': 'Mahesh Patil',     'designation': 'Logistics Company',     'message': "We implemented InDataAI's logistics software, and it has streamlined our daily operations. User-friendly, accurate, and great customer support!", 'rating': 5},
    {'name': 'Priya Kulkarni',   'designation': 'E-Commerce Owner',      'message': "Excellent work on our e-commerce platform. The team was professional, responsive, and delivered beyond our expectations. Highly recommended!", 'rating': 5},
    {'name': 'Dr. Suresh Nair',  'designation': 'Hospital Administrator','message': "InDataAI built our hospital management system with great attention to detail. The system is robust, secure, and easy to use for our staff.", 'rating': 5},
]
for t in testimonials:
    Testimonial.objects.get_or_create(name=t['name'], defaults=t)
print(f"✅ {len(testimonials)} testimonials seeded")

# --- Services ---
services_data = [
    {'title': 'Web Development',    'description': 'Modern, secure and fully responsive web applications for your business.', 'icon_class': 'fas fa-laptop-code', 'order': 1},
    {'title': 'App Development',    'description': 'Android & iOS apps with high performance and cross-platform support.',    'icon_class': 'fas fa-mobile-alt',  'order': 2},
    {'title': 'Digital Marketing',  'description': 'Boost your brand presence with SEO, social media & paid campaigns.',      'icon_class': 'fas fa-bullhorn',    'order': 3},
    {'title': 'AI & Machine Learning','description': 'Intelligent automation & predictive analytics tailored to your needs.', 'icon_class': 'fas fa-brain',       'order': 4},
    {'title': 'Real Estate Software','description': 'End-to-end real-estate CRM with leads, sales, billing & automation.',   'icon_class': 'fas fa-building',    'order': 5},
    {'title': 'HRMS & Custom ERP',  'description': 'Complete HR, payroll, attendance & customized business ERP solutions.',  'icon_class': 'fas fa-users-cog',   'order': 6},
]
for s in services_data:
    Service.objects.get_or_create(title=s['title'], defaults=s)
print(f"✅ {len(services_data)} services seeded")

# --- FAQs ---
faqs_data = [
    {'question': 'How Do You Manage Consulting Effectively?',            'answer': 'Our team works closely with you to understand your unique challenges and deliver tailored solutions through objective insights and streamlined processes.', 'order': 1},
    {'question': 'What Are The Benefits Of Business Consulting Services?','answer': 'You gain access to specialized knowledge without the overhead of full-time hires, enabling faster decision-making and better outcomes.',              'order': 2},
    {'question': 'How Long Does It Take To Build A Custom Software?',    'answer': 'A simple web application may take 4–8 weeks; a complex enterprise solution 3–6 months. We provide a detailed timeline after requirements gathering.',    'order': 3},
    {'question': 'Do You Provide Post-Launch Support?',                  'answer': 'Yes — bug fixes, updates, performance optimization, and feature enhancements are all covered after your product goes live.',                               'order': 4},
    {'question': 'What Technologies Do You Work With?',                  'answer': 'Python/Django, React, Node.js, Flutter, React Native, MySQL, PostgreSQL, AWS, and more — chosen based on your project requirements.',                       'order': 5},
    {'question': 'How Do You Ensure Data Security?',                     'answer': 'We use encryption, secure authentication, regular security audits, and comply with data protection regulations. Your data security is our top priority.',   'order': 6},
]
for f in faqs_data:
    FAQ.objects.get_or_create(question=f['question'], defaults=f)
print(f"✅ {len(faqs_data)} FAQs seeded")

# --- Events ---
events_data = [
    {'title': 'Annual Tech Meetup',      'date': '2026-11-15', 'time': '09:00 AM', 'location': 'Stellar Mall, Hubli', 'description': 'Our yearly gathering showcasing innovation and achievements.'},
    {'title': 'Product Launch Event',    'date': '2026-10-28', 'time': '10:00 AM', 'location': 'Online',              'description': 'Launching our latest technology and industry solutions.'},
    {'title': 'Client Networking Event', 'date': '2026-09-10', 'time': '05:00 PM', 'location': 'Hubli, India',        'description': 'Strengthening partnerships and showcasing client success stories.'},
]
for e in events_data:
    Event.objects.get_or_create(title=e['title'], defaults=e)
print(f"✅ {len(events_data)} events seeded")

print("\n🎉 Database seeded! Run the server: python manage.py runserver")
