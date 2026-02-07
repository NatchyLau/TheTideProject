FROM python:3.13-alpine AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/

WORKDIR /app

RUN pip wheel --wheel-dir=/wheels -r requirements.txt


# Final stage
FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /wheels /wheels

WORKDIR /app

RUN pip install --no-cache-dir /wheels/* \
    && rm -rf /wheels

COPY . /app

RUN adduser -D appuser && chown -R appuser /app && chmod +x /app/entrypoint.sh
USER appuser

RUN SECRET_KEY=dummy_value_for_build DATABASE_URL=sqlite:///dummy.db CLOUDFLARE_TURNSTILE_SECRET_KEY=fuckyou  python manage.py collectstatic --noinput

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--worker-class", "gthread", "--workers", "2", "--threads", "2", "the_tide_project.wsgi:application"]