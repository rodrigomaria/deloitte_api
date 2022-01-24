from apps.team_member import models


class TeamMemberRepository:
    model = models.TeamMember

    def get_all(self):
        return self.model.objects.all()

    def get_by_uuid(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def delete(self, uuid):
        post = self.get_by_uuid(uuid)
        post.delete()

    def create(self, name, function, address, mobile):
        return self.model.objects.create(name=name, function=function, address=address, mobile=mobile)


team_member_repository = TeamMemberRepository()
