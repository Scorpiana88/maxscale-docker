# Real World Project : Maxscale Sharded Database 

## Introduction Maxscale is a database proxy acting as an intermediary for the database requests. In this case our Sharded Database. 

## Running 
Pull the latest Maxscale image 
### docker pull mariadb/maxscale:latest
Run the container 
### docker run -d  mariadb/maxscale:latest

## Configuration 
Define your Maxscale Section and decide upon how many threads are going to be to be utilized.
### [maxscale] 
###threads=5
