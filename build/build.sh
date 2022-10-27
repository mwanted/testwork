#!/usr/bin/env sh

tar -cvf app.tar -C ../app/ . --exclude-from=../.gitignore

docker build -f Dockerfile -t mw/testwork:master . 

rm -rf app.tar

docker tag mw/testwork:master remidor/private:testwork
docker push remidor/private:testwork