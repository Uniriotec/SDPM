from django.contrib import admin

from projects.models import Project, ProjectMember, Task



class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember
    extra = 1
    min = 1

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMemberInline,TaskInline]
    




admin.site.register(Project, ProjectAdmin)