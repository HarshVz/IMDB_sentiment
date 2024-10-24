#!/bin/bash
gunicorn api.predict:app --bind 0.0.0.0:5000
