# faq_app/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang_code = request.query_params.get('lang', 'en')
        faqs = self.get_queryset()
        for faq in faqs:
            faq.question = faq.get_translation(lang_code)
        serializer = self.get_serializer(faqs, many=True)
        return Response(serializer.data)
