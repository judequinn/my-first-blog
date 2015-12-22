from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class AdvancedEditor(forms.Textarea):
    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'advancededitor'}
        if attrs: self.attrs.update(attrs)
        super(AdvancedEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(AdvancedEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
        <script type="text/javascript">
        tinyMCE.init({           
            theme: "advanced",
            plugins: "advhr,table,emotions,media,insertdatetime,directionality,",
            theme_advanced_toolbar_align: "left",
            theme_advanced_toolbar_location: "top",             
            theme_advanced_buttons1:"italic,underline,strikethrough,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,formatselect,fontselect,fontsizeselect,forecolor",
            theme_advanced_buttons2:"bullist,numlist,outdent,indent,ltr,rtl,separator,link,unlink,anchor,image,separator,table,insertdate,inserttime,advhr,emotions,media,charmap,separator,undo,redo",
            theme_advanced_buttons3_add:"forecolor,backcolor",
            theme_advanced_font_sizes:"170%,10px,11px,12px,13px,14px,15px,16px,17px,18px,19px,20px,21px,22px,23px,24px,25px,26px,27px,28px,29px,30px,32px,48px",
            height: "350px",
            width: "653px"
        });
        </script>''')