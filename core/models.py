from django.db import models


# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'GeneralSetting: {self.name}'

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ('name',)


class Skill(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'Skills: {self.name}'

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ('name',)


class Work(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'Works: {self.name}'

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"
        ordering = ('name',)


class About(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'About: {self.name}'

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"
        ordering = ('name',)


class WorkSingle(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'WorkSingle: {self.name}'

    class Meta:
        verbose_name = "WorkSingle"
        verbose_name_plural = "WorkSingles"
        ordering = ('name',)


class Document(models.Model):
    order = models.IntegerField(
        default='',
        verbose_name='Order',
    )

    slug = models.SlugField(
        default = '',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )
    button_text = models.CharField(
        default = '',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
        help_text='',
    )

    file = models.FileField(
        default = '',
        verbose_name='File',
        blank=True,
        help_text='',
        upload_to='documents/',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_date = models.DateField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',

    )
    created_date = models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',

    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ('order',)


