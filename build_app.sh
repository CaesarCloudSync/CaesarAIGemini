git add .
git commit -m "$1"
git push origin -u main:main
docker build -t palondomus/caesaraigemini:newest .
docker push palondomus/caesaraigemini:newest
docker run -it -p 8080:8080 palondomus/caesaraigemini:newest