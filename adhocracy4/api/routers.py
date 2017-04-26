from rest_framework import routers


class CustomRouterMixin():

    prefix_regex = None

    @property
    def routes(self):
        routes = super().routes
        return [route._replace(url=route.url.replace('{prefix}',
                                                     self.prefix_regex))
                for route in routes]


class ContentTypeRouterMixin(CustomRouterMixin):

    prefix_regex = (
        'contenttypes/(?P<content_type>[\d]+)/'
        'objects/(?P<object_pk>[\d]+)/{prefix}'
    )


class ContentTypeSimpleRouter(ContentTypeRouterMixin, routers.SimpleRouter):
    pass


class ContentTypeDefaultRouter(ContentTypeRouterMixin, routers.DefaultRouter):
    pass


class ModuleRouterMixin(CustomRouterMixin):

    prefix_regex = (
        'modules/(?P<module_pk>[\d]+)/{prefix}'
    )


class ModuleSimpleRouter(ModuleRouterMixin, routers.SimpleRouter):
    pass


class ModuleDefaultRouter(ModuleRouterMixin, routers.DefaultRouter):
    pass
