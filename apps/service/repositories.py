from apps.service import models


class ServiceRepository:
    model = models.Service

    def get_all(self):
        return self.model.objects.all()

    def get_by_uuid(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def delete(self, uuid):
        post = self.get_by_uuid(uuid)
        post.delete()

    def create(self, title, description):
        return self.model.objects.create(title=title, description=description)


service_repository = ServiceRepository()
