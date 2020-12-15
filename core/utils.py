from django.utils.translation import ugettext_lazy as _

ACC_INDUSTRY = (
    ("Advertising", "Advertising"),
    ("Agriculture", "Agriculture"),
    ("Apparel & Accesories", "Apparel & Accesories"),
    ("Automotive", "Automotive"),
    ("Banking", "Banking"),
    ("Biotechnology", "Biotechnology"),
    ("Building, Material & Equipment", "Building & Equipment"),
    ("Chemical", "Chemical"),
    ("Education", "Education"),
    ("Electronics", "Electronics"),
    ("Utilities", "Utilities"),
    ("Oil & Gas", "Oil & Gas"),
    ("Entertainment & Leisure", "Entertainment & Leisure"),
    ("Finance", "Finance"),
    ("Food & Beverage", "Food & Beverage"),
    ("Grocery", "Grocery"),
    ("Healthcare", "Healthcare"),
    ("Insurance", "Insurance"),
    ("Legal", "Legal"),
    ("Manufacturing", "Manufacturing"),
    ("Publishing", "Publishing"),
    ("Real State", "Real State"),
    ("Service", "Service"),
    ("Sports", "Sports"),
    ("Technology", "Technology"),
    ("Telecommunications", "Telecommunications"),
    ("Transportation", "Transportation"),
    ("Other", "Other")
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
    ("Identification", "IDENTIFICATION"),
    ("In Contact", "IN CONTACT"),
    ("Under Analysis", "UNDER ANALYSIS"),
    ("Price Quote", "PRICE QUOTE"),
    ("Negotiation/Review", "NEGOTIATION/REVIEW"),
    ("Closed Won", "CLOSED WON"),
    ("Colsed Lost", "CLOSED LOST"),
)

ACC_STATUS = (
    ('Client', 'Client'),
    ('Prospect', 'Prospect'),
    ('Former Client', ('Former Client'))
)


ACC_CATEGORY = (
    ('Platinum', 'Platinum'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
    ('Bronce', 'Bronce'),

)

COUNTRIES = (
    ("Argentina", _("Argentina")),
    ("Bolivia", _("Bolivia")),
    ("Brazil", _("Brazil")),
    ("Colombia", _("Colombia")),
    ("Costa Rica", _("Costa Rica")),
    ("Ecuador", _("Ecuador")),
    ("El Salvador", _("El Salvador")),
    ("Guatemala", _("Guatemala")),
    ("Honduras", _("Honduras")),
    ("Mexico", _("Mexico")),
    ("Nicaragua", _("Nicaragua")),
    ("Panama", _("Panama")),
    ("Paraguay", _("Paraguay")),
    ("Peru", _("Peru")),
    ("Spain", _("Spain")),
    ("Trinidad and Tobago", _("Trinidad and Tobago")),
    ("United States", _("United States")),
    ("Uruguay", _("Uruguay")),
    ("Venezuela", _("Venezuela")),
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
