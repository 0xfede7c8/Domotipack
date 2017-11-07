#!/bin/bash
npm run build
rm -r ../backend/static ../backend/public
cp -r build ../backend/public
cp -r build/static ../backend/static
