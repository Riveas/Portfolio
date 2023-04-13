from django.contrib import admin
from .models import home, aboutMe, links, category, skills, portfolio

# Register your models here.

# Home
admin.site.register(home)

# About
class ProfileInline(admin.TabularInline):
    model = links
    extra = 1


@admin.register(aboutMe)
class AboutAdmin(admin.ModelAdmin):
     inlines = [ProfileInline,]


# Skills
class SkillsInline(admin.TabularInline):
    model = skills
    extra = 2

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [SkillsInline,]

# Portfolio
admin.site.register(portfolio)
