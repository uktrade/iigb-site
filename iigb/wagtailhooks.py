from django.conf import settings
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register('insert_global_admin_js')
def insert_js():
    return format_html('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">')
