from django.contrib import admin

from .models import ClientContact, HomePageGalleryView, Service


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "bootstrap_icon",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = (
        "id",
        "name",
    )
    ordering = ("-id",)


@admin.register(ClientContact)
class ClientContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "service",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = (
        "id",
        "name",
        "service",
    )
    ordering = ("-id",)


@admin.register(HomePageGalleryView)
class HomePageGalleryViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "alt",
    )
    list_display_links = ("id", "alt")
    search_fields = (
        "id",
        "alt",
    )
    ordering = ("-id",)
