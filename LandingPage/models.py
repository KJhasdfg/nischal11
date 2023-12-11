from django.db import models
from textblob import TextBlob



class AnalyzedText(models.Model):
    text = models.TextField()
    sentiment = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        analysis = TextBlob(self.text)
        self.sentiment = analysis.sentiment.polarity
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'LandingPage'