from django.urls import path

from home_app.views import HomeView, BlogView, AboutView, PortfolioView, ShopView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('shop/', ShopView.as_view(), name='shop'),
]