from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self, *args, **kwargs) -> None:
        import cars.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready