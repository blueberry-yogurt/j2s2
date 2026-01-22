import random
from app.models.question import Question


class QuestionRepository:
    @staticmethod
    async def get_random_question():
        count = await Question.all().count()
        if count == 0:
            return None

        random_index = random.randint(0, count - 1)

        return await Question.all().offset(random_index).first()
