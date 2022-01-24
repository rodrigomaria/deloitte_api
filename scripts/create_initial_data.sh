echo "Create superuser"
export DJANGO_SUPERUSER_EMAIL=root@root.com
export DJANGO_SUPERUSER_PASSWORD=root
python manage.py createsuperuser --username root --no-input
echo "Running fixtures Posts"
python manage.py loaddata deloitte_api/fixtures/post.json
echo "Running fixtures Services"
python manage.py loaddata deloitte_api/fixtures/service.json
echo "Running fixtures TeamMembers"
python manage.py loaddata deloitte_api/fixtures/team_member.json