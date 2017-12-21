# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-10 17:19
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_salesforce_forms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_fieldplugin', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('required', models.BooleanField(default=False, verbose_name='Field is required')),
                ('name', models.CharField(help_text='Used to set the field name', max_length=255, verbose_name='Name')),
                ('template_set', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('required_message', models.TextField(blank=True, help_text='Error message displayed if the required field is left empty. Default: "This field is required".', null=True, verbose_name='Error message')),
                ('placeholder_text', models.CharField(blank=True, help_text='Default text in a form. Disappears when user starts typing. Example: "email@example.com"', max_length=255, verbose_name='Placeholder text')),
                ('initial_value', models.CharField(blank=True, help_text='Default value of field.', max_length=255, verbose_name='Initial value')),
                ('help_text', models.TextField(blank=True, help_text='Explanatory text displayed next to input field. Just like this one.', null=True, verbose_name='Help text')),
                ('min_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Min value')),
                ('max_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Max value')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FieldsetPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_fieldsetplugin', serialize=False, to='cms.CMSPlugin')),
                ('legend', models.CharField(blank=True, max_length=255, verbose_name='Legend')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
                ('template_set', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FormButtonPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_formbuttonplugin', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(max_length=255, verbose_name='Label')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FormPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_formplugin', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(help_text='Used to name the form instance.', max_length=255, verbose_name='Name')),
                ('client_id', models.CharField(default=djangocms_salesforce_forms.models.get_default_client_id, help_text='Client ID to use for the submission (_clientID field)', max_length=255, verbose_name='Client ID')),
                ('external_key', models.CharField(default=djangocms_salesforce_forms.models.get_default_external_key, help_text='DEManager External Key to use for the submission (_deExternalKey field)', max_length=255, verbose_name='External Key')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
                ('form_attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('form_template', models.CharField(choices=[('aldryn_forms/salesforceform/form.html', 'Default - form.html')], default='aldryn_forms/salesforceform/form.html', max_length=255, verbose_name='Template Form Name')),
                ('template_set', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template Set')),
                ('error_message', models.TextField(blank=True, help_text="An error message that will be displayed if the form doesn't validate.", null=True, verbose_name='Error message')),
                ('success_message', models.TextField(blank=True, help_text='An success message that will be displayed.', null=True, verbose_name='Success message')),
                ('redirect_type', models.CharField(choices=[('redirect_to_page', 'CMS Page'), ('redirect_to_url', 'Absolute URL')], help_text='Where to redirect the user when the form has been successfully sent?', max_length=20, verbose_name='Redirect to')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Absolute URL')),
                ('hidden_fields', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, help_text='Additional hidden fields to add to the form. (name/value)', verbose_name='Hidden Fields')),
                ('page', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='CMS Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('default_value', models.BooleanField(default=False, verbose_name='Default')),
                ('field', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='djangocms_salesforce_forms.FieldPlugin')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='TextAreaFieldPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_textareafieldplugin', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('required', models.BooleanField(default=False, verbose_name='Field is required')),
                ('name', models.CharField(help_text='Used to set the field name', max_length=255, verbose_name='Name')),
                ('template_set', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('required_message', models.TextField(blank=True, help_text='Error message displayed if the required field is left empty. Default: "This field is required".', null=True, verbose_name='Error message')),
                ('placeholder_text', models.CharField(blank=True, help_text='Default text in a form. Disappears when user starts typing. Example: "email@example.com"', max_length=255, verbose_name='Placeholder text')),
                ('initial_value', models.CharField(blank=True, help_text='Default value of field.', max_length=255, verbose_name='Initial value')),
                ('help_text', models.TextField(blank=True, help_text='Explanatory text displayed next to input field. Just like this one.', null=True, verbose_name='Help text')),
                ('min_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Min value')),
                ('max_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Max value')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
                ('text_area_columns', models.PositiveIntegerField(blank=True, null=True, verbose_name='columns')),
                ('text_area_rows', models.PositiveIntegerField(blank=True, null=True, verbose_name='rows')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TextFieldPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_salesforce_forms_textfieldplugin', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(blank=True, max_length=255, verbose_name='Label')),
                ('required', models.BooleanField(default=False, verbose_name='Field is required')),
                ('name', models.CharField(help_text='Used to set the field name', max_length=255, verbose_name='Name')),
                ('template_set', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('required_message', models.TextField(blank=True, help_text='Error message displayed if the required field is left empty. Default: "This field is required".', null=True, verbose_name='Error message')),
                ('placeholder_text', models.CharField(blank=True, help_text='Default text in a form. Disappears when user starts typing. Example: "email@example.com"', max_length=255, verbose_name='Placeholder text')),
                ('initial_value', models.CharField(blank=True, help_text='Default value of field.', max_length=255, verbose_name='Initial value')),
                ('help_text', models.TextField(blank=True, help_text='Explanatory text displayed next to input field. Just like this one.', null=True, verbose_name='Help text')),
                ('min_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Min value')),
                ('max_value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Max value')),
                ('custom_classes', models.CharField(blank=True, max_length=255, verbose_name='custom css classes')),
                ('type', models.CharField(choices=[('text', 'Text'), ('email', 'Email'), ('number', 'Number'), ('phone', 'Phone'), ('hidden', 'Hidden')], default='text', max_length=30, verbose_name='Type')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
