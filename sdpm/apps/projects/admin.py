from django.contrib import admin

from projects.models import Project,  Task



#class ProjectMemberInline(admin.TabularInline):
#    model = ProjectMember
#    extra = 1
#    min = 1

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]#ProjectMemberInline]
    




admin.site.register(Project, ProjectAdmin)