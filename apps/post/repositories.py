from apps.post import models


class PostRepository:
    model = models.Post

    def get_all(self):
        return self.model.objects.all()

    def get_by_uuid(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def delete(self, uuid):
        post = self.get_by_uuid(uuid)
        post.delete()

    def create(self, content):
        return self.model.objects.create(content=content)


post_repository = PostRepository()
