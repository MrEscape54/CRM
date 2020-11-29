from django.utils.translation import ugettext_lazy as _

ACC_INDUSTRY = (
    ("ADVERTISING", "Advertising"),
    ("AGRICULTURE", "Agriculture"),
    ("APPAREL & ACCESSORIES", "Apparel & Accesories"),
    ("AUTOMOTIVE", "Automotive"),
    ("BANKING", "Banking"),
    ("BIOTECHNOLOGY", "Biotechnology"),
    ("BUILDING MATERIALS & EQUIPMENT", "Building, Material & Equipment"),
    ("CHEMICAL", "Chemical"),
    ("EDUCATION", "Education"),
    ("ELECTRONICS", "Electronics"),
    ("UTILITIES", "Utilities"),
    ("OIL & GAS", "Oil & Gas"),
    ("ENTERTAINMENT & LEISURE", "Entertainment & Leisure"),
    ("FINANCE", "Finance"),
    ("FOOD & BEVERAGE", "Food & Beverage"),
    ("GROCERY", "Grocery"),
    ("HEALTHCARE", "Healthcare"),
    ("INSURANCE", "Insurance"),
    ("LEGAL", "Legal"),
    ("MANUFACTURING", "Manufacturing"),
    ("PUBLISHING", "Publishing"),
    ("REAL ESTATE", "Real State"),
    ("SERVICE", "Service"),
    ("SOFTWARE", "Software"),
    ("SPORTS", "Sports"),
    ("TECHNOLOGY", "Technology"),
    ("TELECOMMUNICATIONS", "Telecommunications"),
    ("TRANSPORTATION", "Transportation"),
    ("OTHER", "Other")
)

OPP_SOURCE = (
    ("call", "Call"),
    ("email", "Email"),
    ("existing customer", "Existing Customer"),
    ("partner", "Partner"),
    ("public relations", "Public Relations"),
    ("compaign", "Campaign"),
    ("other", "Other"),
)

PRIORITY_CHOICE = (
    ("Low", "Low"),
    ("Normal", "Normal"),
    ("High", "High"),
    ("Urgent", "Urgent"),
)

OPP_STAGES = (
    ("QUALIFICATION", "QUALIFICATION"),
    ("NEEDS ANALYSIS", "NEEDS ANALYSIS"),
    ("VALUE PROPOSITION", "VALUE PROPOSITION"),
    ("ID.DECISION MAKERS", "ID.DECISION MAKERS"),
    ("PERCEPTION ANALYSIS", "PERCEPTION ANALYSIS"),
    ("PROPOSAL/PRICE QUOTE", "PROPOSAL/PRICE QUOTE"),
    ("NEGOTIATION/REVIEW", "NEGOTIATION/REVIEW"),
    ("CLOSED WON", "CLOSED WON"),
    ("CLOSED LOST", "CLOSED LOST"),
)

ACC_STATUS = (
    ('Client', 'Client'),
    ('Prospect', 'Prospect'),
    ('Ex-Client', ('Ex-Client'))
)


ACC_CATEGORY = (
    ('Platinum', 'Platinum'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
    ('Bronce', 'Bronce'),

)

COUNTRIES = (
    ("AR", _("Argentina")),
    ("BO", _("Bolivia")),
    ("BR", _("Brazil")),
    ("CO", _("Colombia")),
    ("CR", _("Costa Rica")),
    ("EC", _("Ecuador")),
    ("SV", _("El Salvador")),
    ("GT", _("Guatemala")),
    ("HN", _("Honduras")),
    ("MX", _("Mexico")),
    ("NI", _("Nicaragua")),
    ("PA", _("Panama")),
    ("PY", _("Paraguay")),
    ("PE", _("Peru")),
    ("ES", _("Spain")),
    ("TT", _("Trinidad and Tobago")),
    ("US", _("United States")),
    ("UY", _("Uruguay")),
    ("VE", _("Venezuela")),
)

CURRENCY_CODES = (
    ("ARS", _("ARS, Peso")),
    ("BOB", _("BOB, Boliviano")),
    ("BRL", _("BRL, Real")),
    ("CLP", _("CLP, Peso")),
    ("COP", _("COP, Peso")),
    ("EUR", _("EUR, Euro")),
    ("MXN", _("MXN, Peso")),
    ("PEN", _("PEN, Sol")),
    ("USD", _("USD, Dollar")),
    ("UYU", _("UYU, Peso")),
)
