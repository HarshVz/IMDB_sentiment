#!/bin/bash
gunicorn api.predict:app --bind 0.0.0.0:10000
