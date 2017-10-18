# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel


# performer
# director
# year
# area
# type 类型
# score 评分
# status 状态
# summary 简介
# playlist

class Performer(models.Model):
    name = models.CharField(
        u'分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'演员'
        verbose_name_plural = u'演员管理'


class Director(models.Model):
    name = models.CharField(
        u'导演名称',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'导演'
        verbose_name_plural = u'导演管理'


class Area(models.Model):
    title = models.CharField(
        u'分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'地区'
        verbose_name_plural = u'地区管理'


class Channel(models.Model):
    title = models.CharField(
        u'分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = u'类别管理'


class Weblink(TimeStampedModel, StatusModel):
    STATUS = Choices(('draft', '草稿'), ('published', '发布'))

    name = models.CharField(u'网站名称', max_length=64)
    icon = models.URLField(u'网站图标', max_length=100)
    link = models.URLField(u'网站链接', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'友链'
        verbose_name_plural = u'友链管理'
        # app_label = u"我的应用"
        # db_table = 'apps_weblink'


class Comment(TimeStampedModel, StatusModel):
    STATUS = Choices(('draft', '草稿'), ('published', '发布'))

    name = models.CharField(u'网站名称', max_length=64)
    icon = models.URLField(u'网站图标', max_length=100)
    url = models.URLField(u'网站URL', max_length=100)

    # pubdate = models.DateField(u'发布时间', default=timezone.now())

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'评论管理'
        verbose_name_plural = u'评论管理'
        # app_label = u"我的应用"
        # db_table = 'apps_weblink'


class Category(models.Model):
    """
    Category model to be used for categorization of content. Categories are
    high level constructs to be used for grouping and organizing content,
    thus creating a site's table of contents.
    """
    title = models.CharField(
        u'分类标题',
        max_length=200,
        help_text='Short descriptive name for this category.',
    )

    subtitle = models.CharField(
        u'副标题',
        max_length=200,
        blank=True,
        null=True,
        default='',
        help_text='Some titles may be the same and cause confusion in admin '
                  'UI. A subtitle makes a distinction.',
    )

    slug = models.SlugField(
        u'slug',
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    channel = models.ForeignKey(Channel, null=True, blank=True, verbose_name=u'隶属于')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=u'隶属于')

    def __unicode__(self):
        return self.subtitle if self.subtitle else self.title

    class Meta:
        ordering = ('title',)
        verbose_name = u'类别'
        verbose_name_plural = u'类别管理'

    def save(self, *args, **kwargs):
        parent = self.parent

        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular references not allowed")

            parent = parent.parent

        super(Category, self).save(*args, **kwargs)

    @property
    def children(self):
        return self.category_set.all().order_by('title')

    @property
    def tags(self):
        return Tag.objects.filter(categories__in=[self]).order_by('title')

    def get_absolute_url(self):
        return reverse('category_object_list', kwargs={'category_slug': self.slug})


class Tags(models.Model):
    """
    Tag model to be used for tagging content. Tags are to be used to describe
    your content in more detail, in essence providing keywords associated with
    your content. Tags can also be seen as micro-categorization of a site's
    content.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this tag.',
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    # categories = models.ManyToManyField(
    #     Category,
    #     blank=True,
    #     null=True,
    #     help_text='Categories to which this tag belongs.'
    # )

    def __unicode__(self):
        return self.title

        # def save(self, *args, **kwargs):
        # self.slug = uuslug(self.title, instance=self)
        # super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签管理'


class Live(models.Model):
    """
    Tag model to be used for tagging content. Tags are to be used to describe
    your content in more detail, in essence providing keywords associated with
    your content. Tags can also be seen as micro-categorization of a site's
    content.
    """
    title = models.CharField(
        max_length=200,
        help_text='Short descriptive name for this tag.',
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        help_text='Short descriptive unique name for use in urls.',
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'直播'
        verbose_name_plural = u'直播管理'


class Video(TimeStampedModel, StatusModel):
    STATUS = Choices(('draft', '草稿'), ('published', '发布'))
    slug = models.CharField(u'视频标示', max_length=64)
    tags = models.ManyToManyField(Tags)

    title = models.CharField(u'视频标题', max_length=64)
    cover = models.ImageField(u'视频封面', upload_to='cover/', blank=False)
    views = models.IntegerField(u'浏览数', default=0)
    likes = models.IntegerField(u'喜欢数', default=0)
    count = models.IntegerField(u'视频数', default=0)

    # status = models.BooleanField(verbose_name=u'发布状态', default=False)

    created = models.DateTimeField(u'发布时间', auto_now=True)
    channel = models.ManyToManyField(Channel)
    comment = models.ForeignKey(Comment)

    playlist = models.TextField(verbose_name=u'播放列表', default='')
    category = models.ManyToManyField(Category)
    ordering = models.IntegerField(u'排序', default=9999)

    recommend = models.BooleanField(u'推荐', default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/detail/%s/" % self.id

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = u'视频管理'
        # app_label = u"我的应用"
        # db_table = 'apps_photo'


class Notice(TimeStampedModel, StatusModel):
    STATUS = Choices(('draft', '草稿'), ('published', '发布'))

    subject = models.CharField(u'公告标题', max_length=64)
    content = models.TextField(u'公告内容', blank=True)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = u'公告管理'
        verbose_name_plural = u'公告管理'
