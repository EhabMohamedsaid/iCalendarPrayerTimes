#!/bin/bash

git add .
git commit -m "Updated calendar for year " + "`date + '%Y'`"
git push origin main