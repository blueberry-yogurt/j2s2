class HealthRepository:
    def get_source_name(self) -> str:
        # 나중에 DB/외부 리소스 상태 체크로 확장 가능
        return "repository"
