#!/usr/bin/env python
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015, django ERP Team'
__version__ = '0.0.5'

from hashlib import md5
from django import template
from django.utils.html import format_html, mark_safe, escape

register = template.Library()

@register.simple_tag
def avatar(email, size=32, default="mm", css_class="avatar image"):
    """Returns the gravatar image associated to the given email.
    
    More info: http://www.gravatar.com

    Example tag usage: {% avatar email_address 80 "http://.../my_default_image.jpg" [css_class] %}
    """        
    # Creates and returns the URL.
    h = ""
    if email:
        h = md5(email.encode('utf-8')).hexdigest()
    url = 'http://www.gravatar.com/avatar/%s?s=%s&r=g' % (h, escape(size))
    
    # Adds a default image URL (if present).
    if default:
        url += "&d=%s" % escape(default)
    
    url = mark_safe(url)
        
    return format_html('<img class="{}" width="{}" height="{}" src="{}" />', css_class, size, size, url)

