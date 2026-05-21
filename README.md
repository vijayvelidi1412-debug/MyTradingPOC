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


Key Workflows
Trade Placement Workflow
User places trade (Mon-Fri, 9-4 PM)
System validates trading hours
Trade created with open status
Position updated/created
User P&L updated in real-time
Settlement Workflow
Saturday 10 PM: Settlement task triggers
Get all user positions for the week
Close positions at Friday EOD price
Calculate P&L
Update user balance
Generate credit note
Create cash credit entry
Audit log recorded
Rollover Workflow
Before Settlement: User requests rollover
Admin approves via dashboard
Sunday midnight: Processing task runs
New positions created with Friday EOD price
Monday: Positions active in new week


All Features Complete
✨ Admin Controls

Create users only
Verify KYC
View all transactions
Approve/reject settlements
Approve/reject rollovers
✨ User Features

Place trades Mon-Fri
View open positions
Request rollovers
Track cash credits
View trading history
✨ Automated Processes

Weekly settlements
Position rollovers
Price updates
Credit note generation

