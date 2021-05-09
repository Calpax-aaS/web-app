from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from base.models import AuditModel


class Category(AuditModel):
    class Meta:
        verbose_name_plural = "Categories"

    display_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#000000')
    background_color = models.CharField(max_length=7, default='#FFFFFF')
    default_value = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.display_name, self.default_value)


class LeadOrigin(AuditModel):
    display_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#000000')
    background_color = models.CharField(max_length=7, default='#FFFFFF')
    default_value = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.display_name, self.default_value)

# Règles métiers
# -> Génération de la réf
# -> Si pas de choix sélectionner, mettre ceux par défaut

class FlightTicket(AuditModel):
    class FlightTicketStatus(models.TextChoices):
        UNPLANNED = 'UN', _('Unplanned')
        PLANNED = 'PL', _('Planned')
        PARTIALLY_ORGANIZED = 'PO', _('Partially_organized')
        ORGANIZED = 'OR', _('Organized')
        PARTIALLY_CANCELED = 'PC', _('Partially_canceled')
        PARTIALLY_DONE = 'PD', _('Partially_done')
        CANCELED = 'CA', _('Canceled')
        DONE = 'DO', _('Done')

    reference = models.CharField(max_length=20)
    expiration_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=FlightTicketStatus.choices,
        default=FlightTicketStatus.UNPLANNED,
    )
    reminder_date = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    amount = models.FloatField(default=0.0)

    # Type_planif ('Indetermine','auPlusVite','touteLaJournee','matin','soir','autre')
    # date_debut / date_fin
    # lieu_decollage souhaité
    # lieu de survol souhaité
    # Montgolfière souhaitée
    customer_request = models.JSONField(blank=True, null=True)
    gift_date = models.DateField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    lead_origin = models.ForeignKey(LeadOrigin, on_delete=models.RESTRICT)
