class Budget:
    def __init__(self):
        self._limits = {}

    def set_limit(self, category, limit):
        if limit <= 0:
            raise ValueError("limit must be positive")
        self._limits[category] = round(limit, 2)

    def limit_for(self, category):
        return self._limits.get(category)

    def remaining(self, category, spent):
        limit = self._limits.get(category)
        if limit is None:
            return None
        return round(limit - spent, 2)

    def is_exceeded(self, category, spent):
        limit = self._limits.get(category)
        if limit is None:
            return False
        return spent > limit
