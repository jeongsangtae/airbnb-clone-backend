from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class RatingFilter(admin.SimpleListFilter):

    title = "Filter by rating!"

    parameter_name = "input_rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        if self.value() == "good":
            return reviews.filter(rating__gte=3)
        elif self.value() == "bad":
            return reviews.filter(rating__lt=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        RatingFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
