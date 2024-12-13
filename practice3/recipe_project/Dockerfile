FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=recipe_project.settings

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install pytest pylint

RUN pylint recipe_project && pytest

CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "recipe_project.wsgi:application"]