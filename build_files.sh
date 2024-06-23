# echo "BUILD START"
# python3.9 -m pip install -r requirements.txt
# echo "requirements installed"
# python3.9 manage.py collectstatic --noinput --clear
# python3.9 manage.py makemigrations --noinput
# python3.9 manage.py makemigrations ftech_app --noinput
# python3.9 manage.py migrate --noinput
# echo "BUILD END"

 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"