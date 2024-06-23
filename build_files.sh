echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py makemigrations --noinput
python3 manage.py makemigrations ftech_app --noinput
python3 manage.py migrate --noinput
echo "BUILD END"