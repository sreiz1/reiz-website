#!/bin/sh
# This script is used to deploy the application to dokku 
# via the reiznl intermediate repo

rm -rf ~/git/reiznl-deploy/*
cp -r dist/* ~/git/reiznl-deploy/
cd ~/git/reiznl-deploy
touch .static
git add .
git commit -m "Deploying to dokku"
git push dokku main
