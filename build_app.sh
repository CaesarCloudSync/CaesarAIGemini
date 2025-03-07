git add .
git commit -m "$1"
git push origin -u main:main
docker build -t palondomus/caesaraigemini:finest .
docker push palondomus/caesaraigemini:finest
docker run -it -p 8080:8080 palondomus/caesaraigemini:finest