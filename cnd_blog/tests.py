import datetime
import logging

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from cnd_blog.models import Article


def create_entry(title, pub_date):
    """
    Create a blog entry with the given title, published on the given date.
    """
    lorem_ipsum="Lorem ipsum dolor sit amet, elit lorem in, pede et purus, habitant habitasse magnis nibh, integer conubia. Phasellus tortor fermentum imperdiet vitae, cras elementum feugiat dui ultrices, donec turpis id proin feugiat, nibh nulla, quisque mollis. Semper est eu est elit praesent. Fusce enim ut eu suspendisse scelerisque integer, diam amet morbi sed, metus pharetra fusce gravida vivamus. Mi nullam convallis ornare convallis et, ornare leo vivamus morbi. Quam sem turpis, eget diam, pretium facilisis vehicula sit orci nascetur aenean, dolor est mollis nec pretium. Ipsum mi nulla in vel eros, bibendum viverra. Nulla mauris, maecenas consequat non vulputate. Vulputate augue donec interdum, vulputate risus nulla turpis, quam duis. Placerat vestibulum dui scelerisque sem, a ut vitae, at nam, elit odio elit massa vestibulum ligula cum, tortor aliquam. Odio elit phasellus accumsan voluptas sed mattis, lorem ligula vulputate, eu venenatis rhoncus mauris vehicula ornare, libero vestibulum. Interdum urna vel odio, ac iusto semper massa, amet gravida quis etiam, odio vel eros."

    return Article.objects.create(title_text=title, pub_date=pub_date, blog_content=lorem_ipsum)

class EntryViewTests(TestCase):
    # Disable logging while running tests. It just spams the test results with errors.
    logging.disable(logging.CRITICAL)

    def test_archive_view_with_no_blogs(self):
        """
        If no blog entries exist (ie, only during testing), we should return 404.
        """
        response = self.client.get(reverse('archive'))
        self.assertEqual(response.status_code, 404)

    def test_archive_view_with_one_future_blog(self):
        """
        One future blog entry should not be displayed.
        """
        pub_date = timezone.now() + datetime.timedelta(days=30)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)

        response = self.client.get(reverse('archive'))
        self.assertEqual(response.status_code, 404)

    def test_archive_view_with_a_past_blog(self):
        """
        One past blog entry should be displayed with a title.
        """
        pub_date = timezone.now() - datetime.timedelta(days=30)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)

        response = self.client.get(reverse('archive'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article1.title_text)

    def test_year_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        response = self.client.get(reverse('article_year_archive', kwargs={"year": "2015"}))
        self.assertEqual(response.status_code, 404)

    def test_year_view_with_a_future_blog(self):
        """
        If a blog entry exists in the future, it should not be displayed.
        """
        pub_date = timezone.now() + datetime.timedelta(days=30)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)

        response = self.client.get(reverse('article_year_archive', kwargs={"year": str(pub_date.year)}))
        self.assertEqual(response.status_code, 404)
       
    def test_year_view_with_a_past_blog(self):
        """
        If a blog entry exists from the past in the requested year, it should be displayed.
        """
        pub_date = timezone.now() - datetime.timedelta(days=30)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)

        response = self.client.get(reverse('article_year_archive', kwargs={"year": str(pub_date.year)}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article1.title_text)
       
    def test_month_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        now = timezone.now()
        response = self.client.get(reverse('article_month_archive', kwargs={"year": str(now.year),
                                                                  "month": str(now.month)}))
        self.assertEqual(response.status_code, 404)

    def test_month_view_with_a_future_blog(self):
        """
        If a blog entry has a future date, it should not be displayed
        """
        pub_date = timezone.now() + datetime.timedelta(days=5)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)
        response = self.client.get(reverse('article_month_archive', kwargs={"year": str(pub_date.year),
                                                                  "month": str(pub_date.month)}))
        self.assertEqual(response.status_code, 404)

    def test_month_view_with_a_past_blog(self):
        """
        If a blog entry has a past date, it should be displayed
        """
        pub_date = timezone.now() - datetime.timedelta(days=5)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)
        response = self.client.get(reverse('article_month_archive', kwargs={"year": str(pub_date.year),
                                                                  "month": str(pub_date.month)}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article1.title_text)

    def test_day_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        now = timezone.now()
        response = self.client.get(reverse('article_day_archive', kwargs={"year": str(now.year),
                                                                 "month": str(now.month),
                                                                 "day": str(now.day)}))
        self.assertEqual(response.status_code, 404)

    def test_day_view_with_a_future_blog(self):
        """
        If no blog entries exist, we should display a message.
        """
        pub_date = timezone.now() + datetime.timedelta(days=1)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)
        response = self.client.get(reverse('article_day_archive', kwargs={"year": str(pub_date.year),
                                                                 "month": str(pub_date.month),
                                                                 "day": str(pub_date.day)}))
        self.assertEqual(response.status_code, 404)

    def test_day_view_with_a_past_blog(self):
        """
        If no blog entries exist, we should display a message.
        """
        pub_date = timezone.now() - datetime.timedelta(days=1)
        article1 = create_entry(title="Test article 1", pub_date=pub_date)
        response = self.client.get(reverse('article_day_archive', kwargs={"year": str(pub_date.year),
                                                                 "month": str(pub_date.month),
                                                                 "day": str(pub_date.day)}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article1.title_text)
