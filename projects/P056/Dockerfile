FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home appuser
COPY src/ ./src/
USER appuser
ENV HOST=0.0.0.0
EXPOSE 8000
CMD ["python", "src/app.py"]
