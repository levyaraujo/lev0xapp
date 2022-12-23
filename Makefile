run:
	flask --debug --app src.app:create_app run

app:
	sudo chown -R lev0x data 
	docker compose down
	docker compose up --build