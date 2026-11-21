"""Учебная выгрузка записей организации."""


def export_rows(rows: list[tuple[str, int]], organization: str) -> list[int]:
    """Вернуть идентификаторы организации с повторами. Порядок произвольный."""
    return [identifier for owner, identifier in rows if owner == organization]
