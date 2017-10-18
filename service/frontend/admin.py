# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from suit.widgets import NumberInput

from .models import Video, Notice, Category, Tags, Channel, Weblink


def published(modeladmin, request, queryset):
    queryset.update(status=1)


def recommend(modeladmin, request, queryset):
    queryset.update(recommend=1)


published.short_description = u"发布所选的项目"
recommend.short_description = u"推荐所选的项目"


class VideoForm(ModelForm):
    class Meta:
        widgets = {
            'count': NumberInput(attrs={'class': 'input-mini'}),
            'ordering': NumberInput(attrs={'class': 'input-mini'}),
        }


class VideoInline(admin.TabularInline):
    model = Video
    suit_classes = 'suit-tab suit-tab-cities'


class TabbedVideoAdmin(ModelAdmin):
    # inlines = (VideoInline,)

    def preview(self, obj):
        return '<img src="%s" height="64" width="64" />' % (obj.cover)

    sortable = 'ordering'
    form = VideoForm
    actions = [published, recommend]

    list_display = ('title', 'views', 'likes', 'count', 'created', 'recommend', 'status')
    search_fields = ('title', 'created')

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            -1: 'error',
        }.get(obj.status)

        if css_class:
            return {'class': css_class, 'data': obj.title}

    def suit_cell_attributes(self, obj, column):
        if column == 'status' or column == 'recommend':
            return {'class': 'text-center'}
        elif column == 'status':
            return {'class': 'text-error'}

    # Or bit more advanced example
    def suit_row_attributes(self, obj, request):

        css_class = {1: 'success', 0: 'warning', -1: 'error', }.get(obj.status)

        if css_class:
            return {'class': css_class, 'data': obj.title}

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'slug', 'cover', 'playlist', 'category', 'tags']
        }),
        (None, {
            'classes': ('suit-tab suit-tab-info',),
            'fields': ['views', 'likes', 'count', 'ordering', 'recommend', 'status']}
         ),
    ]

    suit_form_tabs = (('general', u'基本'), ('info', u'扩展'))
    suit_form_includes = None


class WeblinkAdmin(ModelAdmin):
    list_display = ('name', 'icon', 'link')
    search_fields = ('name', 'link')


class NoticeForm(ModelForm):
    class Meta:
        # model = Notice
        widgets = {
            # 'content': RedactorWidget(editor_options = {'autoresize': True}),
            # 'content': RedactorWidget,
            # 'content': RedactorWidget(editor_options={'buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}),
            # 'content': CKEditorWidget(editor_options=_ck_editor_config),
        }


class NoticeAdmin(ModelAdmin):
    form = NoticeForm
    search_fields = ('subject', 'created',)
    list_display = ('subject', 'created',)

    fieldsets = [
        (None, {'fields': ['subject']}),
        ('Content', {'classes': ('full-width',), 'description': 'Full width example', 'fields': ('content',)})
    ]


class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'subtitle')


admin.site.register(Tags)
admin.site.register(Channel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Weblink, WeblinkAdmin)
admin.site.register(Video, TabbedVideoAdmin)
