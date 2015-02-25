import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from cnd_blog.models import Post


def create_entry(title, pub_date):
    """
    Create a blog entry with the given title, published on the given date.
    """
    lorem_ipsum="Lorem ipsum dolor sit amet, elit lorem in, pede et purus, habitant habitasse magnis nibh, integer conubia. Phasellus tortor fermentum imperdiet vitae, cras elementum feugiat dui ultrices, donec turpis id proin feugiat, nibh nulla, quisque mollis. Semper est eu est elit praesent. Fusce enim ut eu suspendisse scelerisque integer, diam amet morbi sed, metus pharetra fusce gravida vivamus. Mi nullam convallis ornare convallis et, ornare leo vivamus morbi. Quam sem turpis, eget diam, pretium facilisis vehicula sit orci nascetur aenean, dolor est mollis nec pretium. Ipsum mi nulla in vel eros, bibendum viverra. Nulla mauris, maecenas consequat non vulputate. Vulputate augue donec interdum, vulputate risus nulla turpis, quam duis. Placerat vestibulum dui scelerisque sem, a ut vitae, at nam, elit odio elit massa vestibulum ligula cum, tortor aliquam. Odio elit phasellus accumsan voluptas sed mattis, lorem ligula vulputate, eu venenatis rhoncus mauris vehicula ornare, libero vestibulum. Interdum urna vel odio, ac iusto semper massa, amet gravida quis etiam, odio vel eros."

    return Post(title_text=title, pub_date=pub_date, blog_content=lorem_ipsum)

class EntryViewTests(TestCase):
    def test_year_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        response = self.client.get(reverse('year_index', kwargs={"year": "2015"}))
        self.assertEqual(response.status_code, 200)
       
    def test_month_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        response = self.client.get(reverse('month_index', kwargs={"year": "2015",
                                                                  "month": "2"}))
        self.assertEqual(response.status_code, 200)

    def test_day_view_with_no_blogs(self):
        """
        If no blog entries exist, we should display a message.
        """
        response = self.client.get(reverse('day_index', kwargs={"year": "2015",
                                                                 "month": "2",
                                                                 "day": "25"}))
        self.assertEqual(response.status_code, 200)