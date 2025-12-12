from django.contrib import admin
from .models import Course, Module, Lesson, UserProgress, CourseEnrollment, Exam, ExamAttempt, Certification


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_type', 'status', 'coach_name', 'is_subscribers_only', 'created_at']
    list_filter = ['course_type', 'status', 'is_subscribers_only', 'is_accredible_certified']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'order']
    list_filter = ['course']
    ordering = ['course', 'order']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'module', 'order', 'lesson_type', 'video_duration', 'ai_generation_status']
    list_filter = ['course', 'lesson_type', 'ai_generation_status']
    search_fields = ['title', 'description', 'working_title', 'vimeo_id']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['course', 'order']
    fieldsets = (
        ('Basic Information', {
            'fields': ('course', 'module', 'title', 'slug', 'order', 'lesson_type')
        }),
        ('Video', {
            'fields': ('video_url', 'vimeo_url', 'vimeo_id', 'vimeo_thumbnail', 'vimeo_duration_seconds', 'video_duration', 'google_drive_url', 'google_drive_id')
        }),
        ('Lesson Creation', {
            'fields': ('working_title', 'rough_notes')
        }),
        ('AI Generated Content', {
            'fields': ('ai_generation_status', 'ai_clean_title', 'ai_short_summary', 'ai_full_description', 'ai_outcomes', 'ai_coach_actions')
        }),
        ('Resources', {
            'fields': ('description', 'workbook_url', 'resources_url')
        }),
    )


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'status', 'completed', 'video_watch_percentage', 'progress_percentage', 'last_accessed']
    list_filter = ['status', 'completed', 'last_accessed']
    search_fields = ['user__username', 'lesson__title']
    readonly_fields = ['last_accessed', 'started_at', 'completed_at']


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'payment_type', 'enrolled_at']
    list_filter = ['payment_type', 'enrolled_at']
    search_fields = ['user__username', 'course__name']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'passing_score', 'max_attempts', 'is_active']
    list_filter = ['is_active']
    search_fields = ['course__name', 'title']


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'exam', 'score', 'passed', 'started_at', 'completed_at', 'attempt_number']
    list_filter = ['passed', 'started_at', 'exam']
    search_fields = ['user__username', 'exam__course__name']
    readonly_fields = ['started_at', 'attempt_number']
    
    def attempt_number(self, obj):
        return obj.attempt_number()
    attempt_number.short_description = 'Attempt #'


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'status', 'issued_at', 'accredible_certificate_id']
    list_filter = ['status', 'issued_at']
    search_fields = ['user__username', 'course__name', 'accredible_certificate_id']
    readonly_fields = ['created_at', 'updated_at']
