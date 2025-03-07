git add .
git commit -m "$1"
git push origin -u main:main
docker build -t palondomus/caesaraigemini:1 .
docker push palondomus/caesaraigemini:1
docker run -it -p 8080:8080 palondomus/caesaraigemini:1