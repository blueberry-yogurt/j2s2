from app.repositories.health_repo import HealthRepository


class HealthService:
    def __init__(self, repo: HealthRepository):
        self.repo = repo

    def health(self) -> dict:
        return {"status": "ok", "source": self.repo.get_source_name()}
