git add .
git commit -m "$1"
git push origin -u main:main
docker build -t palondomus/caesaraigemini:latest .
docker push palondomus/caesaraigemini:latest
docker run -it -p 8080:8080 palondomus/caesaraigemini:latest