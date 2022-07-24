#!/usr/bin/env sh

######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : entrypoint
# @created     : Thursday Jun 02, 2022 01:17:24 CST
#
# @description : 
######################################################################


alembic upgrade head


if [ "$1" = "api" ]; then
	gunicorn  --worker-class gevent -w 4 --worker-connections 1000 -b 0.0.0.0:8000 'jobaggrv-api.app:app'
else 
	gunicorn  --worker-class gevent -w 4 --worker-connections 1000 -b 0.0.0.0:8000 'jobaggrv-api.app:app'	
#elif [ "$1" = "scrapy" ]; then
