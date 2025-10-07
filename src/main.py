import asyncio
from src.orchestrator.teams import team


async def main():
    try:
        task = """
            I've been feeling very tired lately, and I'm not sure if it's related air quality, or something more serious.

            Can you:
            1. Analyze the air quality in my area (ZIP code 90210),
            2. And find nearby health centers or clinics I could visit for a check-up?
        """

        async for message in team.run_stream(task=task):
            print(message)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
