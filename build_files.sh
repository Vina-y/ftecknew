echo "BUILD START"
python -m pip3 install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations ftech_app --noinput
python3.9 manage.py migrate --noinput
echo "BUILD END"