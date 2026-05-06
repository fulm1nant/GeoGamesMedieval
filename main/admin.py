import reversion
from django.contrib import admin
from .models import Country, Region, CountryAccess, Alliance

# ✅ 1. Регистрируем МОДЕЛИ для отслеживания истории
reversion.register(Country)
reversion.register(Region)
reversion.register(Alliance)


# ✅ 2. Наследуем админки от reversion.VersionAdmin (вместо admin.ModelAdmin)
@admin.register(Country)
class CountryAdmin(reversion.VersionAdmin):
    list_display = ('name', 'current_ruler', 'slug', 'order')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            access = request.user.country_access
            return qs.filter(pk=access.country.pk)
        except CountryAccess.DoesNotExist:
            return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        try:
            access = request.user.country_access
            return obj is None or obj.pk == access.country.pk
        except CountryAccess.DoesNotExist:
            return False

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Region)
class RegionAdmin(reversion.VersionAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            access = request.user.country_access
            return qs.filter(country=access.country)
        except CountryAccess.DoesNotExist:
            return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        try:
            access = request.user.country_access
            return obj is None or obj.country.pk == access.country.pk
        except CountryAccess.DoesNotExist:
            return False

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(CountryAccess)
class CountryAccessAdmin(admin.ModelAdmin):  # Обычный ModelAdmin, историю тут не нужно
    list_display = ('user', 'country')


@admin.register(Alliance)
class AllianceAdmin(reversion.VersionAdmin):
    list_display = ('name', 'alliance_type')
    filter_horizontal = ('members',)
