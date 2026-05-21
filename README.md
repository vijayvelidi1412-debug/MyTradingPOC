MyTradingPOC/
├── apps/
│   ├── users/                 # User management & authentication
│   │   ├── models.py         # CustomUser, UserProfile, CashCredit
│   │   ├── views.py          # Auth, user endpoints
│   │   ├── serializers.py    # REST API serializers
│   │   ├── admin.py          # Django admin interface
│   │   ├── signals.py        # Auto profile creation
│   │   └── permissions.py    # Custom permissions
│   │
│   ├── trading/              # Trading operations
│   │   ├── models.py         # Contract, Trade, Position, PriceHistory
│   │   ├── views.py          # Trade & position management
│   │   ├── serializers.py    # Trading serializers
│   │   ├── admin.py          # Trading admin
│   │   ├── apps.py           # App config
│   │   └── utils.py          # Trading utilities
│   │
│   ├── settlements/          # Weekly settlements & rollovers
│   │   ├── models.py         # Settlement, CreditNote, Rollover
│   │   ├── views.py          # Settlement endpoints
│   │   ├── serializers.py    # Settlement serializers
│   │   ├── admin.py          # Settlement admin
│   │   ├── apps.py           # App config
│   │   └── tasks.py          # Celery automation tasks
│   │
│   ├── admin_dashboard/      # Admin overview & analytics
│   │   └── views.py          # Dashboard endpoints
│   │
│   ├── audit/                # Audit logging & compliance
│   │   ├── models.py         # AuditLog, TransactionAudit
│   │   ├── views.py          # Audit endpoints
│   │   └── serializers.py    # Audit serializers
│   │
│   └── __init__.py
│
├── core/
│   ├── settings.py           # Django configuration
│   ├── urls.py               # API routing
│   ├── wsgi.py               # WSGI app
│   ├── asgi.py               # ASGI app
│   └── celery.py             # Celery task scheduler
│
├── manage.py                 # Django management
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
├── docker-compose.yml        # Docker orchestration
├── Dockerfile                # Container image
└── README.md                 # Documentation



**Technology Stack**
Component	Technology
Backend Framework	Django 4.2
REST API	Django REST Framework
Database	PostgreSQL 15
Cache/Queue	Redis 7
Task Scheduler	Celery + Celery Beat
Authentication	JWT (djangorestframework-simplejwt)
Admin Panel	Django Admin
Deployment	Docker & Docker Compose
