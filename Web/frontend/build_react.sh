#!/bin/bash
npm run build
rm -r ../backend/static ../backend/public ../backend/resources
cp -r build ../backend/public
cp -r build/resources ../backend/resources
cp -r build/static ../backend/static
