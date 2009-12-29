# -*- coding: utf-8 -*-

# django
from django.contrib.admin import helpers, ModelAdmin
from django.utils.safestring import mark_safe


class BaseEntityAdmin(ModelAdmin):

    def render_change_form(self, request, context, **kwargs):
        """
        Wrapper for ModelAdmin.render_change_form. Replaces standard static
        AdminForm with an EAV-friendly one. The point is that our form generates
        fields dynamically and fieldsets must be inferred from a prepared and
        validated form instance, not just the form class. Django does not seem
        to provide hooks for this purpose, so we simply wrap the view and
        substitute some data.
        """
        form = context['adminform'].form

        # infer correct data from the form
        fieldsets = [(None, {'fields': form.fields.keys()})]
        adminform = helpers.AdminForm(form, fieldsets, self.prepopulated_fields)
        media = mark_safe(self.media + adminform.media)

        context.update(adminform=adminform, media=media)

        return super(BaseEntityAdmin, self).render_change_form(request, context, **kwargs)


class BaseSchemaAdmin(ModelAdmin):

    list_display = ('title', 'name', 'datatype', 'help_text', 'required')
    prepopulated_fields = {'name': ('title',)}
