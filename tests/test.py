import asyncio
from ascentrade_client import AscentradeClient

async def main():
	client = AscentradeClient("http://localhost:8042/graphql/")

	data = await client.currencies()
	for c in data.currencies:
		print(f'{c.id}: {c.name} ({c.iso_code})')


if __name__ == '__main__':
	asyncio.run(main())